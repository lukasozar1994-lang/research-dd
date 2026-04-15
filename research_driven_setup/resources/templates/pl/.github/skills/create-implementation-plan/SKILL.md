---
name: create-implementation-plan
description: 'Utwórz nowy plik planu implementacji dla nowych funkcjonalności, refaktoryzacji istniejącego kodu lub aktualizacji pakietów, projektu, architektury lub infrastruktury.'
---

<!-- user-language: pl -->

# Utwórz plan implementacji

## Główna dyrektywa

Twoim celem jest utworzenie nowego pliku planu implementacji dla `${input:PlanPurpose}`. Twoje dane wyjściowe muszą być odczytywalne maszynowo, deterministyczne i ustrukturyzowane do autonomicznego wykonania przez inne systemy AI lub ludzi.

## Kontekst wykonania

Ten prompt jest zaprojektowany do komunikacji AI-do-AI i zautomatyzowanego przetwarzania. Wszystkie instrukcje muszą być interpretowane dosłownie i wykonywane systematycznie bez ludzkiej interpretacji ani wyjaśnień.

## Podstawowe wymagania

- Generuj plany implementacji, które są w pełni wykonywalne przez agentów AI lub ludzi
- Używaj deterministycznego języka bez żadnej dwuznaczności
- Strukturyzuj całą treść do zautomatyzowanego parsowania i wykonania
- Zapewnij pełną samowystarczalność bez zewnętrznych zależności dla zrozumienia

## Wymagania dotyczące struktury planu

Plany muszą składać się z dyskretnych, atomowych faz zawierających wykonywalne zadania. Każda faza musi być niezależnie przetwarzalna przez agentów AI lub ludzi bez zależności międzyfazowych, chyba że są jawnie zadeklarowane.

## Architektura faz

- Każda faza musi mieć mierzalne kryteria ukończenia
- Zadania w fazach muszą być wykonywalne równolegle, chyba że określono zależności
- Wszystkie opisy zadań muszą zawierać konkretne ścieżki plików, nazwy funkcji i dokładne szczegóły implementacji
- Żadne zadanie nie powinno wymagać ludzkiej interpretacji ani podejmowania decyzji

## Standardy implementacji zoptymalizowane dla AI

- Używaj jawnego, jednoznacznego języka bez wymaganej interpretacji
- Strukturyzuj całą treść w formatach parsowalnych maszynowo (tabele, listy, dane strukturyzowane)
- Dołączaj konkretne ścieżki plików, numery linii i dokładne odniesienia do kodu tam, gdzie to stosowne
- Definiuj wszystkie zmienne, stałe i wartości konfiguracyjne jawnie
- Zapewniaj pełny kontekst w każdym opisie zadania
- Używaj standaryzowanych prefiksów dla wszystkich identyfikatorów (REQ-, TASK- itp.)
- Dołączaj kryteria walidacji, które mogą być automatycznie weryfikowane

## Specyfikacje pliku wyjściowego

- Zapisuj pliki planu implementacji w katalogu `/plan/`
- Używaj konwencji nazewnictwa: `[cel]-[komponent]-[wersja].md`
- Prefiksy celu: `upgrade|refactor|feature|data|infrastructure|process|architecture|design`
- Przykład: `upgrade-system-command-4.md`, `feature-auth-module-1.md`
- Plik musi być poprawnym Markdown z prawidłową strukturą front matter

## Obowiązkowa struktura szablonu

Wszystkie plany implementacji muszą ściśle przestrzegać poniższego szablonu. Każda sekcja jest wymagana i musi być wypełniona konkretną, wykonalną treścią. Agenci AI muszą zwalidować zgodność z szablonem przed wykonaniem.

## Zasady walidacji szablonu

- Wszystkie pola front matter muszą być obecne i prawidłowo sformatowane
- Wszystkie nagłówki sekcji muszą dokładnie odpowiadać (z uwzględnieniem wielkości liter)
- Wszystkie prefiksy identyfikatorów muszą być w określonym formacie
- Tabele muszą zawierać wszystkie wymagane kolumny
- Żaden tekst zastępczy nie może pozostać w końcowym wyniku

## Status

