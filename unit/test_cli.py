"""Tests for CLI command routing and help output."""

from typer.testing import CliRunner

from research_driven_setup.cli import app

runner = CliRunner()


def test_version_flag():
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert "0.1.1" in result.output


def test_help_output():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "install" in result.output
    assert "doctor" in result.output
    assert "update" in result.output
    assert "list-profiles" in result.output
    assert "report" in result.output


def test_install_help():
    result = runner.invoke(app, ["install", "--help"])
    assert result.exit_code == 0
    assert "--workspace" in result.output
    assert "--profile" in result.output
    assert "--force" in result.output


def test_doctor_help():
    result = runner.invoke(app, ["doctor", "--help"])
    assert result.exit_code == 0
    assert "--workspace" in result.output


def test_update_help():
    result = runner.invoke(app, ["update", "--help"])
    assert result.exit_code == 0
    assert "--force" in result.output
    assert "--dry-run" in result.output


def test_list_profiles_executes():
    result = runner.invoke(app, ["list-profiles"])
    assert result.exit_code == 0
    assert "ubuntu-resear" in result.output  # Rich may truncate in narrow terminals


def test_report_no_report_found(tmp_path):
    result = runner.invoke(app, ["report", "--workspace", str(tmp_path)])
    assert result.exit_code == 1
    assert "No install report found" in result.output
