# Implement Worker

## Purpose

`implement_worker` is the execution agent for plan-driven implementation runs. It consumes `research_data/<topic>/plan_projektu/`, prepares the branch, validates MCP readiness, applies the requested task scope, and persists runtime evidence in `research_data/<topic>/przebieg_implementacji/`.

## Entry Points

- Agent: `.github/agents/implement_worker.agent.md`
- Prompt: `.github/prompts/implement_worker.prompt.md`
- Legacy prompt alias: `.github/prompts/agent_implementacja.prompt.md`

## MCP Requirements

The workspace config lives in `.vscode/mcp.json` and must contain:

- `github` as remote HTTP with OAuth and read-oriented toolsets for `context`, `repos`, `issues`, `pull_requests`, `actions`, `labels`, and `notifications`
- `context7`
- `filesystem`
- `open-websearch`
- `sequential-thinking`

Use `.github/scripts/implement_worker/check-mcp-prereqs.mjs --workspace . --smoke-local` to verify the local MCP prerequisites. If GitHub has not been trusted or authenticated yet in VS Code, run the prompt `.github/prompts/github-mcp-oauth-smoke-test.prompt.md` and complete the interactive OAuth flow.

## Workflow Summary

1. Run MCP preflight.
2. Build execution manifest.
3. Create or switch branch `<topic-slug>-NNN`.
4. Implement one task scope.
5. Validate the scope.
6. Build review packet.
7. Auto-commit on `accept`.
8. Write execution report and handoff.

## Smoke Commands

```bash
node .github/scripts/implement_worker/check-mcp-prereqs.mjs --workspace . --smoke-local
node .github/scripts/implement_worker/build-execution-manifest.mjs --plan research_data/agent-implementacja-best-practices/plan_projektu --scope TASK-005
node --test tests/implement_worker/*.mjs
```

## Merge Policy

The agent never merges. A developer reviews the branch and decides how to merge or continue the work.