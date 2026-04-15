"""Doctor engine — validate workspace health."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from research_driven_setup.core.bootstrap import BootstrapReport, inspect_environment
from research_driven_setup.core.manifest import FrameworkManifest, load_manifest
from research_driven_setup.core.workspace_state import WorkspaceState, detect_workspace_state


@dataclass
class DoctorCheck:
    """A single diagnostic check."""

    category: str
    name: str
    status: str  # "pass" | "warn" | "fail"
    detail: str = ""
    remediation: str = ""


@dataclass
class DoctorReport:
    """Full doctor report."""

    checks: list[DoctorCheck] = field(default_factory=list)

    @property
    def passed(self) -> bool:
        return all(c.status != "fail" for c in self.checks)

    @property
    def failures(self) -> list[DoctorCheck]:
        return [c for c in self.checks if c.status == "fail"]

    @property
    def warnings(self) -> list[DoctorCheck]:
        return [c for c in self.checks if c.status == "warn"]


def run_doctor(workspace: Path) -> DoctorReport:
    """Run all doctor diagnostics."""
    report = DoctorReport()

    # 1. Environment checks
    bootstrap = inspect_environment()
    for check in bootstrap.checks:
        report.checks.append(DoctorCheck(
            category="environment",
            name=check.name,
            status="pass" if check.found else ("fail" if check.required else "warn"),
            detail=check.version or ("found" if check.found else "not found"),
            remediation=check.remediation,
        ))

    # 2. Workspace state
    state = detect_workspace_state(workspace)

    if not state.has_research_driven_marker:
        report.checks.append(DoctorCheck(
            category="workspace",
            name="install marker",
            status="warn",
            detail="No .research-driven/install.json found",
            remediation="Run 'research-driven-setup install' to set up this workspace.",
        ))
    else:
        report.checks.append(DoctorCheck(
            category="workspace",
            name="install marker",
            status="pass",
            detail=f"Installed version: {state.installed_version}",
        ))

    # 3. MCP config
    if state.has_mcp_json:
        mcp_path = workspace / ".vscode" / "mcp.json"
        try:
            mcp_data = json.loads(mcp_path.read_text(encoding="utf-8"))
            servers = mcp_data.get("servers", {})
            report.checks.append(DoctorCheck(
                category="mcp",
                name="mcp.json",
                status="pass",
                detail=f"{len(servers)} server(s) configured: {', '.join(servers.keys())}",
            ))
            # Check for required servers
            for required in ["sequential-thinking", "filesystem", "open-websearch"]:
                if required in servers:
                    report.checks.append(DoctorCheck(
                        category="mcp",
                        name=f"server:{required}",
                        status="pass",
                        detail="configured",
                    ))
                else:
                    report.checks.append(DoctorCheck(
                        category="mcp",
                        name=f"server:{required}",
                        status="fail",
                        detail="not configured",
                        remediation=f"Add '{required}' server to .vscode/mcp.json",
                    ))
            # Context7 check
            if "context7" in servers:
                env_file = workspace / ".env"
                has_key = False
                if env_file.exists():
                    content = env_file.read_text(encoding="utf-8")
                    has_key = "CONTEXT7_API_KEY=" in content and not content.strip().endswith("CONTEXT7_API_KEY=")
                report.checks.append(DoctorCheck(
                    category="mcp",
                    name="server:context7",
                    status="pass" if has_key else "warn",
                    detail="configured" + (" with API key" if has_key else " — API key not set"),
                    remediation="" if has_key else "Add CONTEXT7_API_KEY to .env file",
                ))
        except (json.JSONDecodeError, OSError) as e:
            report.checks.append(DoctorCheck(
                category="mcp",
                name="mcp.json",
                status="fail",
                detail=f"Parse error: {e}",
                remediation="Fix or regenerate .vscode/mcp.json",
            ))
    else:
        report.checks.append(DoctorCheck(
            category="mcp",
            name="mcp.json",
            status="fail",
            detail="Not found",
            remediation="Run 'research-driven-setup install' to generate .vscode/mcp.json",
        ))

    # 4. Generated assets check
    github_dir = workspace / ".github"
    for subdir in ["agents", "prompts", "instructions", "skills", "scripts"]:
        path = github_dir / subdir
        if path.is_dir():
            count = sum(1 for _ in path.rglob("*") if _.is_file())
            report.checks.append(DoctorCheck(
                category="assets",
                name=f".github/{subdir}",
                status="pass",
                detail=f"{count} file(s)",
            ))
        else:
            report.checks.append(DoctorCheck(
                category="assets",
                name=f".github/{subdir}",
                status="warn" if subdir in ("scripts",) else "fail",
                detail="directory missing",
                remediation=f"Run 'research-driven-setup install' to generate .github/{subdir}/",
            ))

    # 5. package.json (for npm MCP deps)
    if state.has_package_json:
        report.checks.append(DoctorCheck(
            category="workspace",
            name="package.json",
            status="pass",
            detail="present",
        ))
        # Check if node_modules exists
        if (workspace / "node_modules").is_dir():
            report.checks.append(DoctorCheck(
                category="workspace",
                name="node_modules",
                status="pass",
                detail="installed",
            ))
        else:
            report.checks.append(DoctorCheck(
                category="workspace",
                name="node_modules",
                status="warn",
                detail="not installed",
                remediation="Run 'npm install' in the workspace",
            ))
    else:
        report.checks.append(DoctorCheck(
            category="workspace",
            name="package.json",
            status="fail",
            detail="not found",
            remediation="Run 'research-driven-setup install' to generate package.json",
        ))

    return report
