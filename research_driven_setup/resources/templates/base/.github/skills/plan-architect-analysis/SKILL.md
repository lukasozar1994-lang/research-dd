---
name: plan-architect-analysis
description: 'Analyze an existing research folder and create planning intake artifacts. Use for intake summarization, requirement extraction, assumption-vs-fact separation, risk spotting, and gap analysis before writing the technical specification.'
---

# Plan Architect Analysis

Use this skill at the start of a planning workflow, after the user points to a research folder and before any technical specification is written.

## When To Use

- The research root contains `zrodla_i_analiza/analiza.md` and source notes that must be converted into planning inputs.
- You need `00_intake.md` and `01_gap_analysis.md`.
- You need to separate facts from assumptions before architecture or stack decisions.

## Required Inputs

- `zrodla_i_analiza/analiza.md`
- `zrodla_i_analiza/source-index.md` or `zrodla_i_analiza/source-index.json` when available
- Any saved source notes in `zrodla_i_analiza/`

## Template References

- [Intake Template](references/intake-template.md)
- [Gap Analysis Template](references/gap-analysis-template.md)
- [Extracted Requirements Template](references/extracted-requirements-template.json)

## Core Responsibilities

- Summarize the research outcome in implementation-oriented language.
- Extract explicit requirements and open questions.
- Separate confirmed facts, inferred assumptions, and unresolved unknowns.
- Identify risks that would affect architecture, stack choice, scope, or delivery confidence.
- Produce a gap analysis that blocks unsafe downstream planning.

## Procedure

1. Read `zrodla_i_analiza/analiza.md` first, then inspect the local source index and source notes.
2. Build an internal table with four buckets: `facts`, `requirements`, `assumptions`, `unknowns`.
3. Detect the likely project type, expected quality level, runtime constraints, and explicit success criteria.
4. List risks that would materially affect the future implementation plan.
5. Write `plan_projektu/00_intake.md`.
6. Write `plan_projektu/01_gap_analysis.md`.
7. Write `plan_projektu/artifacts/extracted_requirements.json` with machine-readable fields for downstream phases.

Use the linked templates in `references/` as the default structure unless the research folder requires an explicit variation.

## Output Requirements

`00_intake.md` must contain:

- problem statement
- target outcome
- inferred project type
- explicit requirements
- initial constraints
- missing context summary

`01_gap_analysis.md` must contain:

- confirmed facts
- assumptions requiring validation
- unknowns that block design confidence
- risk list with severity
- recommended follow-up actions

`artifacts/extracted_requirements.json` should include at least:

- `project_type`
- `goals`
- `constraints`
- `non_goals`
- `assumptions`
- `open_questions`
- `risks`

## Quality Rules

- Do not hide uncertainty.
- Do not convert assumptions into requirements.
- If the research is incomplete, say so explicitly and preserve the blocker.
- Keep the outputs optimized for the next specification phase, not for end-user marketing.
- Prefer filling the linked templates over inventing a new output structure.