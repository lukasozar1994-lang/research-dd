"""Conflict policy for managed files."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ConflictAction(Enum):
    WRITE = "write"
    SKIP = "skip"
    OVERWRITE = "overwrite"
    BLOCK = "block"


@dataclass
class ConflictResult:
    """Result of a conflict check."""

    path: str
    action: ConflictAction
    reason: str


def check_conflict(
    relative_path: str,
    target_root: Path,
    policy: str,
    force: bool = False,
) -> ConflictResult:
    """Decide what to do when a managed file already exists."""
    full_path = target_root / relative_path
    if not full_path.exists():
        return ConflictResult(path=relative_path, action=ConflictAction.WRITE, reason="file does not exist")
    if force:
        return ConflictResult(path=relative_path, action=ConflictAction.OVERWRITE, reason="--force flag set")
    if policy == "overwrite":
        return ConflictResult(path=relative_path, action=ConflictAction.OVERWRITE, reason="policy=overwrite")
    if policy == "block":
        return ConflictResult(path=relative_path, action=ConflictAction.BLOCK, reason="user-owned file, will not overwrite")
    return ConflictResult(path=relative_path, action=ConflictAction.SKIP, reason="file exists, skipping")
