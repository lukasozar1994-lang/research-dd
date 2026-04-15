"""Secret prompting and onboarding guidance."""

from __future__ import annotations

from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

console = Console()

ENV_EXAMPLE_CONTENT = """\
# Research-Driven Setup — Environment Variables
# Copy this file to .env and fill in the values.
# WARNING: Never commit .env to version control.

# Context7 API key (optional — needed for context7 MCP server)
# Get your key at: https://context7.com
# CONTEXT7_API_KEY=your-api-key-here
"""


def prompt_for_secrets(workspace: Path) -> dict[str, str | None]:
    """Prompt the user for optional secrets. Returns a dict of secret_name → value|None."""
    secrets: dict[str, str | None] = {}

    console.print()
    console.print(Panel(
        "[bold]Optional Secret Setup[/bold]\n\n"
        "Some MCP servers require API keys or secrets.\n"
        "You can set them now or later in a [bold].env[/bold] file.",
        border_style="yellow",
    ))

    # Context7 API key
    console.print()
    setup_context7 = typer.confirm(
        "Do you want to configure the Context7 API key now?",
        default=False,
    )
    if setup_context7:
        api_key = typer.prompt(
            "Enter your CONTEXT7_API_KEY",
            hide_input=True,
            default="",
        )
        if api_key.strip():
            secrets["CONTEXT7_API_KEY"] = api_key.strip()
            # Write to .env (local only, not committed)
            _write_env_file(workspace, "CONTEXT7_API_KEY", api_key.strip())
            console.print("[green]✓[/green] CONTEXT7_API_KEY saved to .env")
        else:
            secrets["CONTEXT7_API_KEY"] = None
            console.print("[yellow]⚠[/yellow] Skipped — add CONTEXT7_API_KEY to .env later.")
    else:
        secrets["CONTEXT7_API_KEY"] = None
        console.print("[dim]Skipped Context7 setup. Add CONTEXT7_API_KEY to .env later.[/dim]")

    # Write .env.example
    _write_env_example(workspace)

    return secrets


def _write_env_file(workspace: Path, key: str, value: str) -> None:
    """Append a secret to the .env file (local, not committed)."""
    env_file = workspace / ".env"
    lines: list[str] = []
    if env_file.exists():
        lines = env_file.read_text(encoding="utf-8").splitlines()
    # Remove existing entry for this key
    lines = [line for line in lines if not line.strip().startswith(f"{key}=")]
    lines.append(f"{key}={value}")
    env_file.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_env_example(workspace: Path) -> None:
    """Write .env.example for guidance."""
    example_path = workspace / ".env.example"
    if not example_path.exists():
        example_path.write_text(ENV_EXAMPLE_CONTENT, encoding="utf-8")


def prompt_github_mcp_setup() -> bool:
    """Ask if the user wants to enable GitHub MCP and provide guidance."""
    console.print()
    console.print(Panel(
        "[bold]GitHub MCP Server[/bold]\n\n"
        "The GitHub MCP server provides read access to repos, issues, PRs, and actions.\n"
        "It requires OAuth authentication through VS Code.",
        border_style="blue",
    ))

    enable = typer.confirm(
        "Enable GitHub MCP server in this workspace?",
        default=True,
    )
    if enable:
        console.print()
        console.print("[green]✓[/green] GitHub MCP enabled in configuration.")
        console.print()
        console.print(Panel(
            "[bold yellow]Manual Step Required[/bold yellow]\n\n"
            "After installing, open VS Code in this workspace and:\n"
            "1. Open the Command Palette (Ctrl+Shift+P)\n"
            "2. Search for 'MCP: List Servers'\n"
            "3. Find the 'github' server and click 'Start'\n"
            "4. Complete the OAuth authentication when prompted\n"
            "5. Trust the server when asked",
            border_style="yellow",
        ))
    else:
        console.print("[dim]GitHub MCP disabled. You can enable it later in .vscode/mcp.json.[/dim]")
    return enable
