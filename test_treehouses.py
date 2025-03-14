import pytest 
from playwright.sync_api import sync_playwright 
# Funkce pro spuštění Playwright 
# @pytest.fixture(scope="module")
#  def browser():
#  with sync_playwright() as p:
#  browser = p.chromium.launch(headless=False) # Nastavte headless=True pro běh bez GUI 
# yield browser 
# browser.close()
# # Test 1: Ověření, že stránka obsahuje správný titulek
# def test_title(browser):
#  page = browser.new_page()
#  page.goto("https://www.treehouses.cz/")
# 
#\ title = page.title() assert "Treehouses" in title 
# # Očekávaný titulek stránky page.close()
#  # Test 2: Ověření, že hlavní nadpis na domovské stránce je přítomen def test_main_heading(browser):
#  page = browser.new_page()
#  page.goto("https://www.treehouses.cz/") heading = page.locator("h1") assert heading.is_visible(),
#  "Hlavní nadpis není viditelný" page.close()
#  # Test 3: Ověření, že kontakt na stránce obsahuje e-mailovou adresu 
# def test_contact_email(browser):
#  page = browser.new_page() 
# page.goto("https://www.treehouses.cz/")
#  page.locator('text="Kontakt"').click()
#  # Kliknutí na sekci Kontakt email = page.locator("a[href^='mailto:']") assert email.is_visible(), "E-mailová adresa není k dispozici" page.close()

