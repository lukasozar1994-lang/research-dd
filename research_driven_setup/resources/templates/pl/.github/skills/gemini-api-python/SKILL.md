---
name: gemini-api-python
description: 'Zbadaj aktualne oficjalne Google GenAI SDK dla Pythona, określ poprawną bibliotekę Gemini API i kroki instalacji, oraz wygeneruj aktualne przykłady dla generowania tekstu, streamingu, czatu, wejścia multimodalnego, strukturyzowanego wyniku, plików, użycia asynchronicznego i wywoływania funkcji.'
---

<!-- user-language: pl -->

# Badanie Gemini API Python

## Cel

Używaj tego skilla, gdy użytkownik pyta, której biblioteki Pythona użyć do Gemini API lub jak poprawnie korzystać z aktualnego SDK Pythona.

Celem jest wygenerowanie aktualnej, opartej na źródłach odpowiedzi bazującej na najnowszej oficjalnej dokumentacji Google, a nie na pamięci lub starszych przykładach.

## Zasady bezwzględne

- Preferuj oficjalne źródła Google na pierwszym miejscu: strony bibliotek, quickstart, generowanie tekstu, wywoływanie funkcji, strukturyzowany wynik, przetwarzanie dokumentów/plików, myślenie, migracja i dziennik zmian.
- Traktuj `google-genai` jako domyślny SDK Pythona dla Gemini API.
- Wspominaj o `google-generativeai` tylko jako o starszym pakiecie w kontekście migracji.
- Weryfikuj, że przykłady używają aktualnej formy SDK, zwłaszcza `from google import genai` i `genai.Client()`.
- Nie wymyślaj nazw modeli, kroków autoryzacji ani obsługi funkcji, które nie są pokazane w aktualnej dokumentacji.
- Jeśli strony dokumentacji się nie zgadzają lub funkcja jest w wersji podglądowej, zaznacz to jawnie.

## Przepływ pracy badawczej

1. Potwierdź intencję użytkownika.
   - Czy użytkownik prosi o szybki start, pełny przewodnik integracji, pomoc w migracji, czy przykład specyficzny dla funkcji?
2. Sprawdź aktualną oficjalną dokumentację.
   - Strona bibliotek dla nazwy pakietu i komendy instalacyjnej.
   - Quickstart dla autoryzacji i pierwszego żądania.
   - Generowanie tekstu dla przykładów podstawowych, streamingu, czatu i konfiguracji.
   - Wywoływanie funkcji dla deklaracji narzędzi i przepływu wywołań/odpowiedzi.
   - Strukturyzowany wynik i przetwarzanie dokumentów/plików, jeśli to istotne.
   - Strony migracji i dziennika zmian dla zmian łamiących lub notatek o starszych pakietach.
3. Wyodrębnij aktualną kanoniczną składnię.
   - Komenda instalacyjna.
   - Styl importu.
   - Tworzenie klienta.
   - Wzorce żądań synchronicznych i asynchronicznych.
   - Opcjonalne wzorce konfiguracji.
4. Buduj przykłady wyłącznie ze zweryfikowanej dokumentacji.
   - Utrzymuj przykłady małe i bezpośrednio uruchamialne.
   - Preferuj najprostszy kod demonstrujący żądaną funkcję.
5. Jasno określaj zastrzeżenia i aktualność.
   - Wspominaj daty aktualizacji dokumentacji, gdy są dostępne.
   - Rozróżniaj stabilne zachowanie od eksperymentalnego zachowania w wersji podglądowej.

## Kanoniczne wzorce Python

Używaj tych wzorców jako domyślnego punktu wyjścia, gdy są obsługiwane przez aktualną dokumentację:

- `from google import genai`
- `from google.genai import types`
- `client = genai.Client()`
- `client.models.generate_content(...)`
- `client.models.generate_content_stream(...)`
- `client.chats.create(...)`
- `client.aio.models.generate_content(...)` dla przepływów asynchronicznych
- `types.GenerateContentConfig(...)` dla ustawień generowania
- `types.Tool(...)` i `types.FunctionDeclaration(...)` dla wywoływania funkcji

