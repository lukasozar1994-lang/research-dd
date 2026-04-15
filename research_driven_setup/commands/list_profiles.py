"""List profiles command."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from research_driven_setup.core.profiles import list_available_profiles

console = Console()


def list_profiles() -> None:
    """List available installation profiles."""
    profiles = list_available_profiles()

    table = Table(title="Available Profiles", show_header=True)
    table.add_column("Name", style="bold")
    table.add_column("Display Name")
    table.add_column("Description")
    table.add_column("Playwright")
    table.add_column("MCP Servers")

    for p in profiles:
        table.add_row(
            p.name,
            p.display_name,
            p.description,
            "✓" if p.includes_playwright else "-",
            ", ".join(p.mcp_servers),
        )

    console.print()
    console.print(table)
    console.print()
