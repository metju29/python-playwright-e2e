def test_login_with_correct_credentials(sauce_demo_without_login_page):
    page = sauce_demo_without_login_page

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."
    page.screenshot(path="screenshot_1.png", full_page=True)


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
    page.screenshot(path="screenshot_2.png", full_page=True)


"""
Execute commands:
pytest pytest_fw/screenshot_test.py -s -v --headed --screenshot=on
pytest pytest_fw/screenshot_test.py -s -v --headed --browser=webkit
"""