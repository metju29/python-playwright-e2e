from typing import Generator

import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture(scope="function")
def sauce_demo_page(playwright: Playwright) -> Generator[Page, None, None]:
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    yield page

    context.close()
    browser.close()


@pytest.fixture(scope="function")
def sauce_demo_without_login_page(page: Page) -> Generator[Page, None, None]:
    # page.set_viewport_size({"width": 1536, "height": 474})
    page.goto("https://www.saucedemo.com/")

    yield page

    page.close()
