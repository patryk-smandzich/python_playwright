import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browswer = await p.chromium.launch(headless=False)
        context = await browswer.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({'width': 1800, 'height': 1200})
        await page.goto("https://demoqa.com/radio-button")

        #page objects
        impressibeRadio = page.locator("#impressiveRadio")
        impressibeRadioCheck = page.locator("[class = text-success]")

        #actions
        await impressibeRadio.check(force=True)
        await page.screenshot(path="screenshots/radio-button.png")

        #assertions
        await impressibeRadio.is_checked() is True
        await expect(impressibeRadioCheck).to_have_text("Impressive")

        await context.tracing.stop(path="logs/traceRadio-button.zip")

        await browswer.close()

asyncio.run(main())