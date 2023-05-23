def test_login_with_correct_credentials(set_up):
    page = set_up

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."

def test_logout(set_up):
    page = set_up

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    login_button = page.locator("#login-button")
    login_button.click()

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
"""
