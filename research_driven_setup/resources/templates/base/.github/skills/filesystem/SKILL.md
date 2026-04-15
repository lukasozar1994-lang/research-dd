---
description: 'Użyj tego skilla do zarządzania lokalnymi plikami workflow badawczego: zapisu research_plan.md, tworzenia katalogów research_data, odkładania źródeł .md do zrodla_i_analiza, odczytu source-index i przygotowania końcowego raportu analiza.md.'
name: 'filesystem'
---
# Skill: Filesystem (Zarządzanie Plikami Lokalnymi)

## Opis
Dzięki temu serwerowi MCP masz bezpieczny dostęp do odczytu i zapisu plików w obrębie zadeklarowanej przestrzeni roboczej użytkownika (Workspace).

## Kiedy używać
- Gdy `sequential-thinking` zaplanował zapis `research_plan.md`.
- Gdy `open-websearch` pobrał źródła i trzeba je zapisać lokalnie do `research_data/<folder-badania>/zrodla_i_analiza/`.
- Gdy trzeba utworzyć lub sprawdzić `source-index.md`, `source-index.json` oraz właściwe pliki źródłowe `.md`.
- Gdy analiza końcowa ma być oparta na lokalnych plikach, a nie wyłącznie na odpowiedziach narzędzi MCP.

## Jak korzystać
Zawsze używaj odpowiednich wywołań funkcji zapewnionych przez serwer filesystem:
- **Tworzenie/Nadpisywanie:** Użyj narzędzia `write_file`, podając bezwzględną lub względną ścieżkę do pliku oraz zawartość (`content`).
- **Odczyt:** Użyj narzędzia `read_text_file` lub `read_multiple_files` do pobierania danych.
- **Zarządzanie:** Użyj `create_directory`, `move_file` lub `edit_file` do modyfikacji struktury i zawartości.
- **Wyszukiwanie i Informacje:** Użyj `search_files`, `directory_tree` lub `get_file_info` do eksploracji workspace.

## Dostępne narzędzia (Tools)
| Narzędzie | Opis |
| :--- | :--- |
| `read_text_file` | Odczytuje pełną zawartość pliku tekstowego. |
| `read_media_file` | Odczytuje pliki graficzne lub audio (base64). |
| `read_multiple_files` | Odczytuje wiele plików jednocześnie. |
| `write_file` | Tworzy nowy plik lub nadpisuje istniejący. |
| `edit_file` | Wykonuje precyzyjne edycje w pliku. |
| `create_directory` | Tworzy nowy katalog. |
| `list_directory` | Wyświetla zawartość katalogu. |
| `list_directory_with_sizes` | Wyświetla zawartość katalogu z rozmiarami plików. |
| `move_file` | Przenosi lub zmienia nazwę plików i katalogów. |
| `search_files` | Rekurencyjnie wyszukuje pliki/katalogi według wzorca. |
| `directory_tree` | Zwraca strukturę drzewa katalogów w formacie JSON. |
| `get_file_info` | Pobiera szczegółowe metadane pliku/katalogu. |
| `list_allowed_directories` | Wyświetla listę katalogów, do których serwer ma dostęp. |

## Kompatybilność z workflow badawczym
Jeżeli workflow łączy `sequential-thinking` i `open-websearch`, skill `filesystem` odpowiada za trwały zapis etapów pracy:
- `research_data/<folder-badania>/zrodla_i_analiza/research_plan.md` po etapie planowania,
- katalog `research_data/<folder-badania>/zrodla_i_analiza/` dla artefaktów badawczych,
- pliki źródłowe `.md` pobrane przez `fetchWebContent`,
- `source-index.md` i `source-index.json` jako punkt wejścia do przeglądu źródeł,
- `analiza.md` jako końcowy raport oparty na lokalnych plikach.

## Zalecany sposób użycia w tym workflow
1. Utwórz `research_plan.md` po zakończeniu pierwszych kroków `sequential-thinking`.
2. Przed zapisem źródeł upewnij się, że istnieje katalog `research_data/<folder-badania>/zrodla_i_analiza/`.
3. Zapisuj każde źródło jako osobny plik `.md`, zamiast nadpisywać jeden plik roboczy.
4. Po zebraniu źródeł odczytaj `source-index.md`, a następnie użyj `read_multiple_files` lub `read_text_file` do przeglądu właściwych plików `.md`.
5. Zapisz `analiza.md` dopiero wtedy, gdy synteza opiera się na lokalnie zapisanych plikach.

## Najlepsze praktyki i ograniczenia
- Jeśli zapisujesz długi raport, twórz go w pamięci etapami i zapisz w całości na dysk na samym końcu procesu.
- Jeśli workflow tworzy wiele źródeł, preferuj strukturę `research_data/micropython-esp32/zrodla_i_analiza/`, aby nie mieszać plików z różnych badań i pozostawić miejsce na sąsiedni folder `plan_projektu/`.
- Przed analizą sprawdź przez `list_directory` lub `read_text_file`, czy `source-index.md` i pliki `.md` faktycznie istnieją na dysku.
- Używaj `read_multiple_files`, gdy chcesz porównać kilka lokalnych źródeł naraz, zamiast analizować je pojedynczo bez kontekstu.
- Kody diagramów Mermaid zapisuj zawsze wewnątrz standardowych bloków kodu markdown (```mermaid ... ```), aby renderowały się poprawnie w VS Code.
- Narzędzia takie jak `write_file` oraz `edit_file` są destrukcyjne – należy używać ich z rozwagą.
- Wszystkie operacje są ograniczone do katalogów zdefiniowanych w konfiguracji MCP.