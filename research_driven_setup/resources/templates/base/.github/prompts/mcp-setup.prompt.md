---
name: MCP Setup Guide
description: Instrukcja instalacji i konfiguracji serwerów MCP (sequential-thinking, filesystem, open-websearch) w workspace.
---

# MCP Setup Guide

Ten prompt służy do szybkiego skonfigurowania środowiska MCP w nowym workspace.

## Wymagania
- Zainstalowany Node.js oraz npm.

## Kroki instalacji

1. **Inicjalizacja workspace:**
   Jeśli workspace nie posiada `package.json`, zainicjuj go:
   ```bash
   npm init -y
   ```

2. **Instalacja zależności:**
   Zainstaluj wymagane serwery MCP oraz SDK:
   ```bash
   npm install --save-dev @modelcontextprotocol/server-sequential-thinking @modelcontextprotocol/server-filesystem open-websearch @modelcontextprotocol/sdk
   ```

3. **Konfiguracja MCP w VS Code:**
   Utwórz plik `.vscode/mcp.json` w głównym katalogu projektu z następującą zawartością:

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

4. **Weryfikacja:**
   Możesz zweryfikować działanie serwerów, tworząc skrypt testowy (np. `scripts/mcp-smoke-test.mjs`) i uruchamiając go przez `node scripts/mcp-smoke-test.mjs`.

## Uwagi
- Serwer `sequential-thinking` udostępnia narzędzie o nazwie `sequentialthinking`.
- Upewnij się, że folder `node_modules` nie jest usuwany, aby serwery MCP były dostępne dla VS Code.
