---
name: context-map
description: 'Wygeneruj mapę wszystkich plików istotnych dla zadania przed wprowadzaniem zmian'
---

<!-- user-language: pl -->

# Mapa kontekstu

Przed implementacją jakichkolwiek zmian przeanalizuj bazę kodu i utwórz mapę kontekstu.

## Zadanie

{{task_description}}

## Instrukcje

1. Przeszukaj bazę kodu w poszukiwaniu plików związanych z tym zadaniem
2. Zidentyfikuj bezpośrednie zależności (importy/eksporty)
3. Znajdź powiązane testy
4. Poszukaj podobnych wzorców w istniejącym kodzie

## Format wyjściowy

```markdown
## Mapa kontekstu

### Pliki do modyfikacji
| Plik | Cel | Potrzebne zmiany |
|------|-----|------------------|
| ścieżka/do/pliku | opis | jakie zmiany |

### Zależności (mogą wymagać aktualizacji)
| Plik | Relacja |
|------|---------|
| ścieżka/do/zależności | importuje X z modyfikowanego pliku |

### Pliki testowe
| Test | Pokrycie |
|------|----------|
| ścieżka/do/testu | testuje dotkniętą funkcjonalność |

### Wzorce referencyjne
| Plik | Wzorzec |
|------|---------|
| ścieżka/do/podobnego | przykład do naśladowania |

### Ocena ryzyka
- [ ] Zmiany łamiące publiczne API
- [ ] Potrzebne migracje bazy danych
- [ ] Wymagane zmiany konfiguracji
```

Nie przechodź do implementacji dopóki ta mapa nie zostanie przejrzana.
