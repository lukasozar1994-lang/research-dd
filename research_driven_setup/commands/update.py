"""Update command — safe workspace update."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from research_driven_setup import __version__
from research_driven_setup.core.updater import apply_update, plan_update

console = Console()


def update(
    workspace: Path = typer.Option(None, "--workspace", "-w", help="Target workspace directory."),
    force: bool = typer.Option(False, "--force", "-f", help="Force update even with conflicts."),
    dry_run: bool = typer.Option(False, "--dry-run", help="Preview changes without applying."),
) -> None:
    """Update the workspace to a newer framework release."""
    target = (workspace or Path.cwd()).resolve()

    console.print()
    console.print(f"[bold]Updating workspace:[/bold] {target}")
    console.print()

    plan = plan_update(target)

    if plan.current_version == __version__:
        console.print(f"[green]✓[/green] Workspace is already at version {__version__}")
        return

    console.print(f"Current version: {plan.current_version or 'unknown'}")
    console.print(f"Target version:  {__version__}")
    console.print()

    if not plan.actions:
        console.print("[green]✓[/green] No changes needed")
        return

    table = Table(title="Update Plan", show_header=True)
    table.add_column("File", style="bold")
    table.add_column("Action")
    table.add_column("Reason")

    action_icon = {
        "new": "[green]+ new[/green]",
        "update": "[cyan]↑ update[/cyan]",
        "skip": "[yellow]⏭ skip[/yellow]",
        "conflict": "[red]⚠ conflict[/red]",
    }

    for action in plan.actions:
        table.add_row(
            action.path,
            action_icon.get(action.action, action.action),
            action.reason,
        )

    console.print(table)
    console.print()

    if plan.has_conflicts and not force:
        console.print(Panel(
            "[bold red]Conflicts detected![/bold red]\n\n"
            "Some files have been modified locally and cannot be safely overwritten.\n"
            "Use --force to overwrite, or resolve conflicts manually.",
            border_style="red",
        ))
        if not dry_run:
            raise typer.Exit(1)

    if dry_run:
        console.print("[dim]Dry run — no changes applied.[/dim]")
        return

    if not force:
        proceed = typer.confirm("Apply update?", default=True)
        if not proceed:
            raise typer.Exit(0)

    apply_update(target, force=force)
    console.print(f"\n[bold green]Workspace updated to v{__version__}[/bold green]")
