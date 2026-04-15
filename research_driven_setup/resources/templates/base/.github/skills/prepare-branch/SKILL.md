---
name: prepare-branch
description: 'Use when implementation must create or switch to a branch named <topic-slug>-NNN before any file edit and persist branch context for resume.'
---

<!-- user-language: en -->

# Prepare Branch

## Command

```bash
bash .github/scripts/implement_worker/branch-preflight.sh --repo-root <repo-root> --topic <topic-slug> --run-seq <NNN> --base-branch main --output <run-dir>/branch-context.json
```

## Rules

- Branch creation happens before any edit.
- Existing matching branches are reused.
- The output file is the canonical `branch-context.json`.
- If branch creation or switching fails, the workflow must stop as `blocked`.