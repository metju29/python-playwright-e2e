from typing import Generator

import pytest
from playwright.sync_api import Playwright, Page, BrowserContext


@pytest.fixture(scope="session")
def the_intern_context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context(locale="en-GB")
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name=" Login").click()

    page.close()

    yield context

    context.close()
    browser.close()


@pytest.fixture()
def the_intern_page(the_intern_context) -> Generator[Page, None, None]:
    context = the_intern_context
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/secure")

    yield page



