---
name: plan-architect-analysis
description: 'Przeanalizuj istniejący folder badawczy i utwórz artefakty planistyczne intake. Służy do podsumowania intake, ekstrakcji wymagań, separacji założeń od faktów, wykrywania ryzyk i analizy luk przed napisaniem specyfikacji technicznej.'
---

<!-- user-language: pl -->

# Analiza Plan Architect

Użyj tego skilla na początku przepływu pracy planistycznej, po wskazaniu przez użytkownika na folder badawczy i przed napisaniem jakiejkolwiek specyfikacji technicznej.

## Kiedy używać

- Root badawczy zawiera `zrodla_i_analiza/analiza.md` i notatki źródłowe, które muszą zostać przekonwertowane na dane wejściowe planowania.
- Potrzebujesz `00_intake.md` i `01_gap_analysis.md`.
- Musisz oddzielić fakty od założeń przed decyzjami architektonicznymi lub stackowymi.

## Wymagane dane wejściowe

- `zrodla_i_analiza/analiza.md`
- `zrodla_i_analiza/source-index.md` lub `zrodla_i_analiza/source-index.json` gdy dostępne
- Wszelkie zapisane notatki źródłowe w `zrodla_i_analiza/`

## Odniesienia do szablonów

- [Szablon Intake](references/intake-template.md)
- [Szablon analizy luk](references/gap-analysis-template.md)
- [Szablon wyekstrahowanych wymagań](references/extracted-requirements-template.json)

## Główne obowiązki

- Podsumuj wynik badawczy w języku zorientowanym na implementację.
- Wyodrębnij jawne wymagania i otwarte pytania.
- Oddziel potwierdzone fakty, wnioskowane założenia i nierozwiązane niewiadome.
- Zidentyfikuj ryzyka wpływające na architekturę, wybór stacka, zakres lub pewność realizacji.
- Wygeneruj analizę luk blokującą niebezpieczne dalsze planowanie.

## Procedura

1. Przeczytaj `zrodla_i_analiza/analiza.md` najpierw, następnie zbadaj lokalny indeks źródeł i notatki źródłowe.
2. Zbuduj wewnętrzną tabelę z czterema kubełkami: `fakty`, `wymagania`, `założenia`, `niewiadome`.
3. Wykryj prawdopodobny typ projektu, oczekiwany poziom jakości, ograniczenia runtime i jawne kryteria sukcesu.
4. Wymień ryzyka materialnie wpływające na przyszły plan implementacji.
5. Napisz `plan_projektu/00_intake.md`.
6. Napisz `plan_projektu/01_gap_analysis.md`.
7. Napisz `plan_projektu/artifacts/extracted_requirements.json` z polami odczytywalnymi maszynowo dla dalszych faz.

Użyj powiązanych szablonów w `references/` jako domyślnej struktury, chyba że folder badawczy wymaga jawnej wariacji.

## Wymagania wyjściowe

`00_intake.md` musi zawierać:

- sformułowanie problemu
- docelowy rezultat
- wnioskowany typ projektu
- jawne wymagania
- początkowe ograniczenia
- podsumowanie brakującego kontekstu

`01_gap_analysis.md` musi zawierać:

- potwierdzone fakty
- założenia wymagające walidacji
- niewiadome blokujące pewność projektową
- lista ryzyk z wagą
- rekomendowane działania następcze

`artifacts/extracted_requirements.json` powinien zawierać co najmniej:

- `project_type`
- `goals`
- `constraints`
- `non_goals`
- `assumptions`
- `open_questions`
- `risks`

## Zasady jakości

- Nie ukrywaj niepewności.
- Nie konwertuj założeń w wymagania.
- Jeśli badania są niekompletne, powiedz to jawnie i zachowaj blokadę.
- Utrzymuj wyniki zoptymalizowane dla następnej fazy specyfikacji, nie dla marketingu użytkownika końcowego.
- Preferuj wypełnianie powiązanych szablonów zamiast wymyślania nowej struktury wyjściowej.
