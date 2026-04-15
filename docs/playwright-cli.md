# Playwright CLI — Installation & Usage Guide

This guide covers installing and using **Playwright CLI** (`@playwright/cli`) within the Research-Driven Setup framework. Playwright CLI is a token-efficient, command-line tool for browser automation that integrates with GitHub Copilot agents via **skills**.

> **Playwright CLI vs Playwright MCP**: CLI-based workflows are more token-efficient than MCP because they avoid loading large tool schemas and verbose accessibility trees into the model context. Choose the **Research & Development + Playwright E2E Testing** profile if your project has a web frontend.

## Installation

### 1. Install Playwright CLI globally

```bash
npm install -g @playwright/cli@latest
```

Verify the installation:

```bash
playwright-cli --version
playwright-cli --help
```

### 2. Install skills (required for agent integration)

Skills provide the framework agents with detailed reference guides for Playwright CLI commands:

```bash
playwright-cli install --skills
```

This installs skill files into your workspace that agents like `playwright-debug` and `test-scenario-architect` use to understand available commands.

### 3. Choose the Playwright profile during framework install

When running `research-driven-setup`, select the **Research & Development + Playwright E2E Testing** profile:

```bash
research-driven-setup install --profile ubuntu-research-playwright
```

This profile includes the same agents and MCP servers as the default profile, plus the `playwright-debug.agent.md` and `test-scenario-architect.agent.md` agents preconfigured for Playwright CLI workflows.

## How It Works in the Framework

The framework provides two agents that work together with Playwright CLI:

### Agent Workflow

```
┌─────────────────────────┐     ┌──────────────────────────┐     ┌─────────────────────────┐
│  1. Write a prompt       │     │  2. Generate scenarios    │     │  3. Execute & debug      │
│  (your task description) │────▶│  test-scenario-architect  │────▶│  playwright-debug        │
│                          │     │  agent                    │     │  agent                   │
└─────────────────────────┘     └──────────────────────────┘     └─────────────────────────┘
```

1. **You write a prompt** — Describe your testing goal, context (scripts, functions, database state), and specific tasks in a `.prompt.md` file.
2. **`test-scenario-architect` agent** — Reads your prompt, analyzes the codebase, and generates executable test scenarios (in Polish, structured for `playwright-cli`).
3. **`playwright-debug` agent** — Takes the prompt + scenarios, generates and runs `playwright-cli` commands, iterates in a self-healing loop to fix issues.

### Step-by-step

#### Step 1: Create your prompt

Create a file in `.github/prompts/` (e.g., `e2e-test-login.prompt.md`) describing what you want to test. See the template file `.github/prompts/playwright-e2e-test.prompt.md` for the recommended structure.

#### Step 2: Generate test scenarios

Open GitHub Copilot Chat, select the `@test-scenario-architect` agent, and reference your prompt:

```
@test-scenario-architect Follow #prompt:e2e-test-login.prompt.md
```

The agent will analyze your codebase and generate structured test scenarios.

#### Step 3: Run the tests

Select the `@playwright-debug` agent and provide both the prompt and scenarios:

```
@playwright-debug Follow #prompt:e2e-test-login.prompt.md
```

The agent will:
- Open the browser via `playwright-cli open <url>`
- Execute each test scenario step by step
- Take snapshots and screenshots at key points
- Self-heal when encountering errors (retry with corrected selectors, wait for elements, etc.)

> **Security tip**: Use **-yolo mode** only in a separate branch or sandbox to protect your main codebase from unintended changes during the self-healing loop.

## Common Playwright CLI Commands

### Browser control

```bash
playwright-cli open http://localhost:3000              # open browser
playwright-cli open http://localhost:3000 --headed     # open with visible browser
playwright-cli goto http://localhost:3000/login        # navigate to URL
playwright-cli close                                   # close browser
```

### Interacting with elements

```bash
playwright-cli snapshot                     # capture page state with element refs
playwright-cli click e15                    # click element by ref from snapshot
playwright-cli fill e22 "user@example.com"  # fill input field
playwright-cli fill e22 "query" --submit    # fill and press Enter
playwright-cli type "Hello world"           # type into focused element
playwright-cli press Enter                  # press a key
playwright-cli select e30 "option-value"    # select dropdown option
playwright-cli check e40                    # check checkbox
playwright-cli hover e50                    # hover over element
```

### Assertions & debugging

```bash
playwright-cli eval "() => document.querySelector('.msg').textContent"   # evaluate JS
playwright-cli screenshot                   # capture screenshot
playwright-cli screenshot --filename=test   # save with specific name
playwright-cli console                      # show console messages
playwright-cli network                      # show network requests
```

### Sessions

```bash
playwright-cli -s=mytest open http://localhost:3000  # named session
playwright-cli list                                  # list active sessions
playwright-cli close-all                             # close all browsers
```

## Headed vs Headless

By default, `playwright-cli` runs headless. To see the browser window:

```bash
playwright-cli open http://localhost:3000 --headed
```

Use `playwright-cli show` to open a visual dashboard showing all running browser sessions.

## Troubleshooting

### `playwright-cli` command not found

```bash
# Install globally
npm install -g @playwright/cli@latest

# Or use via npx
npx playwright-cli --help
```

### Browser doesn't start

```bash
# Check Node.js version (18+ required)
node --version

# Try with a specific browser
playwright-cli open --browser=chrome http://localhost:3000
```

### Skills not available to agents

```bash
# Install skills in your workspace
playwright-cli install --skills
```

## Further Reading

- [Playwright CLI Repository](https://github.com/microsoft/playwright-cli)
- [Playwright MCP Repository](https://github.com/microsoft/playwright-mcp) (alternative MCP-based approach)
- [Playwright Documentation](https://playwright.dev/)
