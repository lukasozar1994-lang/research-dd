"""Profile registry and resolution."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from importlib.resources import files
from typing import Any


@dataclass
class Profile:
    """A named installation profile."""

    name: str
    display_name: str
    description: str
    includes_playwright: bool = False
    mcp_servers: list[str] = field(default_factory=list)
    managed_files: list[str] = field(default_factory=list)
    overlays: list[str] = field(default_factory=list)


_PROFILES_CACHE: dict[str, Profile] | None = None

ALIASES: dict[str, str] = {
    "default": "ubuntu-research",
    "ubuntu": "ubuntu-research",
    "playwright": "ubuntu-research-playwright",
}


def _load_profiles() -> dict[str, Profile]:
    global _PROFILES_CACHE
    if _PROFILES_CACHE is not None:
        return _PROFILES_CACHE
    profiles_dir = files("research_driven_setup") / "resources" / "manifest" / "profiles"
    result: dict[str, Profile] = {}
    for item in profiles_dir.iterdir():
        if not item.name.endswith(".json"):
            continue
        raw = json.loads(item.read_text(encoding="utf-8"))
        p = Profile(
            name=raw["name"],
            display_name=raw.get("display_name", raw["name"]),
            description=raw.get("description", ""),
            includes_playwright=raw.get("includes_playwright", False),
            mcp_servers=raw.get("mcp_servers", []),
            managed_files=raw.get("managed_files", []),
            overlays=raw.get("overlays", []),
        )
        result[p.name] = p
    _PROFILES_CACHE = result
    return result


def list_available_profiles() -> list[Profile]:
    """Return all available profiles."""
    return list(_load_profiles().values())


def resolve_profile(name: str) -> Profile:
    """Resolve a profile by name or alias."""
    canonical = ALIASES.get(name, name)
    profiles = _load_profiles()
    if canonical not in profiles:
        raise ValueError(f"Unknown profile: {name!r}. Available: {', '.join(profiles.keys())}")
    return profiles[canonical]


def get_default_profile() -> Profile:
    """Return the default profile."""
    return resolve_profile("ubuntu-research")
