---
name: plan-architect-validation
description: 'Zwaliduj pakiet planistyczny projektu przed implementacją. Służy do budowy macierzy testów, kroków weryfikacji instalacji, przeglądu gotowości, raportowania stanu zablokowania i kontroli śledzenia między artefaktami planistycznymi.'
---

<!-- user-language: pl -->

# Walidacja Plan Architect

Użyj tego skilla na końcu przepływu pracy planistycznej, gdy specyfikacja, weryfikacja stacka i plan implementacji już istnieją.

## Kiedy używać

- Główne artefakty planistyczne są już napisane.
- Potrzebujesz planu testów produkcyjnej jakości i końcowej oceny go lub no-go.
- Musisz udowodnić spójność we wszystkich wygenerowanych plikach planistycznych.

## Główne obowiązki

- Zbuduj macierz testów obejmującą wszystkie krytyczne komponenty i przepływy.
- Zdefiniuj kroki weryfikacji instalacji i środowiska.
- Zgłoś zablokowane pozycje i nierozwiązane ryzyka.
- Sprawdź śledzenie między badaniami, specyfikacją, stackiem, implementacją i testami.
- Wygeneruj przegląd gotowości ze statusem pass lub fail.

## Odniesienia do szablonów

- [Szablon planu testów](./references/test-plan-template.md)
- [Szablon ryzyk i zależności](./references/risks-and-dependencies-template.md)
- [Szablon przeglądu gotowości](./references/readiness-review-template.md)
- [Szablon macierzy testów](./references/test-matrix-template.json)

## Procedura

1. Przeczytaj wszystkie pliki w `plan_projektu/` utworzone przez wcześniejsze fazy.
2. Zbuduj macierz pokrycia od wymagań do modułów do testów.
3. Napisz `plan_projektu/08_plan_testow.md`.
4. Napisz `plan_projektu/10_ryzyka_i_zaleznosci.md`.
5. Napisz `plan_projektu/09_readiness_review.md`.
6. Napisz `plan_projektu/artifacts/test_matrix.json`.

Użyj powiązanych szablonów w `./references/` aby końcowy pakiet walidacji pozostał porównywalny między cyklami planowania.

## Wymagania wyjściowe

`08_plan_testow.md` powinien zawierać:

- poziomy testów
- krytyczne przepływy użytkownika
- kroki weryfikacji środowiska
- walidację instalacji
- pokrycie negatywne i przypadków brzegowych
- strategię regresji
- kolejność wykonania testów

`10_ryzyka_i_zaleznosci.md` powinien zawierać:

- nierozwiązane ryzyka
- ryzyka zależności
- ryzyka środowiskowe
- luki wiedzy
- sugestie łagodzenia

`09_readiness_review.md` powinien zawierać:

- ogólny status: `pass` lub `fail`
- podsumowanie problemów blokujących
- wynik kontroli śledzenia
- pewność pokrycia
- jawną rekomendację następnego działania

`artifacts/test_matrix.json` powinien mapować wymagania i komponenty na konkretne zobowiązania testowe.

## Zasady jakości

- Przegląd gotowości nie może przejść jeśli krytyczne wymagania nie są zmapowane na jednostki implementacji i testy.
- Jeśli jakikolwiek artefakt jest sprzeczny z innym artefaktem, zapisz konflikt jawnie.
- Nie ukrywaj brakujących kroków instalacji lub brakujących założeń środowiskowych.
- Preferuj prawdziwy `fail` od optymistycznego ale nieuzasadnionego `pass`.
- Zachowaj wymagane pola z powiązanych szablonów gotowości i macierzy testów.
