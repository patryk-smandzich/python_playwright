from playwright.sync_api import sync_playwright
from pageObjects.SearchPage import SearchPage

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("Mik Mak")
    page.screenshot(path="screenshots/pom.png")
    print(page.title())
    browser.close()
    