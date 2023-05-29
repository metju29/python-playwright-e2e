import pytest


@pytest.mark.parametrize("username", ["standard_user",
                                      pytest.param("locked_out_user", marks=pytest.mark.xfail),
                                      "problem_user",
                                      "performance_glitch_user"])
class TestClass1:
    @pytest.mark.parametrize("password", ["secret_sauce",
                                          pytest.param("wrong-password", marks=pytest.mark.xfail)])
    def test_login_1(self, sauce_demo_without_login_page, username, password):
        page = sauce_demo_without_login_page

        page.locator("#user-name").fill(username)
        page.locator("#password").fill(password)
        login_button = page.locator("#login-button")
        login_button.click()

        products_header = page.locator("//span[text()=\"Products\"]")
        assert products_header.is_visible(), "User is unable to login."


@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce"),
                                                pytest.param("locked_out_user", "secret_sauce",
                                                             marks=pytest.mark.xfail),
                                                pytest.param("problem_user", "secret_sauce",
                                                             marks=pytest.mark.xfail),
                                                ("performance_glitch_user", "secret_sauce")])
def test_login_2(sauce_demo_without_login_page, username, password):
    page = sauce_demo_without_login_page

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)
    login_button = page.locator("#login-button")
    login_button.click()

    products_header = page.locator("//span[text()=\"Products\"]")
    assert products_header.is_visible(), "User is unable to login."


"""
Execute commands:
pytest pytest_fw/parametrize_test.py -s -v --headed --capture=tee-sys
"""