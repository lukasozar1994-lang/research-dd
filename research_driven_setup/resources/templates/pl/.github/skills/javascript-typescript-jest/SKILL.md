---
name: javascript-typescript-jest
description: 'Najlepsze praktyki pisania testów JavaScript/TypeScript przy użyciu Jest, w tym strategie mockowania, struktura testów i typowe wzorce.'
---

<!-- user-language: pl -->

### Struktura testów
- Nazywaj pliki testowe z sufiksem `.test.ts` lub `.test.js`
- Umieszczaj pliki testowe obok testowanego kodu lub w dedykowanym katalogu `__tests__`
- Używaj opisowych nazw testów, które wyjaśniają oczekiwane zachowanie
- Używaj zagnieżdżonych bloków describe do organizacji powiązanych testów
- Stosuj wzorzec: `describe('Komponent/Funkcja/Klasa', () => { it('powinien coś robić', () => {}) })`

### Skuteczne mockowanie
- Mockuj zewnętrzne zależności (API, bazy danych itp.) aby izolować testy
- Używaj `jest.mock()` dla mocków na poziomie modułu
- Używaj `jest.spyOn()` dla mocków konkretnych funkcji
- Używaj `mockImplementation()` lub `mockReturnValue()` aby zdefiniować zachowanie mocka
- Resetuj mocki między testami za pomocą `jest.resetAllMocks()` w `afterEach`

### Testowanie kodu asynchronicznego
- Zawsze zwracaj promisy lub używaj składni async/await w testach
- Używaj matcherów `resolves`/`rejects` dla promisów
- Ustawiaj odpowiednie limity czasu dla wolnych testów za pomocą `jest.setTimeout()`

### Testowanie snapshotowe
- Używaj testów snapshotowych dla komponentów UI lub złożonych obiektów, które rzadko się zmieniają
- Utrzymuj snapshoty małe i skoncentrowane
- Dokładnie przeglądaj zmiany snapshotów przed commitem

### Testowanie komponentów React
- Używaj React Testing Library zamiast Enzyme do testowania komponentów
- Testuj zachowanie użytkownika i dostępność komponentów
- Szukaj elementów po rolach dostępności, etykietach lub treści tekstowej
- Używaj `userEvent` zamiast `fireEvent` dla bardziej realistycznych interakcji użytkownika

## Typowe matchery Jest
- Podstawowe: `expect(wartość).toBe(oczekiwane)`, `expect(wartość).toEqual(oczekiwane)`
- Prawdziwość: `expect(wartość).toBeTruthy()`, `expect(wartość).toBeFalsy()`
- Liczby: `expect(wartość).toBeGreaterThan(3)`, `expect(wartość).toBeLessThanOrEqual(3)`
- Łańcuchy: `expect(wartość).toMatch(/wzorzec/)`, `expect(wartość).toContain('podłańcuch')`
- Tablice: `expect(tablica).toContain(element)`, `expect(tablica).toHaveLength(3)`
- Obiekty: `expect(obiekt).toHaveProperty('klucz', wartość)`
- Wyjątki: `expect(fn).toThrow()`, `expect(fn).toThrow(Error)`
- Funkcje mock: `expect(mockFn).toHaveBeenCalled()`, `expect(mockFn).toHaveBeenCalledWith(arg1, arg2)`
