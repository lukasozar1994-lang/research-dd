"""MCP configuration composer."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from research_driven_setup.core.manifest import FrameworkManifest, McpServerDescriptor


def compose_mcp_config(
    manifest: FrameworkManifest,
    profile_servers: list[str],
    secrets: dict[str, str | None] | None = None,
) -> dict[str, Any]:
    """Build a .vscode/mcp.json structure from manifest MCP descriptors."""
    secrets = secrets or {}
    servers: dict[str, Any] = {}

    for descriptor in manifest.mcp_servers:
        if descriptor.name not in profile_servers:
            continue
        config = dict(descriptor.config)
        # Substitute secret placeholders
        if descriptor.requires_secret and descriptor.requires_secret in secrets:
            val = secrets[descriptor.requires_secret]
            if val:
                _substitute_secret(config, descriptor.requires_secret, val)
        servers[descriptor.name] = config

    return {"servers": servers}


def _substitute_secret(config: dict[str, Any], key: str, value: str) -> None:
    """Recursively substitute a secret placeholder in config."""
    for k, v in config.items():
        if isinstance(v, str) and f"${{{key}}}" in v:
            config[k] = v.replace(f"${{{key}}}", value)
        elif isinstance(v, dict):
            _substitute_secret(v, key, value)


def write_mcp_config(workspace: Path, config: dict[str, Any]) -> Path:
    """Write the .vscode/mcp.json file."""
    vscode_dir = workspace / ".vscode"
    vscode_dir.mkdir(parents=True, exist_ok=True)
    mcp_path = vscode_dir / "mcp.json"
    mcp_path.write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return mcp_path


def generate_mcp_onboarding_notes(
    manifest: FrameworkManifest,
    profile_servers: list[str],
    secrets: dict[str, str | None] | None = None,
) -> list[str]:
    """Generate onboarding notes for MCP servers that need manual setup."""
    secrets = secrets or {}
    notes: list[str] = []
    for descriptor in manifest.mcp_servers:
        if descriptor.name not in profile_servers:
            continue
        if descriptor.trust_note:
            notes.append(f"[{descriptor.name}] {descriptor.trust_note}")
        if descriptor.requires_secret:
            secret_val = secrets.get(descriptor.requires_secret)
            if not secret_val:
                notes.append(
                    f"[{descriptor.name}] Secret '{descriptor.requires_secret}' is not set. "
                    f"Add it to your .env file or set it in your environment."
                )
    return notes
