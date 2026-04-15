# Profiles

## ubuntu-research (Default)

Full research-driven development workflow for Ubuntu with VS Code and GitHub Copilot Chat.

### Included Agents

| Agent | Purpose |
|-------|---------|
| Deep Research | Multi-source research and analysis |
| Plan Architect | Turn research into project blueprints |
| Implement Worker | Execute implementation plans |
| Playwright Debug | Browser automation debugging |
| Test Scenario Architect | Generate test scenarios |
| Context7 | Library documentation lookup |

### MCP Servers

| Server | Type | Purpose |
|--------|------|---------|
| github | Remote HTTP | Read-only access to GitHub repos, issues, PRs |
| sequential-thinking | Local (npx) | Structured reasoning and planning |
| filesystem | Local (npx) | File system operations for agents |
| open-websearch | Local (npx) | Web search and content fetching |
| context7 | Local (bash) | Library documentation (requires API key) |

## ubuntu-research-playwright

Extends `ubuntu-research` with Playwright browser automation for end-to-end testing and frontend debugging.

### Additional Features

- Playwright CLI instructions for browser automation
- Playwright debug agent for interactive browser control
- Frontend testing workflow integration
