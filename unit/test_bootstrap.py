"""Tests for bootstrap environment inspection."""

from research_driven_setup.core.bootstrap import BootstrapReport, inspect_environment


def test_inspect_environment_returns_report():
    report = inspect_environment()
    assert isinstance(report, BootstrapReport)
    assert len(report.checks) > 0


def test_required_checks_present():
    report = inspect_environment()
    names = [c.name for c in report.checks]
    assert "python3" in names
    assert "node" in names
    assert "npm" in names
    assert "git" in names


def test_python_check_passes():
    """We know Python is available since we're running tests."""
    report = inspect_environment()
    py = [c for c in report.checks if c.name == "python3"][0]
    assert py.found is True
    assert py.version is not None
    assert "Python" in py.version


def test_missing_required_report():
    report = BootstrapReport()
    from research_driven_setup.core.bootstrap import PrerequisiteCheck
    report.checks.append(PrerequisiteCheck(name="fake-tool", required=True, found=False))
    assert not report.all_required_met
    assert len(report.missing_required) == 1
