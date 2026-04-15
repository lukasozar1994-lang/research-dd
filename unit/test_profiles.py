"""Tests for profile registry."""

import pytest

from research_driven_setup.core.profiles import (
    get_default_profile,
    list_available_profiles,
    resolve_profile,
    Profile,
)


def test_list_available_profiles():
    profiles = list_available_profiles()
    assert len(profiles) >= 2
    names = [p.name for p in profiles]
    assert "ubuntu-research" in names
    assert "ubuntu-research-playwright" in names


def test_resolve_profile_by_name():
    profile = resolve_profile("ubuntu-research")
    assert isinstance(profile, Profile)
    assert profile.name == "ubuntu-research"


def test_resolve_profile_by_alias():
    profile = resolve_profile("default")
    assert profile.name == "ubuntu-research"

    profile = resolve_profile("playwright")
    assert profile.name == "ubuntu-research-playwright"


def test_resolve_unknown_profile_raises():
    with pytest.raises(ValueError, match="Unknown profile"):
        resolve_profile("nonexistent-profile")


def test_get_default_profile():
    profile = get_default_profile()
    assert profile.name == "ubuntu-research"
    assert "github" in profile.mcp_servers
    assert "sequential-thinking" in profile.mcp_servers


def test_profile_mcp_servers():
    profile = resolve_profile("ubuntu-research")
    expected = {"github", "sequential-thinking", "filesystem", "open-websearch", "context7"}
    assert set(profile.mcp_servers) == expected


def test_playwright_profile_flag():
    basic = resolve_profile("ubuntu-research")
    assert basic.includes_playwright is False

    pw = resolve_profile("ubuntu-research-playwright")
    assert pw.includes_playwright is True
