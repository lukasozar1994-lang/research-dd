---
name: Deep Research Workspace Setup
description: 'Set up the entire workspace for working with the Deep Research agent after transferring only the .github folder: configure Node, MCP servers, package.json, .vscode/mcp.json, research_data directory, and verify functionality.'
argument-hint: 'Project name, target directory, or additional environment requirements'

---

<!-- user-language: en -->

Set up the current workspace for working with the Deep Research agent, assuming that only the `.github` folder with agents, prompts, instructions, and skills has been transferred to a new computer or project.

Work according to the assumptions from these files:
- [Deep Research agent](../agents/deep_reserch.agent.md)
- [Sequential Thinking skill](../skills/sequential-thinking/SKILL.md)
- [Filesystem skill](../skills/filesystem/SKILL.md)
- [Open-WebSearch skill](../skills/open-websearch/SKILL.md)

## Goal
Restore a complete working environment needed for the Deep Research workflow in a new workspace.

## Required scope of work
1. Check if `node`, `npm`, and `npx` are available in the system. If not, stop and report the specific missing tool.
2. If `package.json` is missing, create it. If it exists, update it minimally.
3. Install required dev dependencies:
   - `@modelcontextprotocol/sdk`
   - `@modelcontextprotocol/server-sequential-thinking`
   - `@modelcontextprotocol/server-filesystem`
   - `open-websearch`
4. Create or update `.vscode/mcp.json` to contain server configuration for:
   - `sequential-thinking`
   - `filesystem`
   - `open-websearch`
5. Ensure these directories exist:
   - `research_data/`
   - `.vscode/`
6. Remember that the Deep Research workflow saves artifacts to `research_data/<research-folder>/zrodla_i_analiza/`, so `plan_projektu/` can be created as a sibling folder.
7. Ensure `package.json` contains the script needed for multi-source workflow:
   - `skill:open-websearch:collect`
8. Verify the configuration:
   - confirm that Node dependencies and MCP configuration are correct,
   - if possible, run `skill:open-websearch:collect` on a simple example or verify the script is ready to run,
   - confirm the workspace is ready for the Deep Research agent.

## Constraints and rules
- Preserve existing user files if they do not require changes.
- Make the smallest possible set of changes needed to launch the workflow.
- Do not recreate optional diagnostic or documentation files unless needed for the workflow itself.
- If an element cannot be restored automatically, describe the gap precisely and propose the closest working alternative.
- Do not stop at analysis alone. Perform the actual file and environment configuration.

## Expected result
At the end, provide a concise summary in four parts:
1. What files and directories were created or changed.
2. What packages and commands were used for configuration.
3. What tests or verifications were run and their results.
4. Whether the workspace is ready for the Deep Research agent and any remaining gaps.