## Struktura wyniku

Odpowiadając, wygeneruj zwięzły brief badawczy z tymi sekcjami:

1. Rekomendowana biblioteka
2. Instalacja
3. Autoryzacja
4. Minimalny działający przykład
5. Istotne zaawansowane przykłady
6. Notatki o migracji
7. Zastrzeżenia i ostrzeżenia wersji
8. Aktualność źródeł

## Wskazówki specyficzne dla funkcji

### Generowanie tekstu

- Pokaż `client.models.generate_content(...)` najpierw.
- Dołącz `response.text` w ścieżce wyniku przykładu.
- Jeśli użytkownik chce konfiguracji, pokaż `types.GenerateContentConfig`.

### Streaming

- Użyj `client.models.generate_content_stream(...)`.
- Iteruj po fragmentach i wypisuj `chunk.text`.

### Czat

- Użyj `client.chats.create(...)`.
- Pokaż `send_message(...)` i `get_history()` gdy stan konwersacji ma znaczenie.

### Asynchroniczne

- Użyj `client.aio...` dla żądań asynchronicznych.
- Wspomnij, że async jest przydatny gdy wywołująca aplikacja już korzysta z pętli zdarzeń.

### Wejście multimodalne

- Pokaż listy treści łączące tekst z obiektami obrazów lub plików.
- Wspominaj o stronach dokumentów, obrazów, wideo i audio tylko gdy użytkownik pyta o te modalności.

### Strukturyzowany wynik

- Wyjaśnij jak ograniczyć format odpowiedzi gdy użytkownik potrzebuje wyniku w formacie JSON lub ze schematu.
- Utrzymuj przykład zgodny z aktualną dokumentacją zamiast zgadywać nazwy parametrów.

### Wywoływanie funkcji

- Pokaż deklarację narzędzia, konfigurację narzędzia, żądanie, inspekcję wywołania funkcji, wykonanie funkcji i roundtrip odpowiedzi funkcji.
- Jeśli użytkownik potrzebuje ręcznej obsługi, wspomnij o przepływie `id` wywołania funkcji dla odpowiedzi w stylu Gemini 3.
- Jeśli użytkownik chce prostszego doświadczenia Python, wspomnij, że automatyczne wywoływanie funkcji jest dostępne w SDK Pythona, gdy dokumentacja to potwierdza.

## Wskazówki migracyjne

- Jeśli użytkownik przechodzi z `google-generativeai`, wyjaśnij ścieżkę migracji do `google-genai`.
- Podkreśl wszelkie luki w funkcjach, przestarzałe zachowania lub usuniętą składnię.
- Jasno zaznacz, że nowy SDK jest oficjalną aktualną ścieżką, chyba że dokumentacja mówi inaczej.

## Lista kontrolna weryfikacji

Przed sfinalizowaniem odpowiedzi potwierdź wszystkie poniższe:

- Nazwa pakietu jest zgodna z aktualną stroną bibliotek.
- Komenda instalacyjna jest zgodna ze stroną quickstart lub bibliotek.
- Styl importu jest zgodny z aktualną dokumentacją.
- Przykład kodu działa z udokumentowanym klientem i metodami.
- Wszelkie zachowania w wersji podglądowej lub specyficzne dla modelu są oznaczone.
- Wszelkie wskazówki dotyczące starszych wersji są jasno oddzielone od rekomendowanej ścieżki.

## Przykładowe prompty obsługiwane przez ten skill

- Której biblioteki Pythona powinienem teraz użyć do Gemini API?
- Pokaż mi aktualny quickstart Gemini Python.
- Jak streamować odpowiedzi Gemini w Pythonie?
- Jak wywołać Gemini z Pythona z wywoływaniem funkcji?
- Co się zmieniło z `google-generativeai` na `google-genai`?

## Wskaźniki źródeł

- Strona bibliotek Gemini API
- Quickstart Gemini API
- Przewodnik generowania tekstu Gemini API
- Przewodnik wywoływania funkcji Gemini API
- Przewodnik strukturyzowanego wyniku Gemini API
- Przewodnik migracji Gemini API
