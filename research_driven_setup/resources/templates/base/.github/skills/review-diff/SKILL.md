---
name: review-diff
description: 'Use when a task implementation is complete and you need to compare the diff against acceptance criteria, validation results, and produce a ReviewPacket with accept, retry, or block.'
---

# Review Diff

## Command

```bash
node .github/scripts/implement_worker/collect-review-packet.mjs --task-id <TASK-XXX> --acceptance-file <plan-dir>/11_kryteria_akceptacji.md --validation-file <run-dir>/validation-packets/<TASK-XXX>.json --output <run-dir>/review-packets/<TASK-XXX>.json
```

## Decision Rules

- `accept` only when validation passes and the changed files are mappable to the target scope.
- `retry` when implementation is incomplete but recoverable.
- `block` when prerequisites, branch policy, or runtime assumptions fail.