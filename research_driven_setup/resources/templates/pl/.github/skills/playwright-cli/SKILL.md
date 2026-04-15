---
name: playwright-cli
description: Automatyzuje interakcje z przeglądarką do testowania stron, wypełniania formularzy, zrzutów ekranu i ekstrakcji danych. Używaj gdy użytkownik potrzebuje nawigować po stronach internetowych, interagować ze stronami, wypełniać formularze, robić zrzuty ekranu, testować aplikacje webowe lub wyodrębniać informacje ze stron.
allowed-tools: Bash(playwright-cli:*)
---

<!-- user-language: pl -->

# Automatyzacja przeglądarki z playwright-cli

## Szybki start

```bash
# otwórz nową przeglądarkę
playwright-cli open
# przejdź do strony
playwright-cli goto https://playwright.dev
# interaguj ze stroną używając referencji ze snapshota
playwright-cli click e15
playwright-cli type "page.click"
playwright-cli press Enter
# zrób zrzut ekranu (rzadko używane, snapshot jest częstszy)
playwright-cli screenshot
# zamknij przeglądarkę
playwright-cli close
```

## Komendy

### Podstawowe

```bash
playwright-cli open
# otwórz i od razu przejdź do strony
playwright-cli open https://example.com/
playwright-cli goto https://playwright.dev
playwright-cli type "zapytanie wyszukiwania"
playwright-cli click e3
playwright-cli dblclick e7
playwright-cli fill e5 "user@example.com"
playwright-cli drag e2 e8
playwright-cli hover e4
playwright-cli select e9 "wartość-opcji"
playwright-cli upload ./dokument.pdf
playwright-cli check e12
playwright-cli uncheck e12
playwright-cli snapshot
playwright-cli snapshot --filename=po-kliknięciu.yaml
playwright-cli eval "document.title"
playwright-cli eval "el => el.textContent" e5
playwright-cli dialog-accept
playwright-cli dialog-accept "tekst potwierdzenia"
playwright-cli dialog-dismiss
playwright-cli resize 1920 1080
playwright-cli close
```

### Nawigacja

```bash
playwright-cli go-back
playwright-cli go-forward
playwright-cli reload
```

### Klawiatura

```bash
playwright-cli press Enter
playwright-cli press ArrowDown
playwright-cli keydown Shift
playwright-cli keyup Shift
```

### Mysz

```bash
playwright-cli mousemove 150 300
playwright-cli mousedown
playwright-cli mousedown right
playwright-cli mouseup
playwright-cli mouseup right
playwright-cli mousewheel 0 100
```

### Zapisywanie

```bash
playwright-cli screenshot
playwright-cli screenshot e5
playwright-cli screenshot --filename=strona.png
playwright-cli pdf --filename=strona.pdf
```

### Karty

```bash
playwright-cli tab-list
playwright-cli tab-new
playwright-cli tab-new https://example.com/strona
playwright-cli tab-close
playwright-cli tab-close 2
playwright-cli tab-select 0
```

### Przechowywanie

```bash
playwright-cli state-save
playwright-cli state-save auth.json
playwright-cli state-load auth.json

# Ciasteczka
playwright-cli cookie-list
playwright-cli cookie-list --domain=example.com
playwright-cli cookie-get session_id
playwright-cli cookie-set session_id abc123
playwright-cli cookie-set session_id abc123 --domain=example.com --httpOnly --secure
playwright-cli cookie-delete session_id
playwright-cli cookie-clear

# LocalStorage
playwright-cli localstorage-list
playwright-cli localstorage-get theme
playwright-cli localstorage-set theme dark
playwright-cli localstorage-delete theme
playwright-cli localstorage-clear

# SessionStorage
playwright-cli sessionstorage-list
playwright-cli sessionstorage-get step
playwright-cli sessionstorage-set step 3
playwright-cli sessionstorage-delete step
playwright-cli sessionstorage-clear
```

### Sieć

```bash
playwright-cli route "**/*.jpg" --status=404
playwright-cli route "https://api.example.com/**" --body='{"mock": true}'
playwright-cli route-list
playwright-cli unroute "**/*.jpg"
playwright-cli unroute
```

### Narzędzia deweloperskie

```bash
playwright-cli console
playwright-cli console warning
playwright-cli network
playwright-cli run-code "async page => await page.context().grantPermissions(['geolocation'])"
playwright-cli tracing-start
playwright-cli tracing-stop
playwright-cli video-start
playwright-cli video-stop video.webm
```

