from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."

    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()

    assert login_button.is_visible(), "User is unable to logout."

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

"""
Execute commands:
python basics/sauce_demo.py
"""
