from playwright.sync_api import Playwright


def test_navigation_example(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://www.google.com/")
    print(f"\n" + page.url)
    page.get_by_role("button", name="Accept all").click()
    page.get_by_role("link", name="Gmail (opens a new tab)").click()
    print(page.url)
    page.go_back()
    print(page.url)
    page.go_forward(wait_until="networkidle")
    print(page.url)

    context.close()
    browser.close()


"""
Execute commands:
pytest playwright_fw/navigation_test.py -s -v
"""