---
name: report-execution
description: 'Use when you need to persist checkpoints and generate execution-report.json plus execution-report.md for human handoff after validation and review.'
---

# Report Execution

## Command

```bash
node .github/scripts/implement_worker/write-execution-report.mjs --review <review.json> --validation <validation.json> --commit <commit.json> --json-out <run-dir>/execution-report.json --md-out <run-dir>/execution-report.md
```

## Requirements

- The JSON report is the canonical source of truth.
- The Markdown report is human-readable only.
- The handoff must include branch name, commit SHA, validation result, review decision, remaining risks, and next step.