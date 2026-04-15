---
name: create-specification
description: 'Utwórz nowy plik specyfikacji dla rozwiązania, zoptymalizowany do wykorzystania przez generatywne AI.'
---

<!-- user-language: pl -->

# Utwórz specyfikację

Twoim celem jest utworzenie nowego pliku specyfikacji dla `${input:SpecPurpose}`.

Plik specyfikacji musi definiować wymagania, ograniczenia i interfejsy dla komponentów rozwiązania w sposób jasny, jednoznaczny i ustrukturyzowany do efektywnego wykorzystania przez generatywne AI. Przestrzegaj ustalonych standardów dokumentacji i upewnij się, że treść jest odczytywalna maszynowo i samowystarczalna.

## Najlepsze praktyki dla specyfikacji gotowych na AI

- Używaj precyzyjnego, jawnego i jednoznacznego języka.
- Jasno rozróżniaj wymagania, ograniczenia i rekomendacje.
- Używaj strukturyzowanego formatowania (nagłówki, listy, tabele) dla łatwego parsowania.
- Unikaj idiomów, metafor lub odwołań zależnych od kontekstu.
- Definiuj wszystkie akronimy i terminy specyficzne dla domeny.
- Dołączaj przykłady i przypadki brzegowe tam, gdzie to stosowne.
- Upewnij się, że dokument jest samowystarczalny i nie polega na zewnętrznym kontekście.

Specyfikacja powinna być zapisana w katalogu [.github/spec/] i nazwana zgodnie z konwencją: `spec-[a-z0-9-]+.md`, gdzie nazwa powinna opisywać treść specyfikacji, zaczynając od ogólnego celu, który jest jednym z [schema, tool, data, infrastructure, process, architecture, lub design].

Plik specyfikacji musi być sformatowany w poprawnym Markdown.

Pliki specyfikacji muszą przestrzegać poniższego szablonu, zapewniając odpowiednie wypełnienie wszystkich sekcji. Front matter dla markdown powinien być prawidłowo ustrukturyzowany zgodnie z poniższym przykładem:

```md
---
title: [Zwięzły tytuł opisujący zakres specyfikacji]
version: [Opcjonalnie: np. 1.0, Data]
date_created: [RRRR-MM-DD]
last_updated: [Opcjonalnie: RRRR-MM-DD]
owner: [Opcjonalnie: Zespół/Osoba odpowiedzialna za tę specyfikację]
tags: [Opcjonalnie: Lista istotnych tagów lub kategorii, np. `infrastructure`, `process`, `design`, `app` itd.]
---

# Wprowadzenie

[Krótkie, zwięzłe wprowadzenie do specyfikacji i celu, który ma osiągnąć.]

## 1. Cel i zakres

[Podaj jasny, zwięzły opis celu specyfikacji i zakresu jej zastosowania. Określ docelową publiczność i wszelkie założenia.]

## 2. Definicje

[Wymień i zdefiniuj wszystkie akronimy, skróty i terminy specyficzne dla domeny używane w tej specyfikacji.]

## 3. Wymagania, ograniczenia i wytyczne

[Jawnie wymień wszystkie wymagania, ograniczenia, zasady i wytyczne. Użyj punktów lub tabel dla jasności.]

- **REQ-001**: Wymaganie 1
- **SEC-001**: Wymaganie bezpieczeństwa 1
- **[3 LITERY]-001**: Inne wymaganie 1
- **CON-001**: Ograniczenie 1
- **GUD-001**: Wytyczna 1
- **PAT-001**: Wzorzec do naśladowania 1

## 4. Interfejsy i kontrakty danych

[Opisz interfejsy, API, kontrakty danych lub punkty integracji. Użyj tabel lub bloków kodu dla schematów i przykładów.]

## 5. Kryteria akceptacji

[Zdefiniuj jasne, testowalne kryteria akceptacji dla każdego wymagania używając formatu Given-When-Then tam, gdzie to stosowne.]

- **AC-001**: Mając [kontekst], Gdy [akcja], Wtedy [oczekiwany rezultat]
- **AC-002**: System powinien [konkretne zachowanie] gdy [warunek]
- **AC-003**: [Dodatkowe kryteria akceptacji w razie potrzeby]

## 6. Strategia automatyzacji testów

[Zdefiniuj podejście do testowania, frameworki i wymagania automatyzacji.]

- **Poziomy testów**: Jednostkowe, Integracyjne, End-to-End
- **Frameworki**: MSTest, FluentAssertions, Moq (dla aplikacji .NET)
- **Zarządzanie danymi testowymi**: [podejście do tworzenia i czyszczenia danych testowych]
- **Integracja CI/CD**: [automatyczne testowanie w pipeline'ach GitHub Actions]
- **Wymagania pokrycia**: [minimalne progi pokrycia kodu]
- **Testowanie wydajności**: [podejście do testów obciążenia i wydajności]

## 7. Uzasadnienie i kontekst

[Wyjaśnij uzasadnienie wymagań, ograniczeń i wytycznych. Podaj kontekst dla decyzji projektowych.]

## 8. Zależności i integracje zewnętrzne

[Zdefiniuj systemy zewnętrzne, usługi i zależności architektoniczne wymagane dla tej specyfikacji. Skup się na tym **co** jest potrzebne, a nie **jak** jest implementowane. Unikaj konkretnych wersji pakietów lub bibliotek, chyba że stanowią ograniczenia architektoniczne.]

### Systemy zewnętrzne
- **EXT-001**: [Nazwa systemu zewnętrznego] - [Cel i typ integracji]

### Usługi zewnętrzne
- **SVC-001**: [Nazwa usługi] - [Wymagane możliwości i wymagania SLA]

### Zależności infrastrukturalne
- **INF-001**: [Komponent infrastruktury] - [Wymagania i ograniczenia]

### Zależności danych
- **DAT-001**: [Zewnętrzne źródło danych] - [Format, częstotliwość i wymagania dostępu]

### Zależności platformy technologicznej
- **PLT-001**: [Wymaganie platformy/runtime] - [Ograniczenia wersji i uzasadnienie]

### Zależności zgodności
- **COM-001**: [Wymóg regulacyjny lub zgodności] - [Wpływ na implementację]

**Uwaga**: Ta sekcja powinna skupiać się na zależnościach architektonicznych i biznesowych, a nie na konkretnych implementacjach pakietów. Na przykład, określ „biblioteka uwierzytelniania OAuth 2.0" zamiast „Microsoft.AspNetCore.Authentication.JwtBearer v6.0.1".

## 9. Przykłady i przypadki brzegowe

    ```code
    // Fragment kodu lub przykład danych demonstrujący prawidłowe zastosowanie wytycznych, w tym przypadki brzegowe
    ```

## 10. Kryteria walidacji

[Wymień kryteria lub testy, które muszą być spełnione dla zgodności z tą specyfikacją.]

## 11. Powiązane specyfikacje / Dalsze czytanie

[Link do powiązanej specyfikacji 1]
[Link do istotnej dokumentacji zewnętrznej]

```
