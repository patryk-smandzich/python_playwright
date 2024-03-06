from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://en.wikipedia.org/wiki/Playwright_(software)")
    page.screenshot(path="wiki.png")
    browser.close()