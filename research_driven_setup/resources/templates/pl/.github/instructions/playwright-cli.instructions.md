<!-- user-language: pl -->

# Instrukcje dla agenta GitHub Copilot

## Cel
Agent musi wykonywać testy zachowania front-endu w JavaScript/TypeScript wyłącznie za pomocą `playwright-cli` w trybie e2e, gdy projekt zawiera frontend JS.

## Kiedy ta instrukcja obowiązuje
- Repozytorium zawiera frontend JS/TS (np. `frontend/package.json`, `src/app`, `next.config.ts`, `public`, `frontend/src`).
- Zadanie dotyczy testowania funkcji, komponentu lub interakcji użytkownika w przeglądarce.

## Zachowanie agenta
1. Wykryj obecność frontendu JS:
   - sprawdź `frontend/package.json` lub inne katalogi frontendowe.
   - w razie wątpliwości zapytaj: „Czy ten test dotyczy logiki frontendu JavaScript?".

2. Do testów funkcjonalności front-endu używaj `playwright-cli` (nie lokalnych testów jednostkowych), np.:
   - `playwright-cli open http://localhost:3000`
   - `playwright-cli goto http://localhost:3000/path`
   - `playwright-cli click <selektor>`
   - `playwright-cli fill <selektor> "wartość"`
   - `playwright-cli eval "() => document.querySelector('...').textContent"`
   - `playwright-cli snapshot --filename=...`
   - `playwright-cli close`

3. Jeśli `playwright-cli` jest niedostępny:
   - użyj lokalnie: `npx playwright-cli ...`
   - rekomendacje instalacji: `npm i -D @playwright/cli` lub `npm i -D playwright` (w zależności od przypadku).

4. Zawsze podawaj:
   - krok po kroku komendy do uruchomienia w terminalu
   - jakie elementy UI są testowane i jak zweryfikować wyniki (oczekiwany stan, tekst, selektory)
   - ewentualne snapshoty lub jawne asercje `eval`

5. Dla zadań backendowych lub skryptów bez warstwy frontendu JS, nie wymuszaj `playwright-cli` (klasyczne testy API/Python itd.).

## Przykładowy przepływ pracy
1. `npm run dev` (uruchom serwer frontendowy)
2. `playwright-cli open http://localhost:3000`
3. `playwright-cli click button#submit`
4. `playwright-cli fill input#email "test@example.com"`
5. `playwright-cli click button#confirm`
6. `playwright-cli eval "() => document.querySelector('.message').innerText"`
7. zweryfikuj czy wynik jest równy np. `'Operation completed successfully'`
8. `playwright-cli close`

## Komunikaty wyjaśniające w razie wątpliwości
- „To zadanie dotyczy UI + JS; wykonam test e2e za pomocą playwright-cli."
- „Playwright-cli nie jest zainstalowany; sugeruję `npx playwright-cli` lub podaję instrukcje instalacji."