Status planu implementacji musi być jasno zdefiniowany w front matter i odzwierciedlać aktualny stan planu. Status może być jednym z następujących (status_color w nawiasach): `Completed` (jasna zielona odznaka), `In progress` (żółta odznaka), `Planned` (niebieska odznaka), `Deprecated` (czerwona odznaka) lub `On Hold` (pomarańczowa odznaka). Powinien być również wyświetlany jako odznaka w sekcji wprowadzenia.

```md
---
goal: [Zwięzły tytuł opisujący cel planu implementacji pakietu]
version: [Opcjonalnie: np. 1.0, Data]
date_created: [RRRR-MM-DD]
last_updated: [Opcjonalnie: RRRR-MM-DD]
owner: [Opcjonalnie: Zespół/Osoba odpowiedzialna za tę specyfikację]
status: 'Completed'|'In progress'|'Planned'|'Deprecated'|'On Hold'
tags: [Opcjonalnie: Lista istotnych tagów lub kategorii, np. `feature`, `upgrade`, `chore`, `architecture`, `migration`, `bug` itd.]
---

# Wprowadzenie

![Status: <status>](https://img.shields.io/badge/status-<status>-<status_color>)

[Krótkie, zwięzłe wprowadzenie do planu i celu, który ma osiągnąć.]

## 1. Wymagania i ograniczenia

[Jawnie wymień wszystkie wymagania i ograniczenia wpływające na plan i sposób jego implementacji. Użyj punktów lub tabel dla jasności.]

- **REQ-001**: Wymaganie 1
- **SEC-001**: Wymaganie bezpieczeństwa 1
- **[3 LITERY]-001**: Inne wymaganie 1
- **CON-001**: Ograniczenie 1
- **GUD-001**: Wytyczna 1
- **PAT-001**: Wzorzec do naśladowania 1

## 2. Kroki implementacji

### Faza implementacji 1

- GOAL-001: [Opisz cel tej fazy, np. „Implementacja funkcji X", „Refaktoryzacja modułu Y" itd.]

| Zadanie | Opis | Ukończone | Data |
|---------|------|-----------|------|
| TASK-001 | Opis zadania 1 | ✅ | 2025-04-25 |
| TASK-002 | Opis zadania 2 | |  |
| TASK-003 | Opis zadania 3 | |  |

### Faza implementacji 2

- GOAL-002: [Opisz cel tej fazy, np. „Implementacja funkcji X", „Refaktoryzacja modułu Y" itd.]

| Zadanie | Opis | Ukończone | Data |
|---------|------|-----------|------|
| TASK-004 | Opis zadania 4 | |  |
| TASK-005 | Opis zadania 5 | |  |
| TASK-006 | Opis zadania 6 | |  |

## 3. Alternatywy

[Lista punktowa alternatywnych podejść, które były rozważane i dlaczego nie zostały wybrane. Pomaga to zapewnić kontekst i uzasadnienie wybranego podejścia.]

- **ALT-001**: Podejście alternatywne 1
- **ALT-002**: Podejście alternatywne 2

## 4. Zależności

[Wymień wszystkie zależności wymagające uwagi, takie jak biblioteki, frameworki lub inne komponenty, od których plan zależy.]

- **DEP-001**: Zależność 1
- **DEP-002**: Zależność 2

## 5. Pliki

[Wymień pliki, które zostaną dotknięte przez funkcjonalność lub zadanie refaktoryzacji.]

- **FILE-001**: Opis pliku 1
- **FILE-002**: Opis pliku 2

## 6. Testowanie

[Wymień testy, które muszą zostać zaimplementowane w celu weryfikacji funkcjonalności lub zadania refaktoryzacji.]

- **TEST-001**: Opis testu 1
- **TEST-002**: Opis testu 2

## 7. Ryzyka i założenia

[Wymień ryzyka lub założenia związane z implementacją planu.]

- **RISK-001**: Ryzyko 1
- **ASSUMPTION-001**: Założenie 1

## 8. Powiązane specyfikacje / Dalsze czytanie

[Link do powiązanej specyfikacji 1]
[Link do istotnej dokumentacji zewnętrznej]
```
