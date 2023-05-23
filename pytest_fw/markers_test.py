import pytest
from playwright.sync_api import Playwright


@pytest.mark.regression
def test_login_with_correct_credentials(playwright: Playwright) -> None:
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


@pytest.mark.regression
@pytest.mark.xfail(reason="BUG 1767")
def test_login_with_incorrect_credentials(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."

    # ---------------------
    context.close()
    browser.close()


@pytest.mark.regression
@pytest.mark.sanity
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


@pytest.mark.sanity
@pytest.mark.skip(reason="Not implemented.")
def test_shopping_card(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    # Login
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    # Open shopping card
    page.locator("#shopping_cart_container").click()

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
pytest -s -v
pytest -s -v -m sanity
pytest -s -v -m regression
pytest -s -v -m "not sanity"
pytest -s -v -m "sanity and regression"
"""
