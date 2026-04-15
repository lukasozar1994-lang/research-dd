---
agent: Implement Worker
---

<!-- user-language: en -->

## User Input

```text
$ARGUMENTS
```

Use this legacy alias to invoke the `implement_worker` agent with the same execution contract as `/implement_worker`.

1. Read the selected `plan_projektu/` package.
2. Run MCP preflight.
3. Build the execution manifest.
4. Prepare or switch the branch before any edit.
5. Implement only the requested task scope.
6. Validate, review, auto-commit on gate pass, and write runtime artifacts.
7. Stop at human handoff without merge.
