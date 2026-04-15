<!-- user-language: en -->

# Playwright E2E Test — [Feature Name]

## Goal
<!-- Describe the main testing goal, e.g., "Verify user login process" -->

## Context
<!-- Describe the application context needed for testing -->

### Application
- **URL**: http://localhost:3000
- **Stack**: <!-- e.g., Next.js, React, Express -->
- **Database state**: <!-- e.g., Test user: test@example.com / password123 -->

### Files to analyze
<!-- Point to key code files the agent should analyze -->
- <!-- e.g., src/pages/login.tsx -->
- <!-- e.g., src/api/auth.ts -->
- <!-- e.g., src/components/LoginForm.tsx -->

### Additional instructions
<!-- Optional agent instructions, e.g., specific requirements or constraints -->
- Start the development server before tests: `npm run dev`
- Run tests in `--headed` mode for better visibility

---

## Tasks

### Task 1: [Task name]

**Context:** <!-- Brief task context description -->

**Goal:** <!-- What exactly you want to test -->

**Additional instructions:**
- <!-- e.g., Check form validation for empty fields -->
- <!-- e.g., Verify error messages -->

---

### Task 2: [Task name]

**Context:** <!-- Brief task context description -->

**Goal:** <!-- What exactly you want to test -->

**Additional instructions:**
- <!-- Additional hints -->

---

## How to use this prompt

### Step 1 — Generate test scenarios
Open Copilot Chat and use the `test-scenario-architect` agent:
```
@test-scenario-architect Follow #prompt:playwright-e2e-test.prompt.md
```

### Step 2 — Run tests with the Playwright agent
After receiving scenarios, use the `playwright-debug` agent:
```
@playwright-debug Follow #prompt:playwright-e2e-test.prompt.md
```

> **Note**: For code safety, work in a separate branch or sandbox,
> especially in -yolo mode where the agent can modify files in a self-healing loop.
