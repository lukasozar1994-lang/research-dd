---
name: mcp-workspace-preflight
description: 'Use when a workflow depends on workspace MCP servers and you need to verify configuration, install missing local prerequisites, and run smoke checks before implementation.'
---

<!-- user-language: en -->

# MCP Workspace Preflight

Use this skill at the start of every `implement_worker` run.

## Goals

- Verify `.vscode/mcp.json` contains the required servers.
- Confirm local prerequisites for `sequential-thinking`, `filesystem`, `open-websearch`, and `context7` are present.
- Validate that the GitHub server is configured as remote HTTP with OAuth-oriented headers.
- Produce a machine-readable status report before implementation proceeds.

## Execution Steps

1. Read [mcp.json](../../../.vscode/mcp.json).
2. Run `.github/scripts/implement_worker/check-mcp-prereqs.mjs --workspace <repo-root> --smoke-local`.
3. If local packages are missing, rerun with `--install`.
4. If the GitHub server is misconfigured, repair `mcp.json` before continuing.
5. If GitHub OAuth or trust is still pending, run [github-mcp-oauth-smoke-test.prompt.md](../../prompts/github-mcp-oauth-smoke-test.prompt.md) and wait for the user to complete the interactive trust or sign-in step.

## Success Criteria

- All required local servers are configured.
- Local MCP binaries can answer a lightweight smoke command.
- GitHub remote config points to `https://api.githubcopilot.com/mcp/` with the expected headers.