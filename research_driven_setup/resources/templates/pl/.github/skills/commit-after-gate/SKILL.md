---
name: commit-after-gate
description: 'Użyj gdy decyzja ReviewPacket to accept i musisz utworzyć automatyczny commit oraz commit.json przy użyciu zamrożonego szablonu wiadomości TASK-XXX.'
---

<!-- user-language: pl -->

# Commit po bramce jakości

## Warunki wstępne

- `ReviewPacket.decision` musi być równe `accept`.
- Preflight gałęzi musi być już ukończony.

## Komenda

```bash
bash .github/scripts/implement_worker/commit-after-gate.sh --repo-root <repo-root> --task-id <TASK-XXX> --task-ids <TASK-XXX,...> --task-slug <task-slug> --topic <topic-slug> --run-seq <NNN> --branch-name <topic-slug>-<NNN> --decision accept --output <run-dir>/commit.json
```

## Kontrakt

- Format tematu: `TASK-XXX: <task-slug>`
- Linie treści: `Topic`, `Run`, `Branch`, `Tasks`, `Gate`
- Brak dodatkowych linii stopki
