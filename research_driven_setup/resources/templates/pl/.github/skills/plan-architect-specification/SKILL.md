---
name: plan-architect-specification
description: 'Utwórz warstwę specyfikacji planistycznej dla projektu planu. Służy do tworzenia konstytucji, opisu architektury, wymagań niefunkcjonalnych, modelowania API i przepływu danych oraz diagramów Mermaid po ukończeniu intake i analizy luk.'
---

<!-- user-language: pl -->

# Specyfikacja Plan Architect

Użyj tego skilla po fazie analizy, gdy istnieją stabilne dane planistyczne i przed rozpoczęciem weryfikacji stacka.

## Kiedy używać

- `00_intake.md` i `01_gap_analysis.md` już istnieją.
- Musisz zdefiniować zasady planowania, architekturę, interfejsy i oczekiwania niefunkcjonalne.
- Musisz wygenerować pliki ograniczające późniejsze decyzje stackowe i implementacyjne.

## Główne obowiązki

- Opracuj konstytucję projektu i ograniczenia.
- Stwórz specyfikację techniczną wystarczająco jawną dla planowania implementacji sterowanego przez AI.
- Opisz architekturę i przepływ danych.
- Zakoduj wymagania niefunkcjonalne i standardy jakości.
- Wyrenderuj kluczowe przepływy lub architekturę za pomocą Mermaid gdy wizualizacje poprawiają jasność.

## Odniesienia do szablonów

- [Szablon konstytucji projektu](./references/constitution-template.md)
- [Szablon specyfikacji technicznej](./references/technical-specification-template.md)
- [Szablon decyzji architektonicznych](./references/architecture-decisions-template.json)

## Procedura

1. Przeczytaj `00_intake.md`, `01_gap_analysis.md` i oryginalny `zrodla_i_analiza/analiza.md`.
2. Zdecyduj które ograniczenia są stałe a które tymczasowe.
3. Napisz `plan_projektu/02_konstytucja_projektu.md`.
4. Napisz `plan_projektu/03_specyfikacja_techniczna.md`.
5. Zapisz główne decyzje projektowe w `plan_projektu/artifacts/architecture_decisions.json`.

Użyj powiązanych szablonów w `./references/` jako punktu wyjścia dla wszystkich trzech artefaktów.

## Wymagania wyjściowe

`02_konstytucja_projektu.md` powinien definiować:

- próg jakości
- oczekiwania bezpieczeństwa
- bazę testową
- politykę zależności
- oczekiwania dokumentacyjne
- ograniczenia operacyjne

`03_specyfikacja_techniczna.md` powinien definiować:

- cel i zakres systemu
- aktorów i przypadki użycia
- koncepty domeny i encje danych
- komponenty i odpowiedzialności
- interfejsy i granice integracji
- wymagania niefunkcjonalne
- otwarte decyzje projektowe wymagające weryfikacji stacka
- diagramy Mermaid dla architektury lub przepływu danych gdy użyteczne

`artifacts/architecture_decisions.json` powinien zawierać:

- identyfikator decyzji
- podsumowanie decyzji
- uzasadnienie
- zależności
- otwarte ryzyka

## Zasady jakości

- Utrzymuj wymagania istotne dla implementacji i jednoznaczne.
- Rozróżniaj obowiązkowe wymagania od wytycznych.
- Nie wybieraj tu konkretnych bibliotek, chyba że są już zablokowane przez badania.
- Jeśli interfejs lub przepływ jest wciąż niepewny, oznacz go jasno dla fazy weryfikacji stacka.
- Zachowaj kolejność sekcji z powiązanych szablonów, chyba że użytkownik wyraźnie zażąda innego formatu.
