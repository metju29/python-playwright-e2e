from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demoqa.com/sortable")
    page.locator("//div[@id=\"demo-tabpane-list\"]//div[text()=\"One\"]").click(button="right")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

"""
Execute commands:
playwright codegen https://demoqa.com/sortable
python basics/demoqa_site.py
"""
