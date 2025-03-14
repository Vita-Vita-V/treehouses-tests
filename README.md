# Automatizované testy pro Treehouses.cz

Tento projekt obsahuje automatizované testy napsané v Pythonu pomocí frameworku Playwright.

## Instalace
1. Ujistěte se, že máte nainstalovaný Python (doporučená verze: 3.10+).
2. Nainstalujte požadované balíčky:
python -m pytest test_treehouses.py


- `tests/` – Obsahuje jednotlivé testy:
  - `test_page_load.py` – Ověření, že stránka se načte správně.
  - `test_navigation.py` – Test navigačního menu.
  - `test_elements.py` – Test hlavního nadpisu a sekce Kontakt.

