---
name: MCP Setup Guide
description: Installation and configuration guide for MCP servers (sequential-thinking, filesystem, open-websearch) in the workspace.
---

<!-- user-language: en -->

# MCP Setup Guide

This prompt is used for quickly configuring the MCP environment in a new workspace.

## Requirements
- Node.js and npm installed.

## Installation steps

1. **Initialize workspace:**
   If the workspace does not have a `package.json`, initialize it:
   ```bash
   npm init -y
   ```

2. **Install dependencies:**
   Install the required MCP servers and SDK:
   ```bash
   npm install --save-dev @modelcontextprotocol/server-sequential-thinking @modelcontextprotocol/server-filesystem open-websearch @modelcontextprotocol/sdk
   ```

3. **Configure MCP in VS Code:**
   Create a `.vscode/mcp.json` file in the project root with the following content:

   ```json
   {
     "servers": {
       "sequential-thinking": {
         "command": "npx",
         "args": ["mcp-server-sequential-thinking"]
       },
       "filesystem": {
         "command": "npx",
         "args": ["mcp-server-filesystem", "${workspaceFolder}"]
       },
       "open-websearch": {
         "command": "npx",
         "args": ["open-websearch"],
         "env": {
           "MODE": "stdio",
           "DEFAULT_SEARCH_ENGINE": "duckduckgo"
         }
       }
     }
   }
   ```

4. **Verification:**
   You can verify server operation by creating a test script (e.g., `scripts/mcp-smoke-test.mjs`) and running it via `node scripts/mcp-smoke-test.mjs`.

## Notes
- The `sequential-thinking` server exposes a tool named `sequentialthinking`.
- Make sure the `node_modules` folder is not deleted so MCP servers remain available to VS Code.
