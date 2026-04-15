"""Integration tests for doctor command."""

import json
import pytest

from research_driven_setup.core.doctor import run_doctor
from research_driven_setup.core.manifest import load_manifest
from research_driven_setup.core.mcp import compose_mcp_config, write_mcp_config
from research_driven_setup.core.renderer import render_workspace


def test_doctor_on_fresh_workspace(tmp_path):
    report = run_doctor(tmp_path)
    # Should have warnings about missing install marker and assets
    assert any(c.name == "install marker" and c.status == "warn" for c in report.checks)
    assert any(c.name == "mcp.json" and c.status == "fail" for c in report.checks)


def test_doctor_on_installed_workspace(tmp_path):
    manifest = load_manifest()
    render_workspace(manifest, tmp_path)

    # Generate MCP config
    config = compose_mcp_config(manifest, ["github", "sequential-thinking", "filesystem", "open-websearch", "context7"])
    write_mcp_config(tmp_path, config)

    # Create package.json
    (tmp_path / "package.json").write_text('{"name":"test","private":true}')

    report = run_doctor(tmp_path)
    assert any(c.name == "install marker" and c.status == "pass" for c in report.checks)
    assert any(c.name == "mcp.json" and c.status == "pass" for c in report.checks)


def test_doctor_detects_missing_prerequisites(tmp_path):
    report = run_doctor(tmp_path)
    env_checks = [c for c in report.checks if c.category == "environment"]
    assert len(env_checks) > 0
    # Python should pass since tests are running
    py = [c for c in env_checks if c.name == "python3"][0]
    assert py.status == "pass"
