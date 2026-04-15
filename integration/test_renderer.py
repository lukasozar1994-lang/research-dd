"""Integration tests for workspace rendering."""

import json
import pytest

from research_driven_setup.core.conflict_policy import ConflictAction
from research_driven_setup.core.manifest import load_manifest
from research_driven_setup.core.renderer import render_workspace


@pytest.fixture
def clean_workspace(tmp_path):
    """Provide a clean temporary workspace."""
    return tmp_path


def test_render_to_clean_workspace(clean_workspace):
    manifest = load_manifest()
    results = render_workspace(manifest, clean_workspace)
    written = [r for r in results if r.action in (ConflictAction.WRITE, ConflictAction.OVERWRITE)]
    assert len(written) > 0


def test_generated_agents_exist(clean_workspace):
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    agents_dir = clean_workspace / ".github" / "agents"
    assert agents_dir.exists()
    agent_files = list(agents_dir.glob("*.md"))
    assert len(agent_files) == 6
    names = sorted(f.name for f in agent_files)
    assert "deep-research.agent.md" in names
    assert "plan-architect.agent.md" in names
    assert "implement-worker.agent.md" in names


def test_generated_prompts_exist(clean_workspace):
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    prompts_dir = clean_workspace / ".github" / "prompts"
    assert prompts_dir.exists()
    prompt_files = list(prompts_dir.glob("*.md"))
    assert len(prompt_files) == 7


def test_generated_instructions_exist(clean_workspace):
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    instructions_dir = clean_workspace / ".github" / "instructions"
    assert instructions_dir.exists()
    assert (instructions_dir / "python.instructions.md").exists()
    assert (instructions_dir / "playwright-cli.instructions.md").exists()


def test_generated_skills_exist(clean_workspace):
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    skills_dir = clean_workspace / ".github" / "skills"
    assert skills_dir.exists()
    skill_dirs = [d.name for d in skills_dir.iterdir() if d.is_dir()]
    assert "open-websearch" in skill_dirs
    assert "sequential-thinking" in skill_dirs
    assert "filesystem" in skill_dirs


def test_generated_scripts_exist(clean_workspace):
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    scripts_dir = clean_workspace / ".github" / "scripts"
    assert scripts_dir.exists()
    assert (scripts_dir / "start-context7-mcp.sh").exists()
    assert (scripts_dir / "implement_worker" / "branch-preflight.sh").exists()


def test_install_marker_created(clean_workspace):
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    marker = clean_workspace / ".research-driven" / "install.json"
    assert marker.exists()
    data = json.loads(marker.read_text())
    assert data["version"] == "0.1.0"
    assert len(data["files_written"]) > 0


def test_skip_existing_files(clean_workspace):
    """Files with skip policy should not be overwritten."""
    manifest = load_manifest()
    # Create an existing agent file
    agents_dir = clean_workspace / ".github" / "agents"
    agents_dir.mkdir(parents=True)
    agent_file = agents_dir / "deep-research.agent.md"
    agent_file.write_text("custom content")

    results = render_workspace(manifest, clean_workspace)
    skip_results = [r for r in results if r.action == ConflictAction.SKIP and "deep-research" in r.path]
    assert len(skip_results) == 1

    # Content should be preserved
    assert agent_file.read_text() == "custom content"


def test_force_overwrite(clean_workspace):
    """Force flag should overwrite existing files."""
    manifest = load_manifest()
    agents_dir = clean_workspace / ".github" / "agents"
    agents_dir.mkdir(parents=True)
    (agents_dir / "deep-research.agent.md").write_text("old content")

    results = render_workspace(manifest, clean_workspace, force=True)
    overwritten = [r for r in results if r.action == ConflictAction.OVERWRITE and "deep-research" in r.path]
    assert len(overwritten) == 1


def test_rerun_is_safe(clean_workspace):
    """Re-running install should not corrupt the workspace."""
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)
    # Run again
    results = render_workspace(manifest, clean_workspace)
    blocked = [r for r in results if r.action == ConflictAction.BLOCK]
    assert len(blocked) == 0  # No blocks on rerun


def test_workflow_surfaces_preserved(clean_workspace):
    """AC-005: Generated assets include research, planning, implementation, and browser-debug surfaces."""
    manifest = load_manifest()
    render_workspace(manifest, clean_workspace)

    agents_dir = clean_workspace / ".github" / "agents"
    agent_names = [f.name for f in agents_dir.glob("*.md")]

    # Research
    assert "deep-research.agent.md" in agent_names
    # Planning
    assert "plan-architect.agent.md" in agent_names
    # Implementation
    assert "implement-worker.agent.md" in agent_names
    # Browser debug
    assert "playwright-debug.agent.md" in agent_names
