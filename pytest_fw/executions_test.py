from playwright.sync_api import Playwright


def test_login_with_valid_credentials(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."

    # ---------------------
    context.close()
    browser.close()

def test_broken_1(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name-wrong").fill("standard_user")

    # ---------------------
    context.close()
    browser.close()

def test_broken_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name-wrong").fill("standard_user")

    # ---------------------
    context.close()
    browser.close()

def test_broken_3(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name-wrong").fill("standard_user")

    # ---------------------
    context.close()
    browser.close()

def test_logout(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    # Logout
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    login_button = page.locator("#login-button")

    assert login_button.is_visible(), "User is unable to logout."

    # ---------------------
    context.close()
    browser.close()


"""
Execute commands:
pytest pytest_fw/executions_test.py -s --headed
pytest pytest_fw/executions_test.py::test_login_with_valid_credentials -s --headed
"""
"""
Pytest CLI commands:
pytest -s -v -k logout
pytest pytest_fw/executions_test.py -s -v -x
pytest -v --lf
pytest pytest_fw/executions_test.py -s -v --ff
pytest pytest_fw/executions_test.py -s -v --maxfail=2
"""
