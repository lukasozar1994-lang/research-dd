"""Workspace state detection."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class WorkspaceState:
    """Describes the current state of a target workspace."""

    path: Path
    has_github_dir: bool = False
    has_vscode_dir: bool = False
    has_mcp_json: bool = False
    has_package_json: bool = False
    has_research_driven_marker: bool = False
    existing_agents: list[str] = field(default_factory=list)
    existing_prompts: list[str] = field(default_factory=list)
    existing_skills: list[str] = field(default_factory=list)
    installed_version: str | None = None

    @property
    def is_fresh(self) -> bool:
        return not self.has_github_dir and not self.has_vscode_dir

    @property
    def is_installed(self) -> bool:
        return self.has_research_driven_marker


def detect_workspace_state(workspace: Path) -> WorkspaceState:
    """Detect the current state of a target workspace."""
    state = WorkspaceState(path=workspace)
    github_dir = workspace / ".github"
    vscode_dir = workspace / ".vscode"
    state.has_github_dir = github_dir.is_dir()
    state.has_vscode_dir = vscode_dir.is_dir()
    state.has_mcp_json = (vscode_dir / "mcp.json").is_file()
    state.has_package_json = (workspace / "package.json").is_file()
    marker = workspace / ".research-driven" / "install.json"
    state.has_research_driven_marker = marker.is_file()
    if state.has_research_driven_marker:
        try:
            data = json.loads(marker.read_text(encoding="utf-8"))
            state.installed_version = data.get("version")
        except (json.JSONDecodeError, OSError):
            pass
    if state.has_github_dir:
        agents_dir = github_dir / "agents"
        if agents_dir.is_dir():
            state.existing_agents = [f.name for f in agents_dir.iterdir() if f.suffix == ".md"]
        prompts_dir = github_dir / "prompts"
        if prompts_dir.is_dir():
            state.existing_prompts = [f.name for f in prompts_dir.iterdir() if f.suffix == ".md"]
        skills_dir = github_dir / "skills"
        if skills_dir.is_dir():
            state.existing_skills = [d.name for d in skills_dir.iterdir() if d.is_dir()]
    return state
