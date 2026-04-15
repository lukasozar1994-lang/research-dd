---
agent: Implement Worker
---

<!-- user-language: en -->

## User Input

```text
$ARGUMENTS
```

You must interpret the user input as one of:

- a path to `research_data/<topic>/plan_projektu/`
- a task scope such as `TASK-005`
- a combined request with path plus scope

## Workflow

1. Read `03_specyfikacja_techniczna.md`, `05_architektura_i_mapa_plikow.md`, `06_plan_implementacji.md`, `07_task_breakdown.md`, `08_plan_testow.md`, `09_readiness_review.md`, `11_kryteria_akceptacji.md`, and `artifacts/runtime_artifact_contract.json` from the selected plan package.
2. Run the MCP workspace preflight before any implementation work. Repair missing local server prerequisites and validate the GitHub remote configuration if needed.
3. Build a context map for the selected scope.
4. Build an execution manifest with `.github/scripts/implement_worker/build-execution-manifest.mjs`.
5. Create or switch the branch `<topic-slug>-NNN` with `.github/scripts/implement_worker/branch-preflight.sh`.
6. Implement exactly one selected task scope at a time.
7. Run local validation. If the manifest marks the scope as browser-related, use Playwright CLI and keep the browser evidence in the validation packet.
8. Build a review packet with `.github/scripts/implement_worker/collect-review-packet.mjs`.
9. If the review packet decision is `accept`, run `.github/scripts/implement_worker/commit-after-gate.sh` and persist `commit.json`.
10. Write `execution-report.json` and `execution-report.md` with `.github/scripts/implement_worker/write-execution-report.mjs`.
11. Stop after handoff. Merge is always left to the developer.

## Hard Rules

- No edits before branch preflight succeeds.
- No Sentry MCP.
- No automatic merge.
- No Playwright path unless the manifest requires browser validation.
- No runtime artifacts outside `research_data/<topic>/przebieg_implementacji/`.

## Final Response

Report:

1. Plan path.
2. Selected task IDs.
3. Branch name.
4. Validation and review outcome.
5. Commit SHA if created.
6. Runtime report path.
