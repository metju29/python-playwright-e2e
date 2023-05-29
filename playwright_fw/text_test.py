from playwright.sync_api import Playwright


def test_text_fill(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").fill("username1")
    page.locator("#username").fill("")
    page.locator("#username").fill("tomsmith")

    context.close()
    browser.close()


def test_text_type(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").type("username1", delay=2000)
    page.locator("#username").type("")
    page.locator("#username").type("tomsmith", delay=2000)

    context.close()
    browser.close()


def test_text_clear(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")
    page.locator("#username").type("username1", delay=500)
    page.locator("#username").clear()
    page.locator("#username").type("tomsmith", delay=500)

    context.close()
    browser.close()


def test_text_get(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong-password")
    login_button = page.locator("#login-button")
    login_button.click()
    error_message = page.locator("[data-test=\"error\"]").text_content()
    print(f"\n{error_message}")

    context.close()
    browser.close()


def test_input_value_get(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong-password")
    login_button = page.locator("#login-button")
    login_button.click()
    error_message = page.locator("[data-test=\"error\"]").text_content()
    print(f"\n{error_message}")
    input_value = page.locator("#user-name").input_value()
    print(input_value)

    context.close()
    browser.close()


"""
Execute commands:
pytest playwright_fw/navigation_test.py -s -v
"""