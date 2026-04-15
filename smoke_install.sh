#!/usr/bin/env bash
# Smoke test: verify research-driven-setup installs correctly into a clean workspace
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

echo "=== Smoke Install Test ==="
echo "Repo: $REPO_ROOT"

# Create temp workspace
TEST_DIR=$(mktemp -d)
trap 'rm -rf "$TEST_DIR"' EXIT
echo "Target: $TEST_DIR"

# Run install
cd "$REPO_ROOT"
research-driven-setup install --workspace "$TEST_DIR" --non-interactive

# Verify key outputs
echo ""
echo "=== Verifying outputs ==="
for f in \
    ".github/agents/deep-research.agent.md" \
    ".github/agents/plan-architect.agent.md" \
    ".github/agents/implement-worker.agent.md" \
    ".github/agents/playwright-debug.agent.md" \
    ".github/prompts/plan-project.prompt.md" \
    ".github/instructions/python.instructions.md" \
    ".github/skills/open-websearch/SKILL.md" \
    ".github/scripts/start-context7-mcp.sh" \
    ".vscode/mcp.json" \
    ".research-driven/install.json" \
    ".research-driven/install-report.md" \
    ".env.example" \
    "package.json"; do
    if [ -e "$TEST_DIR/$f" ]; then
        echo "  ✓ $f"
    else
        echo "  ✗ MISSING: $f"
        exit 1
    fi
done

echo ""
echo "=== Smoke Install PASSED ==="
