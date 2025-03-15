 Testování webové stránky Tree Houses pomocí Playwright

Požadavky
- Python 3.7+
- Playwright
- pytest

Instalace závislostí
Nejdříve nainstalujte potřebné knihovny:
```sh
pip install pytest-playwright
playwright install
```

 Spuštění testů
Testy lze spustit příkazem:
```sh
pytest test_treehouses.py
``nebo
`python -m pytest test_treehouses.py

## Popis testů
Tento testovací skript obsahuje následující testy:
1. test_page_loads – Ověřuje, že stránka má titulek.
2. test_main_heading – Kontroluje, zda je hlavní nadpis viditelný.
3. test_contact_info – Ověřuje, že sekce s kontaktními informacemi je viditelná.
4. test_navigation_menu – Kontroluje, zda je navigační menu viditelné.
5. test_footer_exists – Ověřuje, že patička stránky je viditelná.
