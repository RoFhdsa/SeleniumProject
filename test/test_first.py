import time

import pytest

from src.Products.ProductSQL import ProductSQL


class TestAuthentication:

    @pytest.mark.parametrize(
        "username, password, result_url", [
            ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
            ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
            ("problem_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),
        ]
    )
    def test_authentication(self, main_page, username, password, result_url):
        assert main_page.check_log_in(username, password) == result_url
        # time.sleep(5)


class TestImage:

    @pytest.mark.parametrize(
        "username, password, result",
        [
            ("problem_user", "secret_sauce", False),
            ("standard_user", "secret_sauce", True),

        ]
    )
    def test_check_products(self, main_page, username, password, result):
        product_page = main_page.check_products(username, password)
        original_product = ProductSQL.get_product()
        for row in product_page:
            # print(f'row in original_product = {row in original_product}')
            # print(f'row= {row}')
            # print(f'result = {result}')
            assert (row in original_product) == result
        # *time.sleep(2)
