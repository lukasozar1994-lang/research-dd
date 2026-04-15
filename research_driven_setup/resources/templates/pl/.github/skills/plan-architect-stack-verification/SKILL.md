---
name: plan-architect-stack-verification
description: 'Zweryfikuj stos technologiczny dla przepływu pracy planistycznej. Służy do rozwiązywania bibliotek, porównywania wersji, podsumowania dziennika zmian i migracji, ekstrakcji składni dla wersji docelowej i odczytu manifestu zależności z Context7 jako pierwszym źródłem.'
---

<!-- user-language: pl -->

# Weryfikacja stacka Plan Architect

Użyj tego skilla po istnieniu specyfikacji technicznej i przed finalizacją mapy plików lub planu implementacji.

## Kiedy używać

- `03_specyfikacja_techniczna.md` jest gotowy.
- Potrzebujesz aktualnych bibliotek, wersji, wskazówek konfiguracyjnych i ryzyk migracyjnych.
- Plan musi być oparty na aktualnej wiedzy o pakietach, a nie na pamięci modelu.

## Kolejność głównych źródeł

1. `context7/*`
2. lokalne manifesty zależności w workspace lub docelowym repo
3. `open-websearch/*` do oficjalnych źródeł zapasowych takich jak notatki o wydaniach, rejestry pakietów lub przewodniki migracyjne

## Odniesienia do szablonów

- [Szablon kandydatów stacka](./references/stack-candidates-template.json)
- [Szablon zweryfikowanych wersji](./references/verified-versions-template.json)
- [Szablon raportu stosu technologicznego](./references/stack-technologiczny-template.md)

## Główne obowiązki

- Wyodrębnij kandydackie biblioteki i frameworki ze specyfikacji.
- Rozwiąż dokładne identyfikatory bibliotek.
- Pobierz aktualne dokumenty i składnię specyficzną dla wersji.
- Zbadaj manifesty zależności gdy projekt docelowy już istnieje.
- Porównaj bieżące, rekomendowane i najnowsze stabilne wersje.
- Podsumuj zmiany łamiące, wpływ migracji i ograniczenia runtime.

## Procedura

1. Przeczytaj `03_specyfikacja_techniczna.md` i wyprowadź listę kandydackiego stacka.
2. Zapisz wpisy kandydatów do `plan_projektu/artifacts/stack_candidates.json`.
3. Dla każdej kandydackiej biblioteki użyj Context7 do rozwiązania identyfikatora biblioteki i zapytania o aktualne dokumenty.
4. Jeśli manifest workspace istnieje, zbadaj go i porównaj przypięte lub bieżące wersje z najnowszą udokumentowaną wersją.
5. Jeśli Context7 nie może pokryć pakietu, użyj `open-websearch/*` przeciwko oficjalnym dokumentom pakietu lub rejestrom i oznacz odpowiednio poziom pewności.
6. Napisz `plan_projektu/04_stack_technologiczny.md`.
7. Napisz `plan_projektu/artifacts/verified_versions.json`.

Użyj powiązanych szablonów w `./references/` aby dane wersji i migracji pozostały spójne między projektami.

## Wymagania wyjściowe

`04_stack_technologiczny.md` powinien zawierać dla każdej wybranej technologii:

- rolę w rozwiązaniu
- wybraną wersję lub zakres wersji
- notatki o aktualnej składni i API
- ograniczenia kompatybilności
- notatki o migracji lub zmianach łamiących
- rozważane alternatywy
- źródło pewności

`artifacts/verified_versions.json` powinien zawierać co najmniej:

- `name`
- `library_id`
- `selected_version`
- `current_version`
- `latest_version`
- `source`
- `breaking_changes`
- `migration_required`
- `confidence`

## Zasady jakości

- Nigdy nie podawaj API bibliotek z pamięci gdy Context7 jest dostępny.
- Preferuj oficjalne dokumenty i rejestry gdy używasz zapasowego wyszukiwania.
- Oznaczaj niepewne wpisy jawnie zamiast wygładzać luki.
- Nie pozwalaj planowaniu implementacji postępować na niezweryfikowanym stacku, chyba że użytkownik akceptuje ryzyko.
- Zachowaj odczytywalne maszynowo klucze z powiązanych szablonów JSON.