## Parametry otwierania
```bash
# Użyj konkretnej przeglądarki przy tworzeniu sesji
playwright-cli open --browser=chrome
playwright-cli open --browser=firefox
playwright-cli open --browser=webkit
playwright-cli open --browser=msedge
# Połącz z przeglądarką przez rozszerzenie
playwright-cli open --extension

# Użyj trwałego profilu (domyślnie profil jest w pamięci)
playwright-cli open --persistent
# Użyj trwałego profilu z niestandardowym katalogiem
playwright-cli open --profile=/ścieżka/do/profilu

# Uruchom z plikiem konfiguracji
playwright-cli open --config=moja-konfiguracja.json

# Zamknij przeglądarkę
playwright-cli close
# Usuń dane użytkownika dla domyślnej sesji
playwright-cli delete-data
```

## Snapshoty

Po każdej komendzie playwright-cli dostarcza snapshot aktualnego stanu przeglądarki.

```bash
> playwright-cli goto https://example.com
### Strona
- URL strony: https://example.com/
- Tytuł strony: Example Domain
### Snapshot
[Snapshot](.playwright-cli/page-2026-02-14T19-22-42-679Z.yml)
```

Możesz także zrobić snapshot na żądanie za pomocą komendy `playwright-cli snapshot`.

Jeśli nie podano `--filename`, tworzony jest nowy plik snapshota z sygnaturą czasową. Domyślnie używaj automatycznego nazewnictwa, użyj `--filename=` gdy artefakt jest częścią wyniku przepływu pracy.

## Sesje przeglądarki

```bash
# utwórz nową sesję przeglądarki o nazwie "mojasesja" z trwałym profilem
playwright-cli -s=mojasesja open example.com --persistent
# to samo z ręcznie określonym katalogiem profilu (użyj gdy wyraźnie zażądano)
playwright-cli -s=mojasesja open example.com --profile=/ścieżka/do/profilu
playwright-cli -s=mojasesja click e6
playwright-cli -s=mojasesja close  # zatrzymaj nazwaną przeglądarkę
playwright-cli -s=mojasesja delete-data  # usuń dane użytkownika dla trwałej sesji

playwright-cli list
# Zamknij wszystkie przeglądarki
playwright-cli close-all
# Wymuś zamknięcie wszystkich procesów przeglądarki
playwright-cli kill-all
```

## Lokalna instalacja

W niektórych przypadkach użytkownik może chcieć zainstalować playwright-cli lokalnie. Jeśli uruchomienie globalnie dostępnego pliku binarnego `playwright-cli` nie powiedzie się, użyj `npx playwright-cli` do uruchamiania komend. Na przykład:

```bash
npx playwright-cli open https://example.com
npx playwright-cli click e1
```

## Przykład: Przesyłanie formularza

```bash
playwright-cli open https://example.com/form
playwright-cli snapshot

playwright-cli fill e1 "user@example.com"
playwright-cli fill e2 "password123"
playwright-cli click e3
playwright-cli snapshot
playwright-cli close
```

## Przykład: Przepływ pracy z wieloma kartami

```bash
playwright-cli open https://example.com
playwright-cli tab-new https://example.com/other
playwright-cli tab-list
playwright-cli tab-select 0
playwright-cli snapshot
playwright-cli close
```

## Przykład: Debugowanie z narzędziami deweloperskimi

```bash
playwright-cli open https://example.com
playwright-cli click e4
playwright-cli fill e7 "test"
playwright-cli console
playwright-cli network
playwright-cli close
```

```bash
playwright-cli open https://example.com
playwright-cli tracing-start
playwright-cli click e4
playwright-cli fill e7 "test"
playwright-cli tracing-stop
playwright-cli close
```

## Konkretne zadania

* **Mockowanie żądań** [references/request-mocking.md](references/request-mocking.md)
* **Uruchamianie kodu Playwright** [references/running-code.md](references/running-code.md)
* **Zarządzanie sesjami przeglądarki** [references/session-management.md](references/session-management.md)
* **Stan przechowywania (ciasteczka, localStorage)** [references/storage-state.md](references/storage-state.md)
* **Generowanie testów** [references/test-generation.md](references/test-generation.md)
* **Śledzenie** [references/tracing.md](references/tracing.md)
* **Nagrywanie wideo** [references/video-recording.md](references/video-recording.md)
