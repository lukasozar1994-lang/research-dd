"""Tests for conflict policy."""

import pytest
from pathlib import Path

from research_driven_setup.core.conflict_policy import (
    ConflictAction,
    ConflictResult,
    check_conflict,
)


def test_write_when_file_does_not_exist(tmp_path):
    result = check_conflict("some/file.md", tmp_path, "skip")
    assert result.action == ConflictAction.WRITE
    assert "does not exist" in result.reason


def test_skip_when_file_exists(tmp_path):
    (tmp_path / "some").mkdir()
    (tmp_path / "some" / "file.md").write_text("existing")
    result = check_conflict("some/file.md", tmp_path, "skip")
    assert result.action == ConflictAction.SKIP


def test_overwrite_when_policy_overwrite(tmp_path):
    (tmp_path / "file.md").write_text("existing")
    result = check_conflict("file.md", tmp_path, "overwrite")
    assert result.action == ConflictAction.OVERWRITE


def test_block_when_policy_block(tmp_path):
    (tmp_path / "file.md").write_text("existing")
    result = check_conflict("file.md", tmp_path, "block")
    assert result.action == ConflictAction.BLOCK


def test_force_overrides_skip(tmp_path):
    (tmp_path / "file.md").write_text("existing")
    result = check_conflict("file.md", tmp_path, "skip", force=True)
    assert result.action == ConflictAction.OVERWRITE
