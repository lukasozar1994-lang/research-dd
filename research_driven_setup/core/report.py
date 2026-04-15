"""Report generator for install, doctor, and update flows."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from research_driven_setup.core.conflict_policy import ConflictAction, ConflictResult
from research_driven_setup.core.doctor import DoctorReport


def generate_install_report(
    workspace: Path,
    profile_name: str,
    version: str,
    render_results: list[ConflictResult],
    mcp_notes: list[str],
    bootstrap_ok: bool,
    language: str = "en",
) -> dict[str, Any]:
    """Generate a structured install report."""
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "version": version,
        "profile": profile_name,
        "language": language,
        "workspace": str(workspace),
        "bootstrap_ok": bootstrap_ok,
        "files": {
            "written": [r.path for r in render_results if r.action in (ConflictAction.WRITE, ConflictAction.OVERWRITE)],
            "skipped": [r.path for r in render_results if r.action == ConflictAction.SKIP],
            "blocked": [r.path for r in render_results if r.action == ConflictAction.BLOCK],
        },
        "mcp_notes": mcp_notes,
    }
    return report


def write_install_report(workspace: Path, report: dict[str, Any]) -> tuple[Path, Path]:
    """Write install report as JSON and Markdown."""
    diag_dir = workspace / ".research-driven"
    diag_dir.mkdir(parents=True, exist_ok=True)
    json_path = diag_dir / "install-report.json"
    md_path = diag_dir / "install-report.md"

    json_path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")

    md_lines = [
        "# Install Report",
        "",
        f"- **Date**: {report['timestamp']}",
        f"- **Version**: {report['version']}",
        f"- **Profile**: {report['profile']}",
        f"- **Workspace**: {report['workspace']}",
        f"- **Prerequisites**: {'✅ OK' if report['bootstrap_ok'] else '⚠️ Issues found'}",
        "",
        "## Files Generated",
        "",
    ]
    for f in report["files"]["written"]:
        md_lines.append(f"- ✅ `{f}`")
    md_lines.append("")

    if report["files"]["skipped"]:
        md_lines.append("## Files Skipped (already exist)")
        md_lines.append("")
        for f in report["files"]["skipped"]:
            md_lines.append(f"- ⏭️ `{f}`")
        md_lines.append("")

    if report["files"]["blocked"]:
        md_lines.append("## Files Blocked (conflicts)")
        md_lines.append("")
        for f in report["files"]["blocked"]:
            md_lines.append(f"- 🚫 `{f}`")
        md_lines.append("")

    if report["mcp_notes"]:
        md_lines.append("## MCP Setup Notes")
        md_lines.append("")
        for note in report["mcp_notes"]:
            md_lines.append(f"- ⚠️ {note}")
        md_lines.append("")

    md_lines.extend([
        "## Next Steps",
        "",
        "1. Open VS Code in this workspace",
        "2. Run `npm install` to install MCP server dependencies",
        "3. Check `.env.example` and set up any required API keys in `.env`",
        "4. Open the Command Palette and start MCP servers",
        "5. Run `research-driven-setup doctor` to verify the setup",
        "",
    ])

    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    return json_path, md_path


def generate_doctor_report_files(workspace: Path, report: DoctorReport) -> tuple[Path, Path]:
    """Write doctor report as JSON and Markdown."""
    diag_dir = workspace / ".research-driven"
    diag_dir.mkdir(parents=True, exist_ok=True)
    json_path = diag_dir / "doctor-report.json"
    md_path = diag_dir / "doctor-report.md"

    data = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "passed": report.passed,
        "checks": [
            {
                "category": c.category,
                "name": c.name,
                "status": c.status,
                "detail": c.detail,
                "remediation": c.remediation,
            }
            for c in report.checks
        ],
    }
    json_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")

    status_icon = {"pass": "✅", "warn": "⚠️", "fail": "❌"}
    md_lines = [
        "# Doctor Report",
        "",
        f"- **Date**: {data['timestamp']}",
        f"- **Overall**: {'PASS' if report.passed else 'ISSUES FOUND'}",
        "",
    ]
    current_cat = ""
    for c in report.checks:
        if c.category != current_cat:
            current_cat = c.category
            md_lines.append(f"## {current_cat.title()}")
            md_lines.append("")
        icon = status_icon.get(c.status, "❓")
        line = f"- {icon} **{c.name}**: {c.detail}"
        if c.remediation:
            line += f" → {c.remediation}"
        md_lines.append(line)
    md_lines.append("")

    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    return json_path, md_path
