import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browswer = await p.chromium.launch(headless=False)
        context = await browswer.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({'width': 1800, 'height': 1200})
        await page.goto("https://demoqa.com/buttons")

        #page objects
        doubleClickMe = page.locator("#doubleClickBtn")
        rightClickMe = page.locator("#rightClickBtn")
        clickMe = page.locator("text=Click Me").nth(2)
        doubleClickMeCheck = page.locator("#doubleClickMessage")
        rightClickMeCheck  = page.locator("#rightClickMessage")
        clickMeCheck  = page.locator("#dynamicClickMessage")

        #actions
        await clickMe.click()
        await rightClickMe.click(button='right')
        await doubleClickMe.dblclick()
        await page.screenshot(path="screenshots/buttons.png")

        #assertions
        await expect(clickMeCheck).to_have_text("You have done a dynamic click")
        await expect(rightClickMeCheck).to_have_text("You have done a right click")
        await expect(doubleClickMeCheck).to_have_text("You have done a double click")

        await context.tracing.stop(path="logs/traceClicks.zip")

        await browswer.close()

asyncio.run(main())