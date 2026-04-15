"""Application context shared across commands."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class AppContext:
    """Runtime context for a single installer session."""

    workspace: Path = field(default_factory=lambda: Path.cwd())
    profile_name: str = "ubuntu-research"
    verbose: bool = False
    session_log: list[dict[str, Any]] = field(default_factory=list)

    @property
    def github_dir(self) -> Path:
        return self.workspace / ".github"

    @property
    def vscode_dir(self) -> Path:
        return self.workspace / ".vscode"

    @property
    def diagnostics_dir(self) -> Path:
        return self.workspace / ".research-driven"

    def log(self, action: str, detail: str, status: str = "ok") -> None:
        self.session_log.append({"action": action, "detail": detail, "status": status})
