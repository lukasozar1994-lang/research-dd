# Customization Guide

## Modifying Generated Files

### Agents

Agent files in `.github/agents/` define custom Copilot agents. You can:

- Edit existing agent files to change behavior
- Add new agent files following the same YAML frontmatter + Markdown format
- Remove agents you don't need

**Important:** Agent files have `skip` conflict policy — the installer won't overwrite your changes on re-run or update.

### Prompts

Prompt files in `.github/prompts/` provide pre-built workflows. The same `skip` policy applies.

### Skills

Skills in `.github/skills/` contain domain-specific knowledge. Each skill directory has a `SKILL.md` file that agents reference. You can:

- Edit skill content to match your workflow
- Add new skills with a `SKILL.md` file
- Reference skills from agent files using relative paths

### Instructions

Instruction files in `.github/instructions/` provide coding guidelines that apply across all interactions. These are loaded automatically by Copilot.

## Adding Custom MCP Servers

Edit `.vscode/mcp.json` to add custom MCP servers:

```json
{
  "servers": {
    "my-custom-server": {
      "command": "npx",
      "args": ["my-custom-mcp-server"]
    }
  }
}
```

## Environment Variables

All secrets go in `.env` (never committed). See `.env.example` for available variables.

## Conflict Policy

When re-running the installer or updating:

| Policy | Behavior |
|--------|----------|
| `skip` | Keep existing file, don't overwrite |
| `overwrite` | Replace with latest framework version |
| `block` | Never touch — explicitly user-owned |

Scripts and MCP config use `overwrite` to ensure compatibility. Agent, prompt, and skill files use `skip` to preserve your customizations.
