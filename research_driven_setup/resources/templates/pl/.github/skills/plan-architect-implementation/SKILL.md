---
name: plan-architect-implementation
description: 'Utwórz artefakty planistyczne gotowe do implementacji ze zwalidowanej specyfikacji i stacka. Służy do planowania drzewa plików, mapowania odpowiedzialności modułów, porządkowania zależności, dekompozycji zadań i pisania kryteriów akceptacji.'
---

<!-- user-language: pl -->

# Implementacja Plan Architect

Użyj tego skilla po ukończeniu weryfikacji stacka i gdy wybrane technologie są wystarczająco stabilne aby kierować konkretnymi wynikami planistycznymi.

## Kiedy używać

- `03_specyfikacja_techniczna.md` istnieje.
- `04_stack_technologiczny.md` istnieje i jest zwalidowany.
- Potrzebujesz konkretnego planu budowy, mapy plików, zadań i kryteriów akceptacji.

## Główne obowiązki

- Przełóż specyfikację na konkretny układ plików i modułów.
- Przypisz odpowiedzialności do komponentów i modułów.
- Uporządkuj pracę implementacyjną według zależności.
- Rozbij pracę na zadania odpowiednie do autonomicznego wykonania.
- Zdefiniuj kryteria akceptacji czyniące plan testowalnym.

## Odniesienia do szablonów

- [Szablon architektury i mapy plików](./references/file-map-template.md)
- [Szablon planu implementacji](./references/implementation-plan-template.md)
- [Szablon rozbicia zadań](./references/task-breakdown-template.md)
- [Szablon kryteriów akceptacji](./references/acceptance-criteria-template.md)
- [Szablon jednostek implementacji](./references/implementation-units-template.json)

## Procedura

1. Przeczytaj `03_specyfikacja_techniczna.md` i `04_stack_technologiczny.md`.
2. Zaprojektuj docelową strukturę katalogów i granice modułów.
3. Napisz `plan_projektu/05_architektura_i_mapa_plikow.md`.
4. Napisz `plan_projektu/06_plan_implementacji.md`.
5. Napisz `plan_projektu/07_task_breakdown.md`.
6. Napisz `plan_projektu/11_kryteria_akceptacji.md`.
7. Napisz `plan_projektu/artifacts/implementation_units.json`.

Użyj powiązanych szablonów w `./references/` aby wszystkie wyniki planistyczne pozostały spójne i przyjazne dla wykonania.

## Wymagania wyjściowe

`05_architektura_i_mapa_plikow.md` powinien definiować:

- katalogi i pliki
- granice modułów
- odpowiedzialność per moduł
- relacje interfejsów
- gdzie znajdują się testy
- lokalizacje runtime i konfiguracji

`06_plan_implementacji.md` powinien definiować:

- uporządkowane fazy
- dokładne cele implementacji per faza
- wymagania wstępne i zależności
- kroki weryfikacji instalacji i środowiska
- kryteria ukończenia per faza

`07_task_breakdown.md` powinien definiować dla każdego zadania:

- identyfikator zadania
- cel
- artefakty wejściowe
- pliki do utworzenia lub aktualizacji
- funkcje, klasy lub moduły do implementacji
- obowiązki testowe
- kryteria ukończenia

`11_kryteria_akceptacji.md` powinien definiować mierzalne kryteria akceptacji zmapowane na specyfikację.

`artifacts/implementation_units.json` powinien zawierać odczytywalną maszynowo strukturę zadań i modułów.

## Zasady jakości

- Nie generuj ogólnikowych zadań takich jak „zaimplementuj backend".
- Każdy planowany plik lub moduł powinien mieć określoną odpowiedzialność.
- Kryteria akceptacji muszą być testowalne i powiązane ze specyfikacją.
- Zachowaj jasny łańcuch zależności aby dalsi agenci implementacyjni mogli wykonywać bez zgadywania.
- Utrzymuj identyfikatory i kształty sekcji zgodne z powiązanymi szablonami.
