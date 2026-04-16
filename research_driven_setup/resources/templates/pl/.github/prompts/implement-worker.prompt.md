---
agent: Implement Worker
---

<!-- user-language: pl -->

## Dane wejściowe użytkownika

```text
$ARGUMENTS
```

Musisz zinterpretować dane wejściowe użytkownika jako jedno z:

- ścieżkę do `research_data/<topic>/plan_projektu/`
- zakres zadania taki jak `TASK-005`
- połączone żądanie ze ścieżką plus zakresem

## Przepływ pracy

1. Przeczytaj `02_konstytuacja_projektu.md` (najważniejszy priorytetowy dokument dla projektu), `03_specyfikacja_techniczna.md`, `05_architektura_i_mapa_plikow.md`, `06_plan_implementacji.md`, `07_task_breakdown.md`, `08_plan_testow.md`, `09_readiness_review.md`, `11_kryteria_akceptacji.md` i `artifacts/runtime_artifact_contract.json` z wybranego pakietu planu.
2. Uruchom preflight MCP workspace przed jakąkolwiek pracą implementacyjną. Napraw brakujące wymagania lokalnych serwerów i zwaliduj konfigurację zdalną GitHub jeśli potrzeba.
3. Zbuduj mapę kontekstu dla wybranego zakresu.
4. Zbuduj manifest wykonania za pomocą `.github/scripts/implement_worker/build-execution-manifest.mjs`.
5. Utwórz lub przełącz gałąź `<topic-slug>-NNN` za pomocą `.github/scripts/implement_worker/branch-preflight.sh`.
6. Implementuj dokładnie jeden wybrany zakres zadania na raz.
7. Uruchom lokalną walidację. Jeśli manifest oznacza zakres jako związany z przeglądarką, użyj Playwright CLI i zachowaj dowody przeglądarki w pakiecie walidacji.
8. Zbuduj pakiet przeglądu za pomocą `.github/scripts/implement_worker/collect-review-packet.mjs`.
9. Jeśli decyzja pakietu przeglądu to `accept`, uruchom `.github/scripts/implement_worker/commit-after-gate.sh` i utrwal `commit.json`.
10. Zapisz `execution-report.json` i `execution-report.md` za pomocą `.github/scripts/implement_worker/write-execution-report.mjs`.
11. Zatrzymaj się po przekazaniu. Scalanie jest zawsze pozostawione deweloperowi.

## Twarde zasady

- Żadnych edycji przed pomyślnym preflight gałęzi.
- Żadnego Sentry MCP.
- Żadnego automatycznego scalania.
- Żadnej ścieżki Playwright chyba że manifest wymaga walidacji przeglądarki.
- Żadnych artefaktów uruchomieniowych poza `research_data/<topic>/przebieg_implementacji/`.

## Końcowa odpowiedź

Zgłoś:

1. Ścieżkę planu.
2. Wybrane identyfikatory zadań.
3. Nazwę gałęzi.
4. Wynik walidacji i przeglądu.
5. SHA commita jeśli utworzony.
6. Ścieżkę raportu uruchomieniowego.
