<!-- user-language: pl -->

# Instrukcje dla agenta GitHub Copilot

## Środowisko

Pracujesz w środowisku **Ubuntu 24.04 LTS**. Wszystkie operacje systemowe powinny być zgodne z najlepszymi praktykami Ubuntu.

## Obsługa projektów Python

### Wymagania dotyczące środowiska wirtualnego (venv)

**KRYTYCZNE:** Dla KAŻDEGO projektu Python w tym workspace:

1. **Zawsze sprawdź najpierw istniejące venv**
   - Szukaj katalogów `venv/`, `.venv/` lub `env/` w katalogu głównym projektu
   - Sprawdź czy `pyvenv.cfg` istnieje w katalogu projektu

2. **Utwórz venv jeśli brakuje**
   - Jeśli nie istnieje środowisko wirtualne, utwórz je poleceniem:
     ```bash
     python3 -m venv venv
     ```
   - Lub dla konkretnej wersji Pythona:
     ```bash
     python3.12 -m venv venv
     ```

3. **Aktywuj venv przed WSZYSTKIMI operacjami Python**
   - Zawsze aktywuj środowisko wirtualne przed uruchomieniem komend Pythona:
     ```bash
     source venv/bin/activate
     ```
   - Dotyczy to:
     - Instalowania pakietów przez `pip`
     - Uruchamiania skryptów Python
     - Wykonywania `pip install -r requirements.txt`
     - Uruchamiania serwerów deweloperskich

4. **Instaluj wszystkie pakiety Python w venv**
   - NIGDY nie instaluj pakietów Python globalnie
   - ZAWSZE instaluj w środowisku wirtualnym
   - Użyj `pip install <pakiet>` po aktywacji venv
   - Dla wymagań: `pip install -r requirements.txt`

5. **Zweryfikuj instalację**
   - Po zainstalowaniu pakietów zweryfikuj poleceniem:
     ```bash
     pip list
     python -c "import <nazwa_pakietu>"
     ```
