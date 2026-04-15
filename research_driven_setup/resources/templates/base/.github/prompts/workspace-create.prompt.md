<!-- user-language: en -->

# Goal:
Prepare a comprehensive analysis and research report on best practices for building ready-made AI agent framework installers, similar to GitHub's "Spec-kit", that enable quick and easy workspace setup for the appropriate workflow.
# Context:
Building a complete production workflow based on the following steps:
1. In-depth topic analysis and data collection by research agents:
  - `.github/agents/deep_research.agent.md` — agent that collects data from the internet, documentation, scientific publications, forums, etc. and prepares a research report.
  - `.github/agents/context7.agent.md` — agent that is an expert on technology stacks, libraries, frameworks, etc., preparing reports and analyses on specific technologies, their pros, cons, comparisons, etc.
2. Based on research reports, the planning agent (`.github/agents/plan_architect.agent.md`) prepares a detailed implementation plan containing numerous artifacts such as: intake, gap analysis, project constitution, technical specification, technology stack, architecture and file map, implementation plan, task breakdown, acceptance criteria, test plan, readiness review, risks and dependencies.
3. Based on the implementation plan, the implementation agent `.github/agents/implement_worker.agent.md` carries out the full implementation process, from environment preparation through implementation to testing and stabilization.
4. Additionally, a frontend debugging agent uses `playwright-cli` for browser interaction automation and web application debugging `.github/agents/playwright-debug.agent.md`.
5. A test scenario architect agent creates ready-made test scenarios for `playwright-debug.agent.md` based on developer-specified tasks `.github/agents/test-scenario-architect.agent.md`.

# Task:
Conduct a full topic analysis and prepare a research report on best practices for building ready-made AI agent framework installers similar to GitHub's "Spec-kit" that enable quick and easy workspace setup. The report should cover:
1. Overview of existing solutions and tools such as GitHub's "Spec-kit" and similar tools/frameworks.
2. How to build a framework installer as a ready-made GitHub project with all necessary files, scripts, documentation, etc.
3. How to build an installer that downloads everything from GitHub and installs all dependencies, including MCP server configuration.
4. How to run such an installer in VS Code for Linux/Ubuntu environments.
