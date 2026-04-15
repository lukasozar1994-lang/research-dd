"""Doctor command — workspace diagnostics."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from research_driven_setup.core.doctor import run_doctor
from research_driven_setup.core.report import generate_doctor_report_files

console = Console()


def doctor(
    workspace: Path = typer.Option(None, "--workspace", "-w", help="Target workspace directory."),
) -> None:
    """Validate prerequisites, generated assets, and MCP readiness."""
    target = (workspace or Path.cwd()).resolve()

    console.print()
    console.print(f"[bold]Diagnosing workspace:[/bold] {target}")
    console.print()

    report = run_doctor(target)

    status_icon = {"pass": "[green]✓[/green]", "warn": "[yellow]⚠[/yellow]", "fail": "[red]✗[/red]"}

    table = Table(title="Doctor Report", show_header=True)
    table.add_column("Category", style="bold")
    table.add_column("Check")
    table.add_column("Status")
    table.add_column("Detail")
    table.add_column("Remediation")

    for check in report.checks:
        table.add_row(
            check.category,
            check.name,
            status_icon.get(check.status, "?"),
            check.detail,
            check.remediation or "",
        )

    console.print(table)
    console.print()

    json_path, md_path = generate_doctor_report_files(target, report)

    if report.passed:
        console.print("[bold green]All checks passed![/bold green]")
    else:
        failures = report.failures
        warnings = report.warnings
        if failures:
            console.print(f"[bold red]{len(failures)} check(s) failed[/bold red]")
        if warnings:
            console.print(f"[bold yellow]{len(warnings)} warning(s)[/bold yellow]")

    console.print(f"\n[dim]Full report: {md_path.relative_to(target)}[/dim]")
