"""Main CLI entrypoint for research-driven-setup."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.panel import Panel

from research_driven_setup import __version__

console = Console()

app = typer.Typer(
    name="research-driven-setup",
    help="Framework installer for research-driven development in VS Code with GitHub Copilot Chat.",
    no_args_is_help=False,
    invoke_without_command=True,
    pretty_exceptions_enable=False,
)


def _show_banner() -> None:
    """Display the branded ASCII-art banner."""
    from importlib.resources import files

    banner_path = files("research_driven_setup") / "resources" / "ascii" / "banner.txt"
    try:
        banner_text = banner_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        banner_text = "Research-Driven Setup"
    console.print(
        Panel(
            f"[bold cyan]{banner_text}[/bold cyan]\n[dim]v{__version__}[/dim]",
            border_style="bright_blue",
            padding=(1, 2),
        )
    )


@app.callback()
def main(
    ctx: typer.Context,
    version: bool = typer.Option(False, "--version", "-v", help="Show version and exit."),
) -> None:
    """Research-Driven Setup — workspace installer for VS Code + Copilot workflows."""
    if version:
        console.print(f"research-driven-setup {__version__}")
        raise typer.Exit()
    if ctx.invoked_subcommand is None:
        _show_banner()
        from research_driven_setup.commands.install import install

        ctx.invoke(install)


# --- Register subcommands ---
from research_driven_setup.commands.install import install  # noqa: E402
from research_driven_setup.commands.doctor import doctor  # noqa: E402
from research_driven_setup.commands.update import update  # noqa: E402
from research_driven_setup.commands.list_profiles import list_profiles  # noqa: E402
from research_driven_setup.commands.report import report  # noqa: E402

app.command(name="install", help="Run the interactive install flow.")(install)
app.command(name="doctor", help="Validate prerequisites, generated assets, and MCP readiness.")(doctor)
app.command(name="update", help="Update the workspace to a newer framework release.")(update)
app.command(name="list-profiles", help="List available installation profiles.")(list_profiles)
app.command(name="report", help="Show the last install or doctor report.")(report)
