---
name: create-agentsmd
description: 'Prompt do generowania pliku AGENTS.md dla repozytorium'
---

<!-- user-language: pl -->

# Utwórz wysokiej jakości plik AGENTS.md

Jesteś agentem kodującym. Twoim zadaniem jest utworzenie kompletnego, dokładnego pliku AGENTS.md w katalogu głównym tego repozytorium, zgodnie z publicznymi wytycznymi na https://agents.md/.

AGENTS.md to otwarty format zaprojektowany tak, aby dostarczać agentom kodującym kontekst i instrukcje potrzebne do efektywnej pracy nad projektem.

## Czym jest AGENTS.md?

AGENTS.md to plik Markdown służący jako „README dla agentów" — dedykowane, przewidywalne miejsce dostarczające kontekstu i instrukcji, które pomagają agentom AI kodującym pracować nad Twoim projektem. Uzupełnia README.md, zawierając szczegółowy kontekst techniczny potrzebny agentom, który zaśmiecałby README skierowane do ludzi.

## Kluczowe zasady

- **Skupiony na agentach**: Zawiera szczegółowe instrukcje techniczne dla zautomatyzowanych narzędzi
- **Uzupełnia README.md**: Nie zastępuje ludzkiej dokumentacji, lecz dodaje kontekst specyficzny dla agentów
- **Standardowa lokalizacja**: Umieszczany w katalogu głównym repozytorium (lub katalogach głównych subprojektów w monorepo)
- **Otwarty format**: Używa standardowego Markdown z elastyczną strukturą
- **Kompatybilność z ekosystemem**: Działa z ponad 20 różnymi narzędziami i agentami AI do kodowania

## Struktura pliku i wytyczne dotyczące treści

### 1. Wymagana konfiguracja

- Utwórz plik jako `AGENTS.md` w katalogu głównym repozytorium
- Używaj standardowego formatowania Markdown
- Brak wymaganych pól — elastyczna struktura w zależności od potrzeb projektu

### 2. Istotne sekcje do uwzględnienia

#### Przegląd projektu

- Krótki opis co projekt robi
- Przegląd architektury jeśli złożona
- Kluczowe używane technologie i frameworki

#### Komendy konfiguracji

- Instrukcje instalacji
- Kroki konfiguracji środowiska
- Komendy zarządzania zależnościami
- Konfiguracja bazy danych jeśli dotyczy

#### Przepływ pracy deweloperskiej

- Jak uruchomić serwer deweloperski
- Komendy budowania
- Konfiguracja watch/hot-reload
- Specyfika menedżera pakietów (npm, pnpm, yarn itd.)

#### Instrukcje testowania

- Jak uruchamiać testy (jednostkowe, integracyjne, e2e)
- Lokalizacje plików testowych i konwencje nazewnictwa
- Wymagania pokrycia
- Konkretne wzorce testowe lub używane frameworki
- Jak uruchomić podzbiór testów lub skupić się na konkretnych obszarach

#### Wytyczne stylu kodu

- Konwencje specyficzne dla języka
- Zasady lintowania i formatowania
- Wzorce organizacji plików
- Konwencje nazewnictwa
- Wzorce import/export

#### Budowanie i wdrażanie

- Komendy budowania i ich wyniki
- Konfiguracje środowisk
- Kroki i wymagania wdrożenia
- Informacje o pipeline CI/CD

### 3. Opcjonalne ale rekomendowane sekcje

#### Kwestie bezpieczeństwa

- Wymagania testowania bezpieczeństwa
- Zarządzanie sekretami
- Wzorce uwierzytelniania
- Modele uprawnień

#### Instrukcje dla monorepo (jeśli dotyczy)

- Jak pracować z wieloma pakietami
- Zależności między pakietami
- Selektywne budowanie/testowanie
- Komendy specyficzne dla pakietu

#### Wytyczne pull requestów

- Wymagania formatu tytułu
- Wymagane kontrole przed wysłaniem
- Proces przeglądu
- Konwencje wiadomości commitów

#### Debugowanie i rozwiązywanie problemów

- Typowe problemy i rozwiązania
- Wzorce logowania
- Konfiguracja debugowania
- Kwestie wydajności

## Przykładowy szablon

Użyj go jako szablonu startowego i dostosuj do konkretnego projektu:

```markdown
# AGENTS.md

## Przegląd projektu

[Krótki opis projektu, jego celu i kluczowych technologii]

## Komendy konfiguracji

- Instalacja zależności: `[menedżer pakietów] install`
- Uruchomienie serwera deweloperskiego: `[komenda]`
- Budowanie do produkcji: `[komenda]`

## Przepływ pracy deweloperskiej

- [Instrukcje uruchomienia serwera deweloperskiego]
- [Informacje o hot reload/trybie watch]
- [Konfiguracja zmiennych środowiskowych]

## Instrukcje testowania

- Uruchom wszystkie testy: `[komenda]`
- Uruchom testy jednostkowe: `[komenda]`
- Uruchom testy integracyjne: `[komenda]`
- Pokrycie testowe: `[komenda]`
- [Konkretne wzorce testowe lub wymagania]

## Styl kodu

- [Konwencje języka i frameworka]
- [Zasady lintowania i komendy]
- [Wymagania formatowania]
- [Wzorce organizacji plików]

## Budowanie i wdrażanie

- [Szczegóły procesu budowania]
- [Katalogi wyjściowe]
- [Budowanie specyficzne dla środowiska]
- [Komendy wdrożenia]

## Wytyczne pull requestów

- Format tytułu: [komponent] Krótki opis
- Wymagane kontrole: `[komenda lint]`, `[komenda test]`
- [Wymagania przeglądu]

## Dodatkowe uwagi

- [Kontekst specyficzny dla projektu]
- [Typowe pułapki lub wskazówki dotyczące rozwiązywania problemów]
- [Kwestie wydajności]
```

