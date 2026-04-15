---
name: Deep Research Workspace Setup
description: 'Przygotuj cały workspace do pracy z agentem Deep Research po przeniesieniu samego folderu .github: skonfiguruj Node, serwery MCP, package.json, .vscode/mcp.json, katalog research_data oraz zweryfikuj działanie.'
argument-hint: 'Nazwa projektu, katalog docelowy albo dodatkowe wymagania środowiska'

---

Przygotuj bieżący workspace do pracy z agentem Deep Research, zakładając, że na nowy komputer lub do nowego projektu został przeniesiony tylko folder `.github` z agentami, promptami, instrukcjami i skillami.

Pracuj zgodnie z założeniami z tych plików:
- [Deep Research agent](../agents/deep_reserch.agent.md)
- [Sequential Thinking skill](../skills/sequential-thinking/SKILL.md)
- [Filesystem skill](../skills/filesystem/SKILL.md)
- [Open-WebSearch skill](../skills/open-websearch/SKILL.md)

## Cel
Odtwórz kompletne środowisko robocze potrzebne do działania workflow Deep Research w nowym workspace.

## Wymagany zakres prac
1. Sprawdź, czy w systemie są dostępne `node`, `npm` i `npx`. Jeżeli nie, zatrzymaj się i podaj konkretny brak.
2. Jeśli brakuje `package.json`, utwórz go. Jeśli istnieje, zaktualizuj go minimalnie.
3. Zainstaluj wymagane zależności developerskie:
   - `@modelcontextprotocol/sdk`
   - `@modelcontextprotocol/server-sequential-thinking`
   - `@modelcontextprotocol/server-filesystem`
   - `open-websearch`
4. Utwórz lub zaktualizuj plik `.vscode/mcp.json`, aby zawierał konfigurację serwerów:
   - `sequential-thinking`
   - `filesystem`
   - `open-websearch`
5. Upewnij się, że istnieją katalogi:
   - `research_data/`
   - `.vscode/`
6. Pamiętaj, że workflow Deep Research ma zapisywać artefakty do `research_data/<folder-badania>/zrodla_i_analiza/`, tak aby `plan_projektu/` mógł powstawać jako folder równorzędny.
7. Upewnij się, że `package.json` zawiera skrypt potrzebny do pracy z workflow wieloźródłowym:
   - `skill:open-websearch:collect`
8. Zweryfikuj konfigurację:
   - potwierdź, że zależności Node i konfiguracja MCP są poprawne,
   - jeśli to możliwe, uruchom `skill:open-websearch:collect` na prostym przykładzie lub sprawdź, że skrypt jest gotowy do uruchomienia,
   - potwierdź, że workspace jest gotowy do pracy z agentem Deep Research.

## Ograniczenia i zasady
- Zachowuj istniejące pliki użytkownika, jeśli nie wymagają zmiany.
- Wprowadzaj najmniejszy możliwy zestaw zmian potrzebnych do uruchomienia workflow.
- Nie odtwarzaj opcjonalnych plików diagnostycznych lub dokumentacyjnych, jeśli nie są potrzebne do samego działania workflow.
- Jeśli jakiś element nie może zostać odtworzony automatycznie, opisz dokładnie brak i zaproponuj najbliższą działającą alternatywę.
- Nie kończ na samej analizie. Wykonaj rzeczywistą konfigurację plików i środowiska.

## Oczekiwany rezultat
Na końcu podaj zwięzłe podsumowanie w czterech częściach:
1. Jakie pliki i katalogi zostały utworzone lub zmienione.
2. Jakie pakiety i komendy zostały użyte do konfiguracji.
3. Jakie testy lub weryfikacje zostały uruchomione i z jakim wynikiem.
4. Czy workspace jest gotowy do pracy z agentem Deep Research oraz jakie są ewentualne braki.