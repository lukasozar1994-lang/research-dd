---
description: 'Use this skill for multi-source web research: searching one or more topics, fetching multiple pages via fetchWebContent, and saving cleaned Markdown files to research_data/<research-folder>/zrodla_i_analiza before analysis.'
name: 'open-websearch'
argument-hint: 'Research topic, list of queries, or command to save multiple sources to research_data/<research-folder>/zrodla_i_analiza'
---

<!-- user-language: en -->

# Skill: Open-WebSearch MCP (Web Search and Data Retrieval)

## Description
This tool replaces commercial search engines by using multi-engine proxy servers (e.g., Bing, DuckDuckGo) to deliver results without authorization or API keys. The server integrates both JSON-format search result browsing and readable content extraction (scraping) from target articles.

## When to use
- When the user provides a topic (not a single URL) and expects multiple sources to be collected.
- When several search queries are needed for a single report.
- When `fetchWebContent` results should be saved locally as cleaned `.md` files in `research_data/<research-folder>/zrodla_i_analiza/`.
- When the agent should first build a local source base and only then proceed to analysis.

## Skill resources
- [Multi-source collection script](./scripts/collect-web-research.mjs)
- [Workflow and usage examples](./references/multi-source-workflow.md)

## How to use the functions
1. **Search (Tool `search`):**
   - `query` parameter: Precise search query.
   - `limit` parameter: Number of results (recommended: up to 5).
   - `engines` parameter: Optional list of engines (e.g., `["duckduckgo", "bing"]`).

2. **Content extraction (Tools `fetch*`):**
   After receiving search results, use the dedicated tools to fetch content:
   - `fetchLinuxDoArticle`: For Linux.do articles.
   - `fetchCsdnArticle`: For CSDN articles.
   - `fetchGithubReadme`: For GitHub README files.
   - `fetchJuejinArticle`: For Juejin articles.
   - `fetchWebContent`: For any page (supports Markdown).

## Available Tools
| Tool | Description |
| :--- | :--- |
| `search` | Web search. |
| `fetchLinuxDoArticle` | Fetches article from Linux.do. |
| `fetchCsdnArticle` | Fetches article from CSDN. |
| `fetchGithubReadme` | Fetches README from GitHub. |
| `fetchJuejinArticle` | Fetches article from Juejin. |
| `fetchWebContent` | Fetches content from any page. |

## Procedure for multiple queries
1. Define the main topic and 2–5 supporting queries.
2. Run the [multi-source collection script](./scripts/collect-web-research.mjs), passing multiple `--query` flags or a queries file.
3. The script should execute `search`, filter duplicate URLs, fetch each page via `fetchWebContent`, and save cleaned `.md` files to `research_data/<research-folder>/zrodla_i_analiza/`.
4. After completion, read the source index file `source-index.md` and the actual Markdown files before proceeding to synthesis.
5. If the script reports partial fetch errors, continue analysis based on saved sources and note the gaps.

## Example invocations
```bash
node .github/skills/open-websearch/scripts/collect-web-research.mjs \
   --query "MicroPython ESP32" \
   --query "MicroPython ESP32 Wi-Fi" \
   --limit 3 \
   --output-dir research_data/micropython-esp32/zrodla_i_analiza
```

```bash
node .github/skills/open-websearch/scripts/collect-web-research.mjs \
   --queries-file research_data/queries.txt \
   --limit 2 \
   --engines duckduckgo,bing \
   --output-dir research_data/session-01/zrodla_i_analiza
```

## Best practices
- **Result quality verification:** Snippets from Open-WebSearch can be short. Do not dismiss results with short descriptions if the source domain is widely recognized as technically reliable (e.g., docs.python.org, github.com).
- **Context management:** Always save extraction results directly to a file on the local filesystem (`Filesystem MCP`) before proceeding to analyze the next link. This limits the burden on your internal context memory.
- **Error resilience:** Open-WebSearch scrapes data live. If a page blocks the bot (e.g., 403 error or CAPTCHA during article extraction), smoothly move to the next result from the research list and note the incident in `Sequential Thinking`.
- **Mode selection:** For a single known URL, you can use `fetchWebContent` directly. For multi-source research, prefer this skill's script as it saves multiple pages and creates a source index.
