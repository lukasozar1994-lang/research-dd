"""Bootstrap environment inspector."""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass, field


@dataclass
class PrerequisiteCheck:
    """Result of checking a single prerequisite."""

    name: str
    required: bool
    found: bool
    version: str | None = None
    path: str | None = None
    remediation: str = ""


@dataclass
class BootstrapReport:
    """Full bootstrap inspection report."""

    checks: list[PrerequisiteCheck] = field(default_factory=list)

    @property
    def all_required_met(self) -> bool:
        return all(c.found for c in self.checks if c.required)

    @property
    def missing_required(self) -> list[PrerequisiteCheck]:
        return [c for c in self.checks if c.required and not c.found]

    @property
    def missing_optional(self) -> list[PrerequisiteCheck]:
        return [c for c in self.checks if not c.required and not c.found]


def _check_command(name: str, args: list[str] | None = None) -> tuple[bool, str | None, str | None]:
    """Check if a command exists and optionally get its version."""
    path = shutil.which(name)
    if path is None:
        return False, None, None
    if args is None:
        return True, None, path
    try:
        result = subprocess.run(
            [name] + args,
            capture_output=True,
            text=True,
            timeout=10,
        )
        version = result.stdout.strip().split("\n")[0] if result.stdout else None
        return True, version, path
    except (subprocess.TimeoutExpired, OSError):
        return True, None, path


def inspect_environment() -> BootstrapReport:
    """Inspect the local environment for required prerequisites."""
    report = BootstrapReport()

    # Python
    found, ver, path = _check_command("python3", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="python3",
        required=True,
        found=found,
        version=ver,
        path=path,
        remediation="Install Python 3.12+: sudo apt install python3" if not found else "",
    ))

    # uv
    found, ver, path = _check_command("uv", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="uv",
        required=False,
        found=found,
        version=ver,
        path=path,
        remediation="Install uv: curl -LsSf https://astral.sh/uv/install.sh | sh" if not found else "",
    ))

    # Node.js
    found, ver, path = _check_command("node", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="node",
        required=True,
        found=found,
        version=ver,
        path=path,
        remediation="Install Node.js 18+: sudo apt install nodejs" if not found else "",
    ))

    # npm
    found, ver, path = _check_command("npm", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="npm",
        required=True,
        found=found,
        version=ver,
        path=path,
        remediation="Install npm: sudo apt install npm" if not found else "",
    ))

    # npx
    found, _, path = _check_command("npx", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="npx",
        required=True,
        found=found,
        path=path,
        remediation="npx is bundled with npm. Install npm first." if not found else "",
    ))

    # Git
    found, ver, path = _check_command("git", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="git",
        required=True,
        found=found,
        version=ver,
        path=path,
        remediation="Install git: sudo apt install git" if not found else "",
    ))

    # ripgrep
    found, ver, path = _check_command("rg", ["--version"])
    report.checks.append(PrerequisiteCheck(
        name="ripgrep",
        required=False,
        found=found,
        version=ver,
        path=path,
        remediation="Install ripgrep: sudo apt install ripgrep" if not found else "",
    ))

    return report
