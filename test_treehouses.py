import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.treehouses.cz/")
    yield page
    page.close()

def test_page_loads(page):
    assert page.title() != "", "Stránka by měla mít titulek"


def test_main_heading(page):
    heading = page.locator("h1")
    assert heading.is_visible(), "Hlavní nadpis by měl být viditelný"



def test_main_heading(page):
    heading = page.get_by_role("heading", name="Spát v korunách stromů – snít v Tree Houses")
    assert heading.is_visible(), "Hlavní nadpis by měl být viditelný"

def test_contact_info(page):
    contact_section = page.locator("footer").locator("text=Kontakt")
    assert contact_section.is_visible(), "Sekce s kontaktními informacemi by měla být viditelná"

    def test_navigation_menu(page):
        menu = page.locator("nav")
        assert menu.is_visible(), "Navigační menu by mělo být viditelné"


