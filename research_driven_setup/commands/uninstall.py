"""Uninstall command — remove framework assets from workspace."""

from __future__ import annotations

import json
import shutil
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


def uninstall(
    workspace: Path = typer.Option(None, "--workspace", "-w", help="Target workspace directory."),
    keep_mcp: bool = typer.Option(False, "--keep-mcp", help="Keep .vscode/mcp.json configuration."),
    keep_npm: bool = typer.Option(False, "--keep-npm", help="Keep package.json and node_modules."),
    non_interactive: bool = typer.Option(False, "--non-interactive", "--yes", "-y", help="Skip confirmation prompts."),
) -> None:
    """Remove research-driven-setup assets from the workspace."""
    target = (workspace or Path.cwd()).resolve()

    console.print()
    console.print(f"[bold]Target workspace:[/bold] {target}")
    console.print()

    # Detect install marker
    marker_path = target / ".research-driven" / "install.json"
    if not marker_path.is_file():
        console.print(
            Panel(
                "[bold yellow]No install marker found.[/bold yellow]\n\n"
                "This workspace does not appear to have been set up by research-driven-setup.\n"
                "If files were installed manually, remove them by hand.",
                border_style="yellow",
            )
        )
        raise typer.Exit(1)

    try:
        marker = json.loads(marker_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        console.print(f"[red]✗[/red] Could not read install marker: {exc}")
        raise typer.Exit(1) from exc

    installed_version = marker.get("version", "unknown")
    files_written = marker.get("files_written", [])

    # Build removal plan
    to_remove: list[tuple[str, str]] = []  # (path, reason)

    for rel_path in files_written:
        full = target / rel_path
        if not full.exists():
            continue
        if keep_mcp and rel_path == ".vscode/mcp.json":
            continue
        if keep_npm and rel_path in ("package.json",):
            continue
        to_remove.append((rel_path, "installed file"))

    # Generated files not tracked in files_written
    mcp_json = target / ".vscode" / "mcp.json"
    if mcp_json.is_file() and not keep_mcp and (".vscode/mcp.json", "installed file") not in to_remove:
        to_remove.append((".vscode/mcp.json", "generated MCP config"))

    pkg_json = target / "package.json"
    if pkg_json.is_file() and not keep_npm and ("package.json", "installed file") not in to_remove:
        to_remove.append(("package.json", "generated npm manifest"))

    pkg_lock = target / "package-lock.json"
    if pkg_lock.is_file() and not keep_npm:
        to_remove.append(("package-lock.json", "npm lock file"))

    # .research-driven/ directory (marker + reports)
    rd_dir = target / ".research-driven"
    if rd_dir.is_dir():
        to_remove.append((".research-driven", "install marker & reports"))

    # .env.example (generated during install)
    env_example = target / ".env.example"
    if env_example.is_file():
        to_remove.append((".env.example", "generated env example"))

    # node_modules if not keeping npm
    if not keep_npm:
        nm = target / "node_modules"
        if nm.is_dir():
            to_remove.append(("node_modules", "npm dependencies"))

    if not to_remove:
        console.print("[green]✓[/green] Nothing to remove.")
        return

    # Show plan
    table = Table(title="Uninstall Plan", show_header=True)
    table.add_column("Path", style="bold")
    table.add_column("Reason")

    for path, reason in to_remove:
        table.add_row(path, reason)

    console.print(table)
    console.print()
    console.print(f"[bold]Installed version:[/bold] {installed_version}")
    console.print(f"[bold]Files to remove:[/bold] {len(to_remove)}")
    console.print()

    if not non_interactive:
        proceed = typer.confirm("Proceed with uninstall?", default=False)
        if not proceed:
            console.print("[dim]Aborted.[/dim]")
            raise typer.Exit(0)

    # Execute removal
    removed = 0
    errors = 0

    for rel_path, _reason in to_remove:
        full = target / rel_path
        try:
            if full.is_dir():
                shutil.rmtree(full)
            elif full.is_file():
                full.unlink()
            removed += 1
        except OSError as exc:
            console.print(f"  [red]✗[/red] Failed to remove {rel_path}: {exc}")
            errors += 1

    # Clean up empty parent directories
    _cleanup_empty_dirs(target / ".github")
    _cleanup_empty_dirs(target / ".vscode")

    console.print()
    if errors:
        console.print(f"[yellow]⚠[/yellow] Removed {removed} item(s), {errors} error(s).")
    else:
        console.print(
            Panel(
                f"[bold green]Uninstall complete![/bold green]\n\n"
                f"Removed {removed} item(s) from workspace.\n\n"
                "[bold]To also remove the CLI tool itself:[/bold]\n"
                "  uv tool uninstall research-driven-setup",
                border_style="green",
            )
        )


def _cleanup_empty_dirs(root: Path) -> None:
    """Remove empty directories bottom-up under root."""
    if not root.is_dir():
        return
    # Walk bottom-up
    for dirpath in sorted(root.rglob("*"), reverse=True):
        if dirpath.is_dir() and not any(dirpath.iterdir()):
            dirpath.rmdir()
    # Remove root if empty too
    if root.is_dir() and not any(root.iterdir()):
        root.rmdir()
