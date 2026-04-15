---
name: report-execution
description: 'Użyj gdy musisz utrwalić punkty kontrolne i wygenerować execution-report.json oraz execution-report.md do przekazania człowiekowi po walidacji i przeglądzie.'
---

<!-- user-language: pl -->

# Raport z wykonania

## Komenda

```bash
node .github/scripts/implement_worker/write-execution-report.mjs --review <review.json> --validation <validation.json> --commit <commit.json> --json-out <run-dir>/execution-report.json --md-out <run-dir>/execution-report.md
```

## Wymagania

- Raport JSON jest kanonicznym źródłem prawdy.
- Raport Markdown jest przeznaczony tylko do odczytu przez człowieka.
- Przekazanie musi zawierać nazwę gałęzi, SHA commita, wynik walidacji, decyzję przeglądu, pozostałe ryzyka i następny krok.
