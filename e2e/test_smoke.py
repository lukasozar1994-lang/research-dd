"""End-to-end smoke tests for the CLI."""

from pathlib import Path

from typer.testing import CliRunner

from research_driven_setup.cli import app

runner = CliRunner()


def test_e2e_install_non_interactive(tmp_path):
    """FLOW-001: Full install flow in non-interactive mode."""
    result = runner.invoke(app, [
        "install",
        "--workspace", str(tmp_path),
        "--non-interactive",
    ])
    assert result.exit_code == 0
    assert "Installation Complete" in result.output

    # Verify generated files
    assert (tmp_path / ".github" / "agents" / "deep-research.agent.md").exists()
    assert (tmp_path / ".github" / "prompts" / "plan-project.prompt.md").exists()
    assert (tmp_path / ".github" / "skills" / "open-websearch" / "SKILL.md").exists()
    assert (tmp_path / ".vscode" / "mcp.json").exists()
    assert (tmp_path / ".research-driven" / "install.json").exists()
    assert (tmp_path / ".research-driven" / "install-report.md").exists()


def test_e2e_help_discovery():
    """FLOW-002: Help provides complete discovery."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    commands = ["install", "doctor", "update", "list-profiles", "report"]
    for cmd in commands:
        assert cmd in result.output


def test_e2e_doctor_after_install(tmp_path):
    """Install then doctor should pass."""
    runner.invoke(app, ["install", "--workspace", str(tmp_path), "--non-interactive"])
    result = runner.invoke(app, ["doctor", "--workspace", str(tmp_path)])
    assert result.exit_code == 0
    assert "install marker" in result.output


def test_e2e_rerun_safe(tmp_path):
    """FLOW-006: Re-running install handles managed files safely."""
    runner.invoke(app, ["install", "--workspace", str(tmp_path), "--non-interactive"])
    # Modify an agent file
    agent_file = tmp_path / ".github" / "agents" / "deep-research.agent.md"
    agent_file.write_text("# My Custom Agent\n")

    # Re-run
    result = runner.invoke(app, ["install", "--workspace", str(tmp_path), "--non-interactive"])
    assert result.exit_code == 0

    # Custom content should be preserved (skip policy)
    assert agent_file.read_text() == "# My Custom Agent\n"


def test_e2e_version():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "0.1.1" in result.output
