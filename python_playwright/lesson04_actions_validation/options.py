import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browswer = await p.chromium.launch(headless=False)
        context = await browswer.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({'width': 1800, 'height': 1200})
        await page.goto("https://demoqa.com/select-menu")

        #page objects
        multiSelect = page.locator("#cars")

        #actions
        await multiSelect.select_option(['volvo', 'audi'])
        await page.screenshot(path="screenshots/options.png")

        await context.tracing.stop(path="logs/traceOptions.zip")

        await browswer.close()

asyncio.run(main())