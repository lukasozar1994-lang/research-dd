"""Manifest loader and validator."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from importlib.resources import files
from pathlib import Path
from typing import Any


@dataclass
class ManagedFile:
    """A file managed by the framework."""

    relative_path: str
    source: str  # "template" | "generated" | "skill_catalog"
    overwrite_policy: str = "skip"  # "overwrite" | "skip" | "merge" | "block"
    description: str = ""


@dataclass
class McpServerDescriptor:
    """An MCP server entry."""

    name: str
    config: dict[str, Any]
    optional: bool = False
    requires_secret: str | None = None
    trust_note: str | None = None


@dataclass
class FrameworkManifest:
    """Top-level framework manifest."""

    version: str
    profiles: list[str]
    default_profile: str
    prerequisites: list[dict[str, str]]
    managed_files: list[ManagedFile]
    mcp_servers: list[McpServerDescriptor]
    compatibility_aliases: dict[str, str]
    metadata: dict[str, Any] = field(default_factory=dict)


def load_manifest() -> FrameworkManifest:
    """Load and validate the embedded framework manifest."""
    manifest_path = files("research_driven_setup") / "resources" / "manifest" / "framework.manifest.json"
    raw = json.loads(manifest_path.read_text(encoding="utf-8"))
    managed = [
        ManagedFile(
            relative_path=f["relative_path"],
            source=f["source"],
            overwrite_policy=f.get("overwrite_policy", "skip"),
            description=f.get("description", ""),
        )
        for f in raw.get("managed_files", [])
    ]
    mcp = [
        McpServerDescriptor(
            name=s["name"],
            config=s["config"],
            optional=s.get("optional", False),
            requires_secret=s.get("requires_secret"),
            trust_note=s.get("trust_note"),
        )
        for s in raw.get("mcp_servers", [])
    ]
    aliases = raw.get("compatibility_aliases", {})
    return FrameworkManifest(
        version=raw["version"],
        profiles=raw.get("profiles", []),
        default_profile=raw.get("default_profile", "ubuntu-research"),
        prerequisites=raw.get("prerequisites", []),
        managed_files=managed,
        mcp_servers=mcp,
        compatibility_aliases=aliases,
        metadata=raw.get("metadata", {}),
    )
