"""Update engine — safe workspace update logic."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from research_driven_setup import __version__
from research_driven_setup.core.conflict_policy import ConflictAction, check_conflict
from research_driven_setup.core.manifest import FrameworkManifest, load_manifest
from research_driven_setup.core.renderer import render_workspace
from research_driven_setup.core.workspace_state import detect_workspace_state


@dataclass
class UpdateAction:
    """A planned update action."""

    path: str
    action: str  # "update" | "skip" | "conflict" | "new"
    reason: str


@dataclass
class UpdatePlan:
    """A plan for updating a workspace."""

    current_version: str | None
    target_version: str
    actions: list[UpdateAction] = field(default_factory=list)

    @property
    def has_conflicts(self) -> bool:
        return any(a.action == "conflict" for a in self.actions)

    @property
    def changes_count(self) -> int:
        return sum(1 for a in self.actions if a.action in ("update", "new"))


def plan_update(workspace: Path) -> UpdatePlan:
    """Generate an update plan by comparing installed vs current state."""
    state = detect_workspace_state(workspace)
    manifest = load_manifest()
    plan = UpdatePlan(
        current_version=state.installed_version,
        target_version=__version__,
    )

    if state.installed_version == __version__:
        return plan

    for mf in manifest.managed_files:
        target_path = workspace / mf.relative_path
        if not target_path.exists():
            plan.actions.append(UpdateAction(
                path=mf.relative_path,
                action="new",
                reason="file does not exist in workspace",
            ))
        elif mf.overwrite_policy == "overwrite":
            plan.actions.append(UpdateAction(
                path=mf.relative_path,
                action="update",
                reason="managed file, will overwrite",
            ))
        elif mf.overwrite_policy == "skip":
            plan.actions.append(UpdateAction(
                path=mf.relative_path,
                action="skip",
                reason="file exists, policy=skip",
            ))
        elif mf.overwrite_policy == "block":
            plan.actions.append(UpdateAction(
                path=mf.relative_path,
                action="conflict",
                reason="user-owned file modified externally",
            ))

    return plan


def apply_update(workspace: Path, force: bool = False) -> list[UpdateAction]:
    """Apply an update to the workspace."""
    manifest = load_manifest()
    render_workspace(manifest, workspace, force=force)
    plan = plan_update(workspace)
    return plan.actions
