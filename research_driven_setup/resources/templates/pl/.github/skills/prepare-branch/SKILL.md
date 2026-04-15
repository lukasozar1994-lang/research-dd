---
name: prepare-branch
description: 'Użyj gdy implementacja wymaga utworzenia lub przełączenia na gałąź o nazwie <topic-slug>-NNN przed jakąkolwiek edycją pliku i utrwalenia kontekstu gałęzi do wznowienia.'
---

<!-- user-language: pl -->

# Przygotowanie gałęzi

## Komenda

```bash
bash .github/scripts/implement_worker/branch-preflight.sh --repo-root <repo-root> --topic <topic-slug> --run-seq <NNN> --base-branch main --output <run-dir>/branch-context.json
```

## Zasady

- Tworzenie gałęzi następuje przed jakąkolwiek edycją.
- Istniejące pasujące gałęzie są ponownie wykorzystywane.
- Plik wyjściowy jest kanonicznym `branch-context.json`.
- Jeśli tworzenie lub przełączanie gałęzi nie powiedzie się, przepływ pracy musi się zatrzymać ze statusem `blocked`.
