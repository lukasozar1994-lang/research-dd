---
name: gemini-api-python
description: 'Research the current official Google GenAI SDK for Python, determine the correct Gemini API library and installation steps, and produce up-to-date examples for text generation, streaming, chat, multimodal input, structured output, files, async usage, and function calling.'
---

# Gemini API Python Research

## Purpose

Use this skill when a user asks which Python library to use for Gemini API or how to use the current Python SDK correctly.

The goal is to produce a current, source-backed answer based on the latest official Google documentation rather than memory or legacy examples.

## Non-Negotiable Rules

- Prefer official Google sources first: libraries, quickstart, text generation, function calling, structured output, document/file processing, thinking, migration, and changelog pages.
- Treat `google-genai` as the default Python SDK for Gemini API.
- Mention `google-generativeai` only as a legacy package in migration context.
- Verify that examples use the current SDK shape, especially `from google import genai` and `genai.Client()`.
- Do not invent model names, auth steps, or feature support that are not shown in the current docs.
- If documentation pages disagree or a feature is preview-only, call that out explicitly.

## Research Workflow

1. Confirm the user's intent.
   - Is the user asking for a quick start, full integration guide, migration help, or a feature-specific example?
2. Check the current official docs.
   - Libraries page for package name and install command.
   - Quickstart for auth and first request.
   - Text generation for basic, streaming, chat, and config examples.
   - Function calling for tool declarations and call/response flow.
   - Structured output and document/file processing if relevant.
   - Migration and changelog pages for breaking changes or legacy package notes.
3. Extract the current canonical syntax.
   - Installation command.
   - Import style.
   - Client creation.
   - Sync and async request patterns.
   - Optional configuration patterns.
4. Build examples only from verified documentation.
   - Keep examples small and directly runnable.
   - Prefer the simplest code that demonstrates the requested feature.
5. State caveats and freshness clearly.
   - Mention doc update dates when available.
   - Distinguish stable behavior from preview or experimental behavior.

## Canonical Python Patterns

Use these patterns as the default starting point when they are supported by the current docs:

- `from google import genai`
- `from google.genai import types`
- `client = genai.Client()`
- `client.models.generate_content(...)`
- `client.models.generate_content_stream(...)`
- `client.chats.create(...)`
- `client.aio.models.generate_content(...)` for async workflows
- `types.GenerateContentConfig(...)` for generation settings
- `types.Tool(...)` and `types.FunctionDeclaration(...)` for function calling

## Output Structure

When answering, produce a concise research brief with these sections:

1. Recommended library
2. Installation
3. Authentication
4. Minimal working example
5. Relevant advanced examples
6. Migration notes
7. Caveats and version warnings
8. Source freshness

## Feature-Specific Guidance

### Text Generation

- Show `client.models.generate_content(...)` first.
- Include `response.text` in the example output path.
- If the user wants configuration, show `types.GenerateContentConfig`.

### Streaming

- Use `client.models.generate_content_stream(...)`.
- Iterate over chunks and print `chunk.text`.

### Chat

- Use `client.chats.create(...)`.
- Show `send_message(...)` and `get_history()` when conversation state matters.

### Async

- Use `client.aio...` for asynchronous requests.
- Mention that async is useful when the calling app is already event-loop driven.

### Multimodal Input

- Show content lists that combine text with image or file objects.
- Mention document, image, video, and audio pages only when the user asks for those modalities.

### Structured Output

- Explain how to constrain the response format when the user needs JSON or schema-shaped output.
- Keep the example aligned with the current docs instead of guessing parameter names.

### Function Calling

- Show the tool declaration, tool config, request, function call inspection, function execution, and function response round-trip.
- If the user needs manual handling, mention the function call `id` flow for Gemini 3 style responses.
- If the user wants a simpler Python experience, mention that automatic function calling is available in the Python SDK when the docs support it.

## Migration Guidance

- If the user is coming from `google-generativeai`, explain the migration path to `google-genai`.
- Highlight any feature gaps, deprecated behavior, or removed syntax.
- Make it clear that the new SDK is the official current path unless the docs say otherwise.

## Verification Checklist

Before finalizing the answer, confirm all of the following:

- The package name matches the current libraries page.
- The install command matches the quickstart or libraries page.
- The import style matches the current docs.
- The code sample works with the documented client and methods.
- Any preview-only or model-specific behavior is labeled.
- Any legacy guidance is clearly separated from the recommended path.

## Example Prompts This Skill Should Handle

- Which Python library should I use for Gemini API right now?
- Show me the current Gemini Python quickstart.
- How do I stream Gemini responses in Python?
- How do I call Gemini from Python with function calling?
- What changed from `google-generativeai` to `google-genai`?

## Source Pointers

- Gemini API libraries page
- Gemini API quickstart
- Gemini API text generation guide
- Gemini API function calling guide
- Gemini API structured output guide
- Gemini API migration guide
