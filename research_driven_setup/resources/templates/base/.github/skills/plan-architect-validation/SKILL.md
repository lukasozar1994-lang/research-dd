---
name: plan-architect-validation
description: 'Validate a project planning package before implementation. Use for test matrix construction, installation verification steps, readiness review, blocked-state reporting, and traceability checks between planning artifacts.'
---

<!-- user-language: en -->

# Plan Architect Validation

Use this skill at the end of the planning workflow, after the specification, stack verification, and implementation plan already exist.

## When To Use

- The main planning artifacts are already written.
- You need a production-grade test plan and a final go or no-go assessment.
- You need to prove consistency across all generated planning files.

## Core Responsibilities

- Build a test matrix across all critical components and flows.
- Define installation and environment verification steps.
- Report blocked items and unresolved risks.
- Check traceability across research, specification, stack, implementation, and tests.
- Produce a readiness review with pass or fail status.

## Template References

- [Test Plan Template](./references/test-plan-template.md)
- [Risks And Dependencies Template](./references/risks-and-dependencies-template.md)
- [Readiness Review Template](./references/readiness-review-template.md)
- [Test Matrix Template](./references/test-matrix-template.json)

## Procedure

1. Read all files under `plan_projektu/` created by earlier phases.
2. Build a coverage matrix from requirements to modules to tests.
3. Write `plan_projektu/08_plan_testow.md`.
4. Write `plan_projektu/10_ryzyka_i_zaleznosci.md`.
5. Write `plan_projektu/09_readiness_review.md`.
6. Write `plan_projektu/artifacts/test_matrix.json`.

Use the linked templates in `./references/` so the final validation package stays comparable across planning runs.

## Output Requirements

`08_plan_testow.md` should include:

- test levels
- critical user flows
- environment verification steps
- installation validation
- negative and edge-case coverage
- regression strategy
- test execution order

`10_ryzyka_i_zaleznosci.md` should include:

- unresolved risks
- dependency risks
- environment risks
- knowledge gaps
- mitigation suggestions

`09_readiness_review.md` should include:

- overall status: `pass` or `fail`
- summary of blocking issues
- traceability check result
- coverage confidence
- explicit next action recommendation

`artifacts/test_matrix.json` should map requirements and components to concrete test obligations.

## Quality Rules

- A readiness review cannot pass if critical requirements are not mapped to implementation units and tests.
- If any artifact conflicts with another artifact, record the conflict explicitly.
- Do not hide missing installation steps or missing environment assumptions.
- Prefer a truthful `fail` over an optimistic but unsupported `pass`.
- Preserve the required fields from the linked readiness and test matrix templates.