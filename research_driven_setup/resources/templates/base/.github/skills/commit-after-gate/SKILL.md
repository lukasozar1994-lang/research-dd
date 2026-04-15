---
name: commit-after-gate
description: 'Use when a ReviewPacket decision is accept and you need to create the automatic commit and commit.json using the frozen TASK-XXX message template.'
---

# Commit After Gate

## Preconditions

- `ReviewPacket.decision` must equal `accept`.
- Branch preflight must already be complete.

## Command

```bash
bash .github/scripts/implement_worker/commit-after-gate.sh --repo-root <repo-root> --task-id <TASK-XXX> --task-ids <TASK-XXX,...> --task-slug <task-slug> --topic <topic-slug> --run-seq <NNN> --branch-name <topic-slug>-<NNN> --decision accept --output <run-dir>/commit.json
```

## Contract

- Subject format: `TASK-XXX: <task-slug>`
- Body lines: `Topic`, `Run`, `Branch`, `Tasks`, `Gate`
- No additional footer lines
- No commit if decision is not `accept`