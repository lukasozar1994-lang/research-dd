---
name: plan-architect-specification
description: 'Create the planning specification layer for a project blueprint. Use for constitution drafting, architecture description, non-functional requirements authoring, API and data flow modeling, and Mermaid diagrams after intake and gap analysis are complete.'
---

# Plan Architect Specification

Use this skill after the analysis phase has produced stable planning inputs and before stack verification begins.

## When To Use

- `00_intake.md` and `01_gap_analysis.md` already exist.
- You need to define planning rules, architecture, interfaces, and non-functional expectations.
- You need to produce the files that constrain later stack and implementation decisions.

## Core Responsibilities

- Draft the project constitution and constraints.
- Create a technical specification that is explicit enough for AI-driven implementation planning.
- Describe the architecture and data flow.
- Encode non-functional requirements and quality standards.
- Render key flows or architecture using Mermaid when visuals improve clarity.

## Template References

- [Project Constitution Template](./references/constitution-template.md)
- [Technical Specification Template](./references/technical-specification-template.md)
- [Architecture Decisions Template](./references/architecture-decisions-template.json)

## Procedure

1. Read `00_intake.md`, `01_gap_analysis.md`, and the original `zrodla_i_analiza/analiza.md`.
2. Decide which constraints are fixed and which are provisional.
3. Write `plan_projektu/02_konstytucja_projektu.md`.
4. Write `plan_projektu/03_specyfikacja_techniczna.md`.
5. Record major design decisions in `plan_projektu/artifacts/architecture_decisions.json`.

Use the linked templates in `./references/` as the starting point for all three artifacts.

## Output Requirements

`02_konstytucja_projektu.md` should define:

- quality bar
- security expectations
- testing baseline
- dependency policy
- documentation expectations
- operational constraints

`03_specyfikacja_techniczna.md` should define:

- system purpose and scope
- actors and use cases
- domain concepts and data entities
- components and responsibilities
- interfaces and integration boundaries
- non-functional requirements
- open design decisions requiring stack verification
- Mermaid diagrams for architecture or data flow when useful

`artifacts/architecture_decisions.json` should capture:

- decision id
- decision summary
- rationale
- dependencies
- open risks

## Quality Rules

- Keep requirements implementation-relevant and unambiguous.
- Distinguish mandatory requirements from guidelines.
- Do not choose concrete libraries here unless they are already locked by the research.
- If an interface or flow is still uncertain, mark it clearly for the stack verification phase.
- Keep the section order from the linked templates unless the user explicitly requests another format.