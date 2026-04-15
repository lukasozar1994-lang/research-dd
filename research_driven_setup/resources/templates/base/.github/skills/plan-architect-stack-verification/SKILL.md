---
name: plan-architect-stack-verification
description: 'Verify the technology stack for a planning workflow. Use for library resolution, version comparison, changelog and migration summarization, syntax extraction for the target version, and dependency manifest reading with Context7 as the first source.'
---

<!-- user-language: en -->

# Plan Architect Stack Verification

Use this skill after the technical specification exists and before the file map or implementation plan is finalized.

## When To Use

- `03_specyfikacja_techniczna.md` is ready.
- You need current libraries, versions, configuration guidance, and migration risks.
- The plan must be grounded in up-to-date package knowledge, not model memory.

## Primary Source Order

1. `context7/*`
2. local dependency manifests in the workspace or target repo
3. `open-websearch/*` for official fallback sources such as release notes, package registries, or migration guides

## Template References

- [Stack Candidates Template](./references/stack-candidates-template.json)
- [Verified Versions Template](./references/verified-versions-template.json)
- [Technology Stack Report Template](./references/stack-technologiczny-template.md)

## Core Responsibilities

- Extract candidate libraries and frameworks from the specification.
- Resolve exact library identifiers.
- Retrieve current docs and version-specific syntax.
- Inspect dependency manifests when the target project already exists.
- Compare current, recommended, and latest stable versions.
- Summarize breaking changes, migration impact, and runtime constraints.

## Procedure

1. Read `03_specyfikacja_techniczna.md` and derive a candidate stack list.
2. Save candidate entries to `plan_projektu/artifacts/stack_candidates.json`.
3. For each candidate library, use Context7 to resolve the library id and query current docs.
4. If a workspace manifest exists, inspect it and compare pinned or current versions with the latest documented version.
5. If Context7 cannot cover a package, use `open-websearch/*` against official package docs or registries and mark the confidence level accordingly.
6. Write `plan_projektu/04_stack_technologiczny.md`.
7. Write `plan_projektu/artifacts/verified_versions.json`.

Use the linked templates in `./references/` so that version and migration data stays consistent across projects.

## Output Requirements

`04_stack_technologiczny.md` should include for each selected technology:

- role in the solution
- selected version or version range
- current syntax and API notes
- compatibility constraints
- migration or breaking-change notes
- alternatives considered
- confidence source

`artifacts/verified_versions.json` should include at least:

- `name`
- `library_id`
- `selected_version`
- `current_version`
- `latest_version`
- `source`
- `breaking_changes`
- `migration_required`
- `confidence`

## Quality Rules

- Never state library APIs from memory when Context7 is available.
- Prefer official docs and registries when using fallback web search.
- Mark uncertain entries explicitly instead of smoothing over gaps.
- Do not let implementation planning proceed on an unverified stack unless the user accepts the risk.
- Preserve the machine-readable keys from the linked JSON templates.