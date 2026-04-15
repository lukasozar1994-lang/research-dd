"""Workspace renderer — copies/generates files into target workspace."""

from __future__ import annotations

import json
import shutil
from importlib.resources import files
from pathlib import Path
from typing import Any

from research_driven_setup.core.conflict_policy import ConflictAction, ConflictResult, check_conflict
from research_driven_setup.core.manifest import FrameworkManifest, ManagedFile


def _template_base() -> Path:
    """Return the Path to the embedded template base directory."""
    ref = files("research_driven_setup") / "resources" / "templates" / "base"
    # Traversable → Path for filesystem access
    return Path(str(ref))


def render_workspace(
    manifest: FrameworkManifest,
    workspace: Path,
    force: bool = False,
) -> list[ConflictResult]:
    """Render managed files into the target workspace.

    Returns a list of ConflictResult items describing what happened to each file.
    """
    results: list[ConflictResult] = []
    template_root = _template_base()

    for mf in manifest.managed_files:
        if mf.source == "template":
            result = _render_template_file(mf, template_root, workspace, force)
        elif mf.source == "generated":
            # Generated files are handled by their respective modules
            result = ConflictResult(path=mf.relative_path, action=ConflictAction.SKIP, reason="generated elsewhere")
        elif mf.source == "skill_catalog":
            result = _render_skill_stub(mf, template_root, workspace, force)
        else:
            result = ConflictResult(path=mf.relative_path, action=ConflictAction.SKIP, reason=f"unknown source: {mf.source}")
        results.append(result)

    # Write install marker
    _write_install_marker(manifest, workspace, results)

    return results


def _render_template_file(
    mf: ManagedFile,
    template_root: Path,
    workspace: Path,
    force: bool,
) -> ConflictResult:
    """Copy a template file to the workspace."""
    conflict = check_conflict(mf.relative_path, workspace, mf.overwrite_policy, force)
    if conflict.action in (ConflictAction.SKIP, ConflictAction.BLOCK):
        return conflict

    src = template_root / mf.relative_path
    dst = workspace / mf.relative_path
    dst.parent.mkdir(parents=True, exist_ok=True)

    if src.is_file():
        shutil.copy2(src, dst)
    elif src.is_dir():
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    else:
        return ConflictResult(path=mf.relative_path, action=ConflictAction.SKIP, reason="template source not found")

    return conflict


def _render_skill_stub(
    mf: ManagedFile,
    template_root: Path,
    workspace: Path,
    force: bool,
) -> ConflictResult:
    """Render a skill directory from the template catalog."""
    conflict = check_conflict(mf.relative_path, workspace, mf.overwrite_policy, force)
    if conflict.action in (ConflictAction.SKIP, ConflictAction.BLOCK):
        return conflict

    src_dir = template_root / mf.relative_path
    dst_dir = workspace / mf.relative_path

    if src_dir.is_dir():
        dst_dir.mkdir(parents=True, exist_ok=True)
        # Copy all files from the skill template
        for item in src_dir.rglob("*"):
            if item.is_file():
                rel = item.relative_to(src_dir)
                target = dst_dir / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target)
    else:
        # Create minimal skill stub
        dst_dir.mkdir(parents=True, exist_ok=True)
        skill_md = dst_dir / "SKILL.md"
        if not skill_md.exists() or force:
            skill_md.write_text(f"# {mf.description}\n\nSkill managed by research-driven-setup.\n", encoding="utf-8")

    return conflict


def _write_install_marker(
    manifest: FrameworkManifest,
    workspace: Path,
    results: list[ConflictResult],
) -> None:
    """Write the .research-driven/install.json marker file."""
    marker_dir = workspace / ".research-driven"
    marker_dir.mkdir(parents=True, exist_ok=True)
    marker = {
        "version": manifest.version,
        "profile": manifest.default_profile,
        "files_written": [r.path for r in results if r.action in (ConflictAction.WRITE, ConflictAction.OVERWRITE)],
        "files_skipped": [r.path for r in results if r.action == ConflictAction.SKIP],
        "files_blocked": [r.path for r in results if r.action == ConflictAction.BLOCK],
    }
    (marker_dir / "install.json").write_text(json.dumps(marker, indent=2) + "\n", encoding="utf-8")
