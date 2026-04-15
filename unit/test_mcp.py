"""Tests for MCP configuration composition."""

import json
import pytest

from research_driven_setup.core.manifest import load_manifest
from research_driven_setup.core.mcp import compose_mcp_config, generate_mcp_onboarding_notes, write_mcp_config


def test_compose_mcp_config_all_servers():
    manifest = load_manifest()
    servers = ["github", "sequential-thinking", "filesystem", "open-websearch", "context7"]
    config = compose_mcp_config(manifest, servers)
    assert "servers" in config
    assert set(config["servers"].keys()) == set(servers)


def test_compose_mcp_config_subset():
    manifest = load_manifest()
    servers = ["filesystem", "sequential-thinking"]
    config = compose_mcp_config(manifest, servers)
    assert set(config["servers"].keys()) == {"filesystem", "sequential-thinking"}


def test_github_server_config():
    manifest = load_manifest()
    config = compose_mcp_config(manifest, ["github"])
    gh = config["servers"]["github"]
    assert gh["type"] == "http"
    assert gh["url"] == "https://api.githubcopilot.com/mcp/"
    assert "X-MCP-Readonly" in gh["headers"]


def test_context7_server_config():
    manifest = load_manifest()
    config = compose_mcp_config(manifest, ["context7"])
    ctx = config["servers"]["context7"]
    assert ctx["type"] == "stdio"
    assert "start-context7-mcp.sh" in ctx["args"][0]


def test_write_mcp_config(tmp_path):
    config = {"servers": {"test": {"command": "echo"}}}
    path = write_mcp_config(tmp_path, config)
    assert path.exists()
    data = json.loads(path.read_text())
    assert data["servers"]["test"]["command"] == "echo"


def test_onboarding_notes_for_missing_secret():
    manifest = load_manifest()
    servers = ["context7"]
    notes = generate_mcp_onboarding_notes(manifest, servers, secrets={})
    assert any("CONTEXT7_API_KEY" in n for n in notes)


def test_no_hardcoded_secrets_in_config():
    """SEC-002: Generated MCP config must not contain hardcoded secrets."""
    manifest = load_manifest()
    config = compose_mcp_config(manifest, ["context7"], secrets={"CONTEXT7_API_KEY": None})
    raw = json.dumps(config)
    # Should not have any actual API key values
    assert "your-api-key" not in raw.lower()
