from playwright.sync_api import Playwright


def test_successful_login(the_intern_page) -> None:
    page = the_intern_page

    subheader_text = page.locator(".subheader").inner_text()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."
    assert expected_text in subheader_text

    page.close()


def test_successful_logout(the_intern_page) -> None:
    page = the_intern_page

    subheader_text = page.locator(".subheader").inner_text()
    expected_text = "Welcome to the Secure Area. When you are done click logout below."
    assert expected_text in subheader_text

    page.get_by_role("link", name="Logout").click()
    flash_message = page.locator("[class=\"flash success\"]")
    success_message_logout = "You logged out of the secure area!"
    assert success_message_logout in flash_message.inner_text()

    page.close()


"""
Execute commands:
playwright codegen https://the-internet.herokuapp.com/login
pytest playwright_fw/authentication_test.py -s -v
"""