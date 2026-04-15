---
name: validate-task
description: 'Use when you need to execute task-specific validation commands, decide whether browser automation is required, and persist a ValidationPacket.'
---

# Validate Task

## Responsibilities

- Run the `validation_commands` from the execution manifest.
- If `browser_required` is true, use [Playwright CLI](../playwright-cli/SKILL.md) or the `Playwright-debug` agent.
- Persist validation evidence to `validation-packets/TASK-XXX.json`.

## Validation Policy

- Backend or docs-only scopes must skip Playwright.
- Browser scopes must include at least one Playwright evidence artifact or command transcript.
- Validation failure must prevent automatic commit.