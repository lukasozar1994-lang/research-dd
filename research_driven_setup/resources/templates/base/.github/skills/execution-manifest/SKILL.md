---
name: execution-manifest
description: 'Use when you need to normalize research_data/<topic>/plan_projektu into a deterministic execution manifest with task scope, target files, validation commands, runtime paths, and browser routing flags.'
---

# Execution Manifest

## Inputs

- `03_specyfikacja_techniczna.md`
- `05_architektura_i_mapa_plikow.md`
- `06_plan_implementacji.md`
- `07_task_breakdown.md`
- `08_plan_testow.md`
- `11_kryteria_akceptacji.md`
- `artifacts/runtime_artifact_contract.json`

## Command

Run:

```bash
node .github/scripts/implement_worker/build-execution-manifest.mjs --plan <plan-dir> --scope <task-id|all> --output <run-dir>/execution-manifest.json
```

## Output

The manifest must include:

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

Reference template: [execution-manifest-template.json](./references/execution-manifest-template.json)