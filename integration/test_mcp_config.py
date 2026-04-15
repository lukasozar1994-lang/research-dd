"""Integration tests for MCP config generation."""

import json
import pytest

from research_driven_setup.core.manifest import load_manifest
from research_driven_setup.core.mcp import compose_mcp_config, write_mcp_config


def test_generated_mcp_matches_profile(tmp_path):
    """AC-003: .vscode/mcp.json is generated from manifest data."""
    manifest = load_manifest()
    servers = ["github", "sequential-thinking", "filesystem", "open-websearch", "context7"]
    config = compose_mcp_config(manifest, servers)
    path = write_mcp_config(tmp_path, config)

    data = json.loads(path.read_text())
    assert "servers" in data
    assert set(data["servers"].keys()) == set(servers)

    # Validate structure
    gh = data["servers"]["github"]
    assert gh["type"] == "http"
    assert "X-MCP-Toolsets" in gh["headers"]

    fs = data["servers"]["filesystem"]
    assert fs["command"] == "npx"

    ctx = data["servers"]["context7"]
    assert "start-context7-mcp.sh" in json.dumps(ctx)


def test_mcp_json_valid_syntax(tmp_path):
    """Generated mcp.json must be valid JSON."""
    manifest = load_manifest()
    config = compose_mcp_config(manifest, ["github", "filesystem"])
    path = write_mcp_config(tmp_path, config)
    # Should not raise
    data = json.loads(path.read_text())
    assert isinstance(data, dict)


def test_no_secrets_in_mcp_json(tmp_path):
    """SEC-001: No secret values in generated MCP config."""
    manifest = load_manifest()
    config = compose_mcp_config(manifest, ["context7"], secrets={"CONTEXT7_API_KEY": "test-key-123"})
    path = write_mcp_config(tmp_path, config)
    content = path.read_text()
    # The actual API key should not appear in the config
    # Context7 uses a startup script that reads from .env
    assert "test-key-123" not in content
