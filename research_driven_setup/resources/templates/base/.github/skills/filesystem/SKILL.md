---
description: 'Use this skill to manage local research workflow files: saving research_plan.md, creating research_data directories, storing sources as .md in zrodla_i_analiza, reading source-index, and preparing the final analiza.md report.'
name: 'filesystem'
---

<!-- user-language: en -->

# Skill: Filesystem (Local File Management)

## Description
This MCP server provides safe read and write access to files within the user's declared workspace.

## When to use
- When `sequential-thinking` has planned a `research_plan.md` save.
- When `open-websearch` has fetched sources and they need to be saved locally to `research_data/<research-folder>/zrodla_i_analiza/`.
- When you need to create or check `source-index.md`, `source-index.json`, and the actual source `.md` files.
- When the final analysis should be based on local files, not solely on MCP tool responses.

## How to use
Always use the appropriate function calls provided by the filesystem server:
- **Create/Overwrite:** Use the `write_file` tool, providing the absolute or relative file path and content.
- **Read:** Use `read_text_file` or `read_multiple_files` to retrieve data.
- **Manage:** Use `create_directory`, `move_file`, or `edit_file` to modify structure and content.
- **Search & Info:** Use `search_files`, `directory_tree`, or `get_file_info` to explore the workspace.

## Available Tools
| Tool | Description |
| :--- | :--- |
| `read_text_file` | Reads the full content of a text file. |
| `read_media_file` | Reads image or audio files (base64). |
| `read_multiple_files` | Reads multiple files simultaneously. |
| `write_file` | Creates a new file or overwrites an existing one. |
| `edit_file` | Makes precise edits to a file. |
| `create_directory` | Creates a new directory. |
| `list_directory` | Lists directory contents. |
| `list_directory_with_sizes` | Lists directory contents with file sizes. |
| `move_file` | Moves or renames files and directories. |
| `search_files` | Recursively searches files/directories by pattern. |
| `directory_tree` | Returns directory tree structure in JSON format. |
| `get_file_info` | Retrieves detailed file/directory metadata. |
| `list_allowed_directories` | Lists directories the server has access to. |

## Compatibility with research workflow
If the workflow combines `sequential-thinking` and `open-websearch`, the `filesystem` skill handles persistent storage of work stages:
- `research_data/<research-folder>/zrodla_i_analiza/research_plan.md` after planning stage,
- `research_data/<research-folder>/zrodla_i_analiza/` directory for research artifacts,
- source `.md` files fetched by `fetchWebContent`,
- `source-index.md` and `source-index.json` as entry points for source review,
- `analiza.md` as the final report based on local files.

## Recommended usage in this workflow
1. Create `research_plan.md` after completing the first `sequential-thinking` steps.
2. Before saving sources, ensure the `research_data/<research-folder>/zrodla_i_analiza/` directory exists.
3. Save each source as a separate `.md` file instead of overwriting a single working file.
4. After collecting sources, read `source-index.md` and then use `read_multiple_files` or `read_text_file` to review the actual `.md` files.
5. Save `analiza.md` only when the synthesis is based on locally saved files.

## Best practices and limitations
- If writing a long report, build it in memory in stages and save to disk at the very end of the process.
- If the workflow creates many sources, prefer the structure `research_data/<topic>/zrodla_i_analiza/` to keep files from different studies separate and leave room for the sibling `plan_projektu/` folder.
- Before analysis, check via `list_directory` or `read_text_file` that `source-index.md` and `.md` files actually exist on disk.
- Use `read_multiple_files` when comparing several local sources at once, rather than analyzing them individually without context.
- Always write Mermaid diagram code inside standard markdown code blocks (```mermaid ... ```) so they render correctly in VS Code.
- Tools such as `write_file` and `edit_file` are destructive — use them carefully.
- All operations are restricted to directories defined in the MCP configuration.
