"""Tests for manifest loading and validation."""

import pytest

from research_driven_setup.core.manifest import FrameworkManifest, load_manifest


def test_load_manifest_returns_framework_manifest():
    manifest = load_manifest()
    assert isinstance(manifest, FrameworkManifest)
    assert manifest.version == "0.1.1"


def test_manifest_has_profiles():
    manifest = load_manifest()
    assert "ubuntu-research" in manifest.profiles
    assert "ubuntu-research-playwright" in manifest.profiles


def test_manifest_has_default_profile():
    manifest = load_manifest()
    assert manifest.default_profile == "ubuntu-research"


def test_manifest_has_prerequisites():
    manifest = load_manifest()
    names = [p["name"] for p in manifest.prerequisites]
    assert "python3" in names
    assert "node" in names
    assert "git" in names


def test_manifest_has_managed_files():
    manifest = load_manifest()
    assert len(manifest.managed_files) > 0
    paths = [f.relative_path for f in manifest.managed_files]
    assert ".github/agents/deep-research.agent.md" in paths
    assert ".vscode/mcp.json" in paths


def test_manifest_has_mcp_servers():
    manifest = load_manifest()
    names = [s.name for s in manifest.mcp_servers]
    assert "github" in names
    assert "sequential-thinking" in names
    assert "filesystem" in names
    assert "open-websearch" in names
    assert "context7" in names


def test_manifest_has_compatibility_aliases():
    manifest = load_manifest()
    assert "deep_reserch.agent.md" in manifest.compatibility_aliases
    assert manifest.compatibility_aliases["deep_reserch.agent.md"] == "deep-research.agent.md"


def test_manifest_mcp_context7_requires_secret():
    manifest = load_manifest()
    ctx7 = [s for s in manifest.mcp_servers if s.name == "context7"][0]
    assert ctx7.requires_secret == "CONTEXT7_API_KEY"
    assert ctx7.optional is True


def test_manifest_no_secrets_in_config():
    """SEC-001: No hardcoded secrets in framework assets."""
    manifest = load_manifest()
    import json
    raw = json.dumps([s.config for s in manifest.mcp_servers])
    assert "api_key" not in raw.lower() or "CONTEXT7_API_KEY" not in raw
