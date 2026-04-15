# Instructions for GitHub Copilot Agent

## Purpose
The agent must perform front-end behavior testing in JavaScript/TypeScript exclusively with `playwright-cli` in e2e mode when the project includes a JS frontend.

## When this instruction applies
- The repository contains a JS/TS frontend (e.g., `frontend/package.json`, `src/app`, `next.config.ts`, `public`, `frontend/src`).
- The task is about testing a function, component, or user interaction in the browser.

## Agent behavior
1. Detect JS frontend presence:
   - check for `frontend/package.json` or other frontend directories.
   - when unsure, ask: "Does this test concern JavaScript frontend logic?".

2. For front-end functionality tests use `playwright-cli` (not local unit tests), e.g.:
   - `playwright-cli open http://localhost:3000`
   - `playwright-cli goto http://localhost:3000/path`
   - `playwright-cli click <selector>`
   - `playwright-cli fill <selector> "value"`
   - `playwright-cli eval "() => document.querySelector('...').textContent"`
   - `playwright-cli snapshot --filename=...`
   - `playwright-cli close`

3. If `playwright-cli` is unavailable:
   - use locally: `npx playwright-cli ...`
   - install recommendations: `npm i -D @playwright/cli` or `npm i -D playwright` (as applicable).

4. Always provide:
   - step-by-step commands to run in a terminal
   - what UI elements are being tested and how to verify results (expected state, text, selectors)
   - possible snapshots or explicit `eval` assertions

5. For backend tasks or scripts with no JS frontend layer, do not force `playwright-cli` (classic API/Python tests etc.).

## Example workflow
1. `npm run dev` (start the frontend server)
2. `playwright-cli open http://localhost:3000`
3. `playwright-cli click button#submit`
4. `playwright-cli fill input#email "test@example.com"`
5. `playwright-cli click button#confirm`
6. `playwright-cli eval "() => document.querySelector('.message').innerText"`
7. verify the result equals e.g. `'Operation completed successfully'`
8. `playwright-cli close`

## Clarification messages when uncertain
- "This task concerns UI + JS; I will execute an e2e test using playwright-cli."
- "Playwright-cli is not installed; I suggest `npx playwright-cli` or provide installation instructions."
