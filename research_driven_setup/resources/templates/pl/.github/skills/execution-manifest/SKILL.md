---
name: execution-manifest
description: 'Użyj gdy musisz znormalizować research_data/<topic>/plan_projektu do deterministycznego manifestu wykonania z zakresem zadań, plikami docelowymi, komendami walidacji, ścieżkami uruchomieniowymi i flagami routingu przeglądarki.'
---

<!-- user-language: pl -->

# Manifest wykonania

## Dane wejściowe

- `03_specyfikacja_techniczna.md`
- `05_architektura_i_mapa_plikow.md`
- `06_plan_implementacji.md`
- `07_task_breakdown.md`
- `08_plan_testow.md`
- `11_kryteria_akceptacji.md`
- `artifacts/runtime_artifact_contract.json`

## Komenda

Uruchom:

```bash
node .github/scripts/implement_worker/build-execution-manifest.mjs --plan <plan-dir> --scope <task-id|all> --output <run-dir>/execution-manifest.json
```

## Dane wyjściowe

Manifest musi zawierać:

- `topic_slug`
- `run_sequence`
- `branch_name`
- `selected_scope`
- `task_ids`
- `tasks`
- `browser_required`
- `validation_commands`
- `target_files`
- `runtime_paths`

Szablon referencyjny: [execution-manifest-template.json](./references/execution-manifest-template.json)
