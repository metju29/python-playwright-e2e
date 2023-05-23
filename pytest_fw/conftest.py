import pytest
from playwright.sync_api import Playwright, Page


# @pytest.fixture(scope="function")
# def set_up(playwright: Playwright):
#     browser = playwright.chromium.launch()
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto("https://www.saucedemo.com/")
#
#     yield page
#
#     context.close()
#     browser.close()

@pytest.fixture(scope="function")
def set_up(page: Page):
    page.goto("https://www.saucedemo.com/")

    yield page
