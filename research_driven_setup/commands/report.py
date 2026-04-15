"""Report command — show last install or doctor report."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.markdown import Markdown

console = Console()


def report(
    workspace: Path = typer.Option(None, "--workspace", "-w", help="Target workspace directory."),
    kind: str = typer.Option("install", "--kind", "-k", help="Report type: install or doctor."),
) -> None:
    """Show the last install or doctor report."""
    target = (workspace or Path.cwd()).resolve()
    diag_dir = target / ".research-driven"

    if kind == "install":
        md_path = diag_dir / "install-report.md"
    elif kind == "doctor":
        md_path = diag_dir / "doctor-report.md"
    else:
        console.print(f"[red]Unknown report type: {kind}[/red]")
        raise typer.Exit(1)

    if not md_path.exists():
        console.print(f"[yellow]No {kind} report found.[/yellow]")
        console.print(f"Run 'research-driven-setup {kind}' first.")
        raise typer.Exit(1)

    content = md_path.read_text(encoding="utf-8")
    console.print()
    console.print(Markdown(content))
    console.print()
