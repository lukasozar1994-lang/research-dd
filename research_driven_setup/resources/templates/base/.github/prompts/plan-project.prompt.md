<!-- user-language: en -->

# Goal:
Prepare a project and implementation plan based on `research_data/ai-agent-framework-installers-best-practices/zrodla_i_analiza/analiza.md` and user guidelines.
# Context:
1. In the current workspace I have built a complete workflow for the research-driven development methodology, which starts from preparing research and analyses using agents `.github/agents/deep_research.agent.md` and `.github/agents/context7.agent.md`, then transitions to a full project planning phase using agent `.github/agents/plan_architect.agent.md`, which creates a project plan based on research results and user guidelines that is then executed by implementation agent `.github/agents/implement_worker.agent.md`. Currently I am preparing the project plan for the topic `ai-agent-framework-installers-best-practices`, with the main source being `research_data/ai-agent-framework-installers-best-practices/zrodla_i_analiza/analiza.md`.
2. Agents use MCP servers configured in `.vscode/mcp.json`, as well as tools such as `read`, `search`, `edit`, `execute`, `todo`, `vscode/memory`, `context7/*`, `filesystem/*`, `open-websearch/*`, `sequential-thinking/*`, and `github/*`.
3. MCP tools are local except for `github/*` and `context7/*`.
4. Agents use ready-made scripts for configuration and research.
5. Agents use ready-made templates and specially prepared skills.
# Task:
Based on the analysis in `research_data/ai-agent-framework-installers-best-practices/zrodla_i_analiza/analiza.md` and user guidelines, prepare a detailed project plan covering the transformation of the entire current architecture of agents, skills, scripts, prompts, and MCP tools into a complete framework installer for research-driven development methodology.
# Execution process:
1. Carefully analyze `research_data/ai-agent-framework-installers-best-practices/zrodla_i_analiza/analiza.md`, identify key information, conclusions, and recommendations.
2. Thoroughly analyze the current agent workflow for research-driven development, skills, MCP tools, and prompts.
3. Prepare the project plan.
# Additional guidelines:
- The CLI command should be `research-driven-setup`.
- The CLI terminal should look aesthetic with clear messages and attractive ASCII art on startup.
- The plan should include a `--help` command displaying framework help.
- The plan should include documentation and a README.md.
