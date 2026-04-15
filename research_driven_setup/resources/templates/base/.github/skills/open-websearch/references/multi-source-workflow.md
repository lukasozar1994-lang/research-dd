# Multi-Source Workflow

Ten skill służy do budowania lokalnej bazy źródeł przed analizą. Agent powinien użyć go wtedy, gdy użytkownik podaje temat badawczy, a nie pojedynczy adres URL.

## Co robi skrypt
- wykonuje jedno lub wiele zapytań przez `search`,
- scala i deduplikuje linki,
- pobiera każdą stronę przez `fetchWebContent`,
- czyści treść z typowych artefaktów HTML,
- zapisuje każdą stronę jako osobny plik `.md` w `research_data/<folder-badania>/zrodla_i_analiza/`,
- tworzy `source-index.md` i `source-index.json` z listą źródeł, zapytań oraz błędów.

## Zalecany workflow agenta
1. Odbierz temat badawczy.
2. Rozbij temat na 2-5 zapytań roboczych.
3. Uruchom skrypt z wieloma flagami `--query` albo z `--queries-file`.
4. Przeczytaj `source-index.md`.
5. Przejrzyj zapisane pliki `.md` i dopiero wtedy wykonaj analizę końcową.

## Wejścia skryptu
- `--query <tekst>`: można podać wielokrotnie.
- `--queries-file <ścieżka>`: plik `.txt` lub `.json` z listą zapytań.
- `--limit <n>`: liczba wyników na zapytanie.
- `--engines <lista>`: lista silników oddzielona przecinkami.
- `--output-dir <ścieżka>`: katalog docelowy wewnątrz workspace.
- `--max-chars <n>`: maksymalna długość treści zwracanej przez `fetchWebContent`.

## Przykłady
```bash
node .github/skills/open-websearch/scripts/collect-web-research.mjs \
  --query "MicroPython ESP32" \
  --query "MicroPython ESP32 PWM" \
  --query "MicroPython ESP32 networking" \
  --limit 3 \
  --output-dir research_data/micropython-esp32/zrodla_i_analiza
```

```bash
node .github/skills/open-websearch/scripts/collect-web-research.mjs \
  --queries-file research_data/queries.txt \
  --engines duckduckgo,bing \
  --limit 2 \
  --output-dir research_data/session-02/zrodla_i_analiza
```

## Kryteria ukończenia
- co najmniej jeden plik `.md` został zapisany lokalnie,
- powstał `source-index.md`,
- indeks zawiera zarówno zapisane źródła, jak i ewentualne błędy pobierania,
- agent analizuje lokalne pliki zamiast polegać wyłącznie na odpowiedzi narzędzia MCP.