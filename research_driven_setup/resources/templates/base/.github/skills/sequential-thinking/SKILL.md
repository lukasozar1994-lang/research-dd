---
description: 'Use this skill for planning multi-stage research: breaking a topic into steps, defining queries for open-websearch, and controlling the transition from source collection to analysis of local files in research_data/<research-folder>/zrodla_i_analiza.'
name: 'sequential-thinking'
---

<!-- user-language: en -->

# Skill: Sequential Thinking (Thought Process Management)

## Description
This tool (MCP Sequential Thinking) is used to structure your research process. It prevents "hallucinations" by requiring you to outline analysis stages before taking action on files.

## When to use
- Always at the beginning of complex research, before launching plan saving or source collection.
- When the topic needs to be broken down into several queries for the `open-websearch` skill.
- When you want to plan the transition from `research_plan.md`, through saving sources to `research_data/<research-folder>/zrodla_i_analiza/`, to the final analysis.
- When you need to decide how to handle partial fetch errors or contradictions between sources.

## How to use (tool invocation)
When starting a task, use the `sequentialthinking` tool with the following parameters:
- `thought` (string): Content of your thought/research step.
- `thoughtNumber` (integer): Current step number (e.g., 1).
- `totalThoughts` (integer): Expected total number of analysis steps.
- `nextThoughtNeeded` (boolean): `true` until you reach the synthesis stage.

**Optional parameters:**
- `isRevision` (boolean): Whether you are correcting a previous thought.
- `revisesThought` (integer): Number of the thought you are correcting.
- `branchFromThought` (integer): Number of the thought from which you create a new reasoning branch.
- `branchId` (string): Branch identifier.
- `needsMoreThoughts` (boolean): Whether you need more steps than originally planned.

## Compatibility with `open-websearch`
If the workflow uses the `open-websearch` skill, the thought plan should explicitly include:
- the main topic and a list of 2–5 working queries,
- a decision whether to use a single `fetchWebContent` or the `collect-web-research.mjs` script,
- the target main directory in `research_data/<research-folder>/` and artifacts subdirectory `zrodla_i_analiza/`,
- criteria for reviewing `source-index.md` and saved `.md` files before synthesis,
- how to handle missing or contradictory sources.

## Recommended thought sequence
1. Understanding the topic and creating structure for `research_plan.md`.
2. Breaking the topic into research questions and search queries.
3. Deciding whether source collection will be done manually or via `open-websearch/scripts/collect-web-research.mjs`.
4. Defining source selection criteria and quality risks.
5. Reviewing local results in `research_data/<research-folder>/zrodla_i_analiza/`, including `source-index.md` and saved `.md` files.
6. Synthesizing conclusions and preparing the final report.

## Best practices
- The first thought should always be: "Understanding requirements and creating structure for `research_plan.md`".
- If using `open-websearch` for multiple queries, one of the early thoughts must explicitly list the queries, the main research directory, and the target directory `research_data/<research-folder>/zrodla_i_analiza/`.
- Before drawing conclusions for the final report, your second-to-last thought must contain a review of fetched sources from `research_data/<research-folder>/zrodla_i_analiza/`, with special attention to `source-index.md` and local `.md` files.
- If some sources were not fetched, use thought revision or branching to decide whether to narrow the topic, change queries, or continue analysis based on already locally saved sources.
