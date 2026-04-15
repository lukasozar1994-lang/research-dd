# Playwright E2E Test — [Nazwa funkcjonalności]

## Cel
<!-- Opisz główny cel testowania, np. "Weryfikacja procesu logowania użytkownika" -->

## Kontekst
<!-- Opisz kontekst aplikacji niezbędny do przeprowadzenia testów -->

### Aplikacja
- **URL**: http://localhost:3000
- **Stack**: <!-- np. Next.js, React, Express -->
- **Stan bazy danych**: <!-- np. Użytkownik testowy: test@example.com / hasło123 -->

### Pliki do analizy
<!-- Wskaż kluczowe pliki kodu, które agent powinien przeanalizować -->
- <!-- np. src/pages/login.tsx -->
- <!-- np. src/api/auth.ts -->
- <!-- np. src/components/LoginForm.tsx -->

### Dodatkowe instrukcje
<!-- Opcjonalne instrukcje dla agenta, np. szczególne wymagania lub ograniczenia -->
- Uruchom serwer deweloperski przed testami: `npm run dev`
- Testy prowadź w trybie `--headed` dla lepszej widoczności

---

## Zadania

### Zadanie 1: [Nazwa zadania]

**Kontekst:** <!-- Krótki opis kontekstu zadania -->

**Cel:** <!-- Co dokładnie chcesz przetestować -->

**Dodatkowe instrukcje:**
- <!-- np. Sprawdź walidację formularza dla pustych pól -->
- <!-- np. Zweryfikuj komunikaty błędów -->

---

### Zadanie 2: [Nazwa zadania]

**Kontekst:** <!-- Krótki opis kontekstu zadania -->

**Cel:** <!-- Co dokładnie chcesz przetestować -->

**Dodatkowe instrukcje:**
- <!-- Dodatkowe wskazówki -->

---

## Jak używać tego prompta

### Krok 1 — Wygeneruj scenariusze testowe
Otwórz Copilot Chat i użyj agenta `test-scenario-architect`:
```
@test-scenario-architect Follow #prompt:playwright-e2e-test.prompt.md
```

### Krok 2 — Uruchom testy z agentem Playwright
Po otrzymaniu scenariuszy, użyj agenta `playwright-debug`:
```
@playwright-debug Follow #prompt:playwright-e2e-test.prompt.md
```

> **Uwaga**: Dla bezpieczeństwa kodu, pracuj w osobnym branchu lub piaskownicy,
> szczególnie w trybie -yolo, gdzie agent może modyfikować pliki w pętli self-healing.
