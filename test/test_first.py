import time

import pytest

class TestAuthentication:

    @pytest.mark.parametrize(
        "username, password, result_url", [
             ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
            ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
            ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
        ]
    )
    def test_authentication (self, main_page, username, password, result_url):
        assert main_page.check_log_in(username, password) == result_url
        time.sleep(5)


class TestImage:


    @pytest.mark.parametrize(
        "username, password",
        [
            ("problem_user", "secret_sauce"),
        ]
    )
    def test_check_image (self, main_page, username, password):
        main_page.check_image(username, password)
        time.sleep(5)