import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browswer = await p.chromium.launch(headless=False)
        context = await browswer.new_context()
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page = await context.new_page()
        await page.set_viewport_size({'width': 1800, 'height': 1200})
        await page.goto("https://demoqa.com/checkbox")

        await page.check("[class=\"rct-checkbox\"]")
        await page.screenshot(path="screenshots/checkboxes.png")

        await page.is_checked("[class=\"rct-checkbox\"]")
        await expect(page.locator("#result span:first-child")).to_have_text("You have selected :")

        await context.tracing.stop(path="logs/trace.zip")

        await browswer.close()

asyncio.run(main())