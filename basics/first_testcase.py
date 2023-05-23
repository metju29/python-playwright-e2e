from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # Start tracing before creating / navigating a page.
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    page.goto("https://www.google.com/")
    page.get_by_role("button", name="Zaakceptuj wszystko").click()
    page.get_by_role("combobox", name="Szukaj").click()
    page.get_by_role("combobox", name="Szukaj").fill("Playwright")
    page.get_by_role("combobox", name="Szukaj").press("Enter")
    page.get_by_role("link", name="Playwright: Fast and reliable end-to-end testing for modern ... playwright.dev https://playwright.dev").click()

    # Stop tracing and export it into a zip archive.
    context.tracing.stop(path="trace.zip")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

"""
# Playwright inspector
Chrome Devtools -> Console -> Execute command:
playwright.$('text=Google Search')
playwright.$(":nth-match(button, 1)")
playwright.$(":nth-match(:text('Sauce Labs'), 1)")
playwright.$("button:visible")
"""

"""
Execute commands:
playwright codegen https://www.google.com/
playwright codegen https://www.saucedemo.com
playwright codegen https://demoqa.com/sortable
python basics/first_testcase.py
playwright show-trace trace.zip
"""
