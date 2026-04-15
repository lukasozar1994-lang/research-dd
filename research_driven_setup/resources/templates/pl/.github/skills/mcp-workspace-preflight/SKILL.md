---
name: mcp-workspace-preflight
description: 'Użyj gdy przepływ pracy zależy od serwerów MCP workspace i musisz zweryfikować konfigurację, zainstalować brakujące lokalne wymagania i uruchomić testy dymne przed implementacją.'
---

<!-- user-language: pl -->

# Preflight MCP Workspace

Używaj tego skilla na początku każdego uruchomienia `implement_worker`.

## Cele

- Zweryfikuj czy `.vscode/mcp.json` zawiera wymagane serwery.
- Potwierdź obecność lokalnych wymagań dla `sequential-thinking`, `filesystem`, `open-websearch` i `context7`.
- Sprawdź czy serwer GitHub jest skonfigurowany jako zdalny HTTP z nagłówkami zorientowanymi na OAuth.
- Wygeneruj raport statusu w formacie maszynowym przed kontynuowaniem implementacji.

## Kroki wykonania

1. Przeczytaj [mcp.json](../../../.vscode/mcp.json).
2. Uruchom `.github/scripts/implement_worker/check-mcp-prereqs.mjs --workspace <repo-root> --smoke-local`.
3. Jeśli brakuje lokalnych pakietów, uruchom ponownie z `--install`.
4. Jeśli serwer GitHub jest błędnie skonfigurowany, napraw `mcp.json` przed kontynuowaniem.
5. Jeśli OAuth lub zaufanie GitHub wciąż oczekuje, uruchom [github-mcp-oauth-smoke-test.prompt.md](../../prompts/github-mcp-oauth-smoke-test.prompt.md) i poczekaj aż użytkownik ukończy interaktywny krok zaufania lub logowania.

## Kryteria sukcesu

- Wszystkie wymagane serwery lokalne są skonfigurowane.
- Lokalne pliki binarne MCP mogą odpowiedzieć na lekką komendę testową.
- Zdalna konfiguracja GitHub wskazuje na `https://api.githubcopilot.com/mcp/` z oczekiwanymi nagłówkami.
