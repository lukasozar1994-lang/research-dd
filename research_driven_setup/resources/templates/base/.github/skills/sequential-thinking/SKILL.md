---
description: 'Użyj tego skilla do planowania wieloetapowego researchu: rozbijania tematu na kroki, definiowania zapytań do open-websearch i kontrolowania przejścia od zbierania źródeł do analizy lokalnych plików w research_data/<folder-badania>/zrodla_i_analiza.'
name: 'sequential-thinking'
---


# Skill: Sequential Thinking (Zarządzanie procesem myślowym)

## Opis
To narzędzie (MCP Sequential Thinking) służy do ustrukturyzowania Twojego procesu badawczego. Pozwala uniknąć "halucynacji" poprzez zmuszenie Cię do rozpisania etapów analizy przed podjęciem akcji na plikach.

## Kiedy używać
- Zawsze na początku złożonego researchu, zanim uruchomisz zapis planu lub zbieranie źródeł.
- Gdy temat wymaga rozbicia na kilka zapytań do skilla `open-websearch`.
- Gdy chcesz zaplanować przejście od `research_plan.md`, przez zapis źródeł do `research_data/<folder-badania>/zrodla_i_analiza/`, aż po analizę końcową.
- Gdy musisz zdecydować, jak reagować na częściowe błędy pobierania lub sprzeczności między źródłami.

## Jak korzystać (wywołanie narzędzi)
Kiedy rozpoczynasz zadanie, użyj narzędzia `sequentialthinking`, dostarczając następujące parametry:
- `thought` (string): Treść Twojej myśli/kroku badawczego.
- `thoughtNumber` (integer): Aktualny numer kroku (np. 1).
- `totalThoughts` (integer): Przewidywana całkowita liczba kroków w analizie.
- `nextThoughtNeeded` (boolean): `true`, dopóki nie dotrzesz do etapu syntezy.

**Parametry opcjonalne:**
- `isRevision` (boolean): Czy poprawiasz poprzednią myśl.
- `revisesThought` (integer): Numer myśli, którą poprawiasz.
- `branchFromThought` (integer): Numer myśli, od której tworzysz nową gałąź rozumowania.
- `branchId` (string): Identyfikator gałęzi.
- `needsMoreThoughts` (boolean): Czy potrzebujesz więcej kroków niż pierwotnie zakładałeś.

## Kompatybilność z `open-websearch`
Jeżeli workflow używa skilla `open-websearch`, plan myślowy powinien zawierać jawnie:
- temat główny i listę 2-5 zapytań roboczych,
- decyzję, czy użyć pojedynczego `fetchWebContent`, czy skryptu `collect-web-research.mjs`,
- docelowy katalog główny w `research_data/<folder-badania>/` i podkatalog artefaktów `zrodla_i_analiza/`,
- kryterium przeglądu `source-index.md` i zapisanych plików `.md` przed syntezą,
- sposób postępowania przy brakujących lub sprzecznych źródłach.

## Zalecana sekwencja myśli
1. Zrozumienie tematu i stworzenie struktury dla `research_plan.md`.
2. Rozbicie tematu na pytania badawcze i zapytania do wyszukiwarki.
3. Decyzja, czy zbieranie źródeł będzie wykonywane ręcznie, czy przez `open-websearch/scripts/collect-web-research.mjs`.
4. Określenie kryteriów wyboru źródeł i ryzyk jakościowych.
5. Przegląd lokalnych wyników w `research_data/<folder-badania>/zrodla_i_analiza/`, w tym `source-index.md` i zapisanych plików `.md`.
6. Synteza wniosków i przygotowanie raportu końcowego.

## Najlepsze praktyki
- Pierwsza myśl to zawsze: "Zrozumienie wymagań i stworzenie struktury dla `research_plan.md`".
- Jeżeli używasz `open-websearch` dla wielu zapytań, jedna z wczesnych myśli musi jawnie rozpisać listę zapytań, katalog główny badania i katalog docelowy `research_data/<folder-badania>/zrodla_i_analiza/`.
- Zanim wyciągniesz wnioski do raportu końcowego, Twoja przedostatnia myśl musi zawierać przegląd pobranych źródeł z folderu `research_data/<folder-badania>/zrodla_i_analiza/`, ze szczególnym uwzględnieniem `source-index.md` i lokalnych plików `.md`.
- Jeżeli część źródeł nie została pobrana, użyj rewizji lub rozgałęzienia myśli, aby zdecydować, czy zawęzić temat, zmienić zapytania, czy kontynuować analizę na podstawie źródeł już zapisanych lokalnie.