## Działający przykład z agents.md

Oto prawdziwy przykład ze strony agents.md:

```markdown
# Przykładowy plik AGENTS.md

## Wskazówki dotyczące środowiska deweloperskiego

- Użyj `pnpm dlx turbo run where <nazwa_projektu>` aby przejść do pakietu zamiast skanować za pomocą `ls`.
- Uruchom `pnpm install --filter <nazwa_projektu>` aby dodać pakiet do workspace, tak aby Vite, ESLint i TypeScript mogły go widzieć.
- Użyj `pnpm create vite@latest <nazwa_projektu> -- --template react-ts` aby uruchomić nowy pakiet React + Vite z gotowymi kontrolami TypeScript.
- Sprawdź pole name w package.json każdego pakietu aby potwierdzić poprawną nazwę — pomiń główny.

## Instrukcje testowania

- Znajdź plan CI w folderze .github/workflows.
- Uruchom `pnpm turbo run test --filter <nazwa_projektu>` aby uruchomić każdą kontrolę zdefiniowaną dla tego pakietu.
- Z katalogu głównego pakietu możesz po prostu wywołać `pnpm test`. Commit powinien przejść wszystkie testy przed scaleniem.
- Aby skupić się na jednym kroku, dodaj wzorzec Vitest: `pnpm vitest run -t "<nazwa testu>"`.
- Napraw wszelkie błędy testów lub typów dopóki cały zestaw nie będzie zielony.
- Po przeniesieniu plików lub zmianie importów, uruchom `pnpm lint --filter <nazwa_projektu>` aby upewnić się że zasady ESLint i TypeScript wciąż przechodzą.
- Dodaj lub zaktualizuj testy dla zmienianego kodu, nawet jeśli nikt o to nie prosił.

## Instrukcje PR

- Format tytułu: [<nazwa_projektu>] <Tytuł>
- Zawsze uruchom `pnpm lint` i `pnpm test` przed commitem.
```

## Kroki implementacji

1. **Przeanalizuj strukturę projektu** aby zrozumieć:

   - Używane języki programowania i frameworki
   - Menedżery pakietów i narzędzia budowania
   - Frameworki testowe
   - Architekturę projektu (monorepo, pojedynczy pakiet itd.)

2. **Zidentyfikuj kluczowe przepływy pracy** badając:

   - Skrypty package.json
   - Makefile lub inne pliki budowania
   - Pliki konfiguracji CI/CD
   - Pliki dokumentacji

3. **Utwórz kompleksowe sekcje** obejmujące:

   - Wszystkie istotne komendy konfiguracji i deweloperskie
   - Strategie testowania i komendy
   - Styl kodu i konwencje
   - Procesy budowania i wdrażania

4. **Dołącz konkretne, wykonywalne komendy** które agenci mogą uruchomić bezpośrednio

5. **Przetestuj instrukcje** upewniając się że wszystkie komendy działają jak udokumentowano

6. **Zachowaj skupienie** na tym co agenci muszą wiedzieć, nie na ogólnych informacjach o projekcie

## Najlepsze praktyki

- **Bądź konkretny**: Podawaj dokładne komendy, nie niejasne opisy
- **Używaj bloków kodu**: Otaczaj komendy tyldami dla jasności
- **Dołączaj kontekst**: Wyjaśniaj dlaczego pewne kroki są potrzebne
- **Utrzymuj aktualność**: Aktualizuj w miarę ewolucji projektu
- **Testuj komendy**: Upewnij się że wszystkie wymienione komendy rzeczywiście działają
- **Rozważ zagnieżdżone pliki**: Dla monorepo twórz pliki AGENTS.md w podprojektach w razie potrzeby

## Kwestie monorepo

Dla dużych monorepo:

- Umieść główny AGENTS.md w katalogu głównym repozytorium
- Utwórz dodatkowe pliki AGENTS.md w katalogach subprojektów
- Najbliższy plik AGENTS.md ma priorytet dla danej lokalizacji
- Dołącz wskazówki nawigacji między pakietami/projektami

## Uwagi końcowe

- AGENTS.md działa z ponad 20 narzędziami AI do kodowania w tym Cursor, Aider, Gemini CLI i wieloma innymi
- Format jest celowo elastyczny — dostosuj go do potrzeb projektu
- Skup się na wykonalnych instrukcjach pomagających agentom zrozumieć i pracować z bazą kodu
- To żywa dokumentacja — aktualizuj ją w miarę ewolucji projektu

Tworząc plik AGENTS.md, priorytetyzuj jasność, kompletność i wykonalność. Celem jest dostarczenie każdemu agentowi kodującemu wystarczającego kontekstu do efektywnego wkładu w projekt bez wymagania dodatkowego ludzkiego wsparcia.
