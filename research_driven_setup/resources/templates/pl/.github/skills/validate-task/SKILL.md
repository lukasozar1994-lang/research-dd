---
name: validate-task
description: 'Użyj gdy musisz wykonać komendy walidacyjne specyficzne dla zadania, zdecydować czy wymagana jest automatyzacja przeglądarki i utrwalić ValidationPacket.'
---

<!-- user-language: pl -->

# Walidacja zadania

## Obowiązki

- Uruchom `validation_commands` z manifestu wykonania.
- Jeśli `browser_required` jest true, użyj [Playwright CLI](../playwright-cli/SKILL.md) lub agenta `Playwright-debug`.
- Utrwal dowody walidacji w `validation-packets/TASK-XXX.json`.

## Polityka walidacji

- Zakresy backendowe lub dotyczące tylko dokumentacji muszą pomijać Playwright.
- Zakresy przeglądarki muszą zawierać co najmniej jeden artefakt dowodowy Playwright lub transkrypt komend.
- Niepowodzenie walidacji musi uniemożliwić automatyczny commit.
