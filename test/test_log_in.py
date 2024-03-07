import time
import random

import pytest
import allure
from src.Products.ProductSQL import ProductSQL
from src.Products.product_data import Products


class TestAuthentication:

    @pytest.mark.parametrize(
        "username, password, result_url", [
            ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html")
        ]
    )
    def test_authentication(self, log_in_page, username, password, result_url):
        log_in_page.enter_username (username=username)
        log_in_page.enter_password (password= password)
        log_in_page.click_login_button

        # assert main_page.check_log_in(username, password) == result_url
        # time.sleep(5)
