"""Install command — interactive install flow."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from research_driven_setup import __version__
from research_driven_setup.core.bootstrap import inspect_environment
from research_driven_setup.core.conflict_policy import ConflictAction
from research_driven_setup.core.manifest import load_manifest
from research_driven_setup.core.mcp import compose_mcp_config, generate_mcp_onboarding_notes, write_mcp_config
from research_driven_setup.core.profiles import get_default_profile, list_available_profiles, resolve_profile
from research_driven_setup.core.renderer import render_workspace
from research_driven_setup.core.report import generate_install_report, write_install_report
from research_driven_setup.core.secrets import _write_env_example, prompt_for_secrets, prompt_github_mcp_setup
from research_driven_setup.core.workspace_state import detect_workspace_state

console = Console()


def install(
    workspace: Path = typer.Option(None, "--workspace", "-w", help="Target workspace directory."),
    profile: str = typer.Option(None, "--profile", "-p", help="Installation profile name."),
    force: bool = typer.Option(False, "--force", "-f", help="Force overwrite existing files."),
    non_interactive: bool = typer.Option(False, "--non-interactive", "--yes", "-y", help="Skip interactive prompts."),
) -> None:
    """Run the interactive install flow."""
    target = workspace or Path.cwd()
    target = target.resolve()

    console.print()
    console.print(f"[bold]Target workspace:[/bold] {target}")
    console.print()

    # Step 1: Environment checks
    console.print("[bold cyan]Step 1/6:[/bold cyan] Checking environment prerequisites...")
    bootstrap = inspect_environment()

    table = Table(title="Environment Check", show_header=True)
    table.add_column("Tool", style="bold")
    table.add_column("Status")
    table.add_column("Version")
    table.add_column("Action")

    for check in bootstrap.checks:
        status = "[green]✓[/green]" if check.found else ("[red]✗[/red]" if check.required else "[yellow]⚠[/yellow]")
        table.add_row(
            check.name,
            status,
            check.version or ("-" if not check.found else "found"),
            check.remediation or "",
        )
    console.print(table)
    console.print()

    if not bootstrap.all_required_met:
        console.print(Panel(
            "[bold red]Missing required prerequisites![/bold red]\n\n"
            "Please install the missing tools listed above and retry.",
            border_style="red",
        ))
        if not non_interactive:
            proceed = typer.confirm("Continue anyway?", default=False)
            if not proceed:
                raise typer.Exit(1)

    # Step 2: Profile selection
    console.print("[bold cyan]Step 2/6:[/bold cyan] Selecting installation profile...")
    if profile:
        selected_profile = resolve_profile(profile)
    elif non_interactive:
        selected_profile = get_default_profile()
    else:
        profiles = list_available_profiles()
        console.print()
        for i, p in enumerate(profiles, 1):
            marker = " [bold green](default)[/bold green]" if p.name == "ubuntu-research" else ""
            console.print(f"  {i}. [bold]{p.display_name}[/bold]{marker}")
            console.print(f"     {p.description}")
        console.print()
        choice = typer.prompt(
            "Select profile (number or name)",
            default="1",
        )
        try:
            idx = int(choice) - 1
            selected_profile = profiles[idx]
        except (ValueError, IndexError):
            selected_profile = resolve_profile(choice)

    console.print(f"[green]✓[/green] Profile: [bold]{selected_profile.display_name}[/bold]")
    console.print()

    # Step 3: Workspace state check
    console.print("[bold cyan]Step 3/6:[/bold cyan] Inspecting workspace state...")
    state = detect_workspace_state(target)
    if state.is_installed:
        console.print(f"[yellow]⚠[/yellow] Workspace already installed (v{state.installed_version})")
        if not force and not non_interactive:
            proceed = typer.confirm("Continue with re-install? Existing managed files will follow conflict policy.", default=True)
            if not proceed:
                raise typer.Exit(0)
    elif state.is_fresh:
        console.print("[green]✓[/green] Fresh workspace — clean install")
    else:
        console.print("[yellow]⚠[/yellow] Workspace has existing .github/ or .vscode/ content")
    console.print()

    # Step 4: Render templates
    console.print("[bold cyan]Step 4/6:[/bold cyan] Rendering workspace assets...")
    manifest = load_manifest()
    render_results = render_workspace(manifest, target, force=force)

    written = sum(1 for r in render_results if r.action in (ConflictAction.WRITE, ConflictAction.OVERWRITE))
    skipped = sum(1 for r in render_results if r.action == ConflictAction.SKIP)
    blocked = sum(1 for r in render_results if r.action == ConflictAction.BLOCK)
    console.print(f"  [green]✓[/green] {written} file(s) written")
    if skipped:
        console.print(f"  [yellow]⏭[/yellow] {skipped} file(s) skipped (already exist)")
    if blocked:
        console.print(f"  [red]🚫[/red] {blocked} file(s) blocked (conflicts)")
    console.print()

    # Step 5: MCP configuration and secrets
    console.print("[bold cyan]Step 5/6:[/bold cyan] Configuring MCP servers...")
    if non_interactive:
        secrets: dict[str, str | None] = {}
        enable_github = True
        _write_env_example(target)
    else:
        secrets = prompt_for_secrets(target)
        enable_github = prompt_github_mcp_setup()

    profile_servers = list(selected_profile.mcp_servers)
    if not enable_github and "github" in profile_servers:
        profile_servers.remove("github")

    mcp_config = compose_mcp_config(manifest, profile_servers, secrets)
    write_mcp_config(target, mcp_config)
    console.print("[green]✓[/green] .vscode/mcp.json generated")

    mcp_notes = generate_mcp_onboarding_notes(manifest, profile_servers, secrets)
    console.print()

    # Step 5.5: Generate package.json and run npm install
    _generate_package_json(target)
    console.print("[green]✓[/green] package.json generated")

    if not non_interactive:
        run_npm = typer.confirm("Run 'npm install' to install MCP server dependencies?", default=True)
    else:
        run_npm = True

    if run_npm:
        console.print("[dim]Running npm install...[/dim]")
        result = subprocess.run(
            ["npm", "install"],
            cwd=str(target),
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0:
            console.print("[green]✓[/green] npm dependencies installed")
        else:
            console.print(f"[yellow]⚠[/yellow] npm install completed with issues: {result.stderr[:200]}")
    console.print()

    # Step 6: Report
    console.print("[bold cyan]Step 6/6:[/bold cyan] Generating install report...")
    report_data = generate_install_report(
        workspace=target,
        profile_name=selected_profile.name,
        version=__version__,
        render_results=render_results,
        mcp_notes=mcp_notes,
        bootstrap_ok=bootstrap.all_required_met,
    )
    json_path, md_path = write_install_report(target, report_data)
    console.print(f"[green]✓[/green] Report written to {md_path.relative_to(target)}")
    console.print()

    # Final summary
    console.print(Panel(
        f"[bold green]Installation Complete![/bold green]\n\n"
        f"Profile: {selected_profile.display_name}\n"
        f"Version: {__version__}\n"
        f"Files written: {written}\n"
        f"Files skipped: {skipped}\n\n"
        + (
            "[bold yellow]Next steps:[/bold yellow]\n"
            "1. Open VS Code in this workspace\n"
            "2. Start MCP servers from the Command Palette\n"
            "3. Run 'research-driven-setup doctor' to verify\n"
            + (
                "\n[bold]MCP Notes:[/bold]\n" + "\n".join(f"  • {n}" for n in mcp_notes)
                if mcp_notes
                else ""
            )
        ),
        border_style="green",
    ))


def _generate_package_json(workspace: Path) -> None:
    """Generate package.json with MCP server npm dependencies."""
    pkg_path = workspace / "package.json"
    if pkg_path.exists():
        # Merge devDependencies
        try:
            existing = json.loads(pkg_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            existing = {}
    else:
        existing = {}

    existing.setdefault("name", workspace.name)
    existing.setdefault("version", "1.0.0")
    existing.setdefault("private", True)
    existing.setdefault("description", "Workspace for research-driven development with MCP servers.")
    existing.setdefault("type", "commonjs")

    deps = existing.setdefault("devDependencies", {})
    deps.setdefault("@modelcontextprotocol/sdk", "^1.29.0")
    deps.setdefault("@modelcontextprotocol/server-filesystem", "^2026.1.14")
    deps.setdefault("@modelcontextprotocol/server-sequential-thinking", "^2025.12.18")
    deps.setdefault("open-websearch", "^2.1.5")

    pkg_path.write_text(json.dumps(existing, indent=2) + "\n", encoding="utf-8")
