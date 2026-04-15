---
name: review-diff
description: 'Użyj gdy implementacja zadania jest ukończona i musisz porównać diff z kryteriami akceptacji, wynikami walidacji i wygenerować ReviewPacket z decyzją accept, retry lub block.'
---

<!-- user-language: pl -->

# Przegląd diff

## Komenda

```bash
node .github/scripts/implement_worker/collect-review-packet.mjs --task-id <TASK-XXX> --acceptance-file <plan-dir>/11_kryteria_akceptacji.md --validation-file <run-dir>/validation-packets/<TASK-XXX>.json --output <run-dir>/review-packets/<TASK-XXX>.json
```

## Zasady decyzyjne

- `accept` tylko gdy walidacja przechodzi i zmienione pliki dają się przypisać do zakresu docelowego.
- `retry` gdy implementacja jest niekompletna, ale możliwa do naprawienia.
- `block` gdy wymagania wstępne, polityka gałęzi lub założenia uruchomieniowe zawodzą.
