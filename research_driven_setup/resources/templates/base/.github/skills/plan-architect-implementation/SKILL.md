---
name: plan-architect-implementation
description: 'Create implementation-ready planning artifacts from a validated specification and stack. Use for file tree planning, module responsibility mapping, dependency ordering, task decomposition, and acceptance criteria writing.'
---

<!-- user-language: en -->

# Plan Architect Implementation

Use this skill after stack verification is complete and the selected technologies are stable enough to drive concrete planning outputs.

## When To Use

- `03_specyfikacja_techniczna.md` exists.
- `04_stack_technologiczny.md` exists and is validated.
- You need the concrete build plan, file map, tasks, and acceptance criteria.

## Core Responsibilities

- Translate the specification into a concrete file and module layout.
- Assign responsibilities to components and modules.
- Order implementation work by dependency.
- Break the work into tasks suitable for autonomous execution.
- Define acceptance criteria that make the plan testable.

## Template References

- [Architecture And File Map Template](./references/file-map-template.md)
- [Implementation Plan Template](./references/implementation-plan-template.md)
- [Task Breakdown Template](./references/task-breakdown-template.md)
- [Acceptance Criteria Template](./references/acceptance-criteria-template.md)
- [Implementation Units Template](./references/implementation-units-template.json)

## Procedure

1. Read `03_specyfikacja_techniczna.md` and `04_stack_technologiczny.md`.
2. Design the target directory structure and module boundaries.
3. Write `plan_projektu/05_architektura_i_mapa_plikow.md`.
4. Write `plan_projektu/06_plan_implementacji.md`.
5. Write `plan_projektu/07_task_breakdown.md`.
6. Write `plan_projektu/11_kryteria_akceptacji.md`.
7. Write `plan_projektu/artifacts/implementation_units.json`.

Use the linked templates in `./references/` so all planning outputs remain consistent and execution-friendly.

## Output Requirements

`05_architektura_i_mapa_plikow.md` should define:

- directories and files
- module boundaries
- responsibility per module
- interface relationships
- where tests live
- runtime and config locations

`06_plan_implementacji.md` should define:

- ordered phases
- exact implementation goals per phase
- prerequisites and dependencies
- install and environment verification steps
- done criteria per phase

`07_task_breakdown.md` should define for each task:

- task id
- purpose
- input artifacts
- files to create or update
- functions, classes, or modules to implement
- test obligations
- completion criteria

`11_kryteria_akceptacji.md` should define measurable acceptance criteria mapped to the specification.

`artifacts/implementation_units.json` should capture machine-readable task and module structure.

## Quality Rules

- Do not produce generic tasks such as "implement backend".
- Every planned file or module should have a stated responsibility.
- Acceptance criteria must be testable and linked back to the specification.
- Preserve a clear dependency chain so downstream implementation agents can execute without guessing.
- Keep identifiers and section shapes aligned with the linked templates.