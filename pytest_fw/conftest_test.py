import pytest


@pytest.mark.browser_context
def test_login_with_correct_credentials(sauce_demo_without_login_page):
    page = sauce_demo_without_login_page

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."


@pytest.mark.browser_context
def test_login_with_incorrect_credentials(sauce_demo_without_login_page):
    page = sauce_demo_without_login_page

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    error_text = page.locator("//div[@class=\"error-message-container error\"]/h3")
    error_text.wait_for()
    expected_error_text = "Username and password do not match any user in this service"
    assert expected_error_text in error_text.inner_text(), "Correct error message is not displayed."


def test_logout(sauce_demo_page):
    page = sauce_demo_page

    # Logout
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    login_button = page.locator("#login-button")

    assert login_button.is_visible(), "User is unable to logout."


"""
Execute commands:
pytest -s -v
pytest -s -v -m sanity
pytest -s -v -m regression
pytest -s -v -m "not sanity"
pytest -s -v -m "sanity and regression"
pytest pytest_fw/conftest_test.py -s -v --headed --browser=webkit
pytest pytest_fw/conftest_test.py -s -v --headed --browser=webkit --browser=chromium
pytest pytest_fw/conftest_test.py -s -v --headed --browser-channel=chromium
pytest pytest_fw/conftest_test.py -s -v -m browser_context --headed --device="iPhone 8"
pytest pytest_fw/conftest_test.py -s -v -m browser_context --headed --device="iPhone 8" --browser=webkit
"""
