
import time

import pytest
import allure

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

@allure.feature("Проверка продуктовой страницы")
class TestProducts:
    @allure.title("Тест проверки отображения страницы продуктов")
    @allure.description("Проверка отображения страницы продуктов для разных типов пользователей")
    @pytest.mark.parametrize(
        "username, password, result",
        [
            ("problem_user", "secret_sauce", False),
            ("standard_user", "secret_sauce", True),

        ]
    )
    def test_check_products(self, main_page, username, password, result):
        with allure.step(f"Проверка отображения продуктовой страницы для пользователя {username}"):
            product_page = main_page.check_products(username, password)
            original_product = ProductSQL.get_product()
            for row in product_page:
                assert (row in original_product) == result
        if result:
            allure.dynamic.title(f"Успешная проверка продуктовой страницы для {username}")
            allure.dynamic.description(f"Продуктовая страница отображается корректно для пользователя {username}")
        else:
            allure.dynamic.title(f"Неудачная проверка продуктовой страницы для {username}")
            allure.dynamic.description(f"Продуктовая страница не отображается корректно для пользователя {username}")

        # allure.attach.file('screenshot.png', attachment_type=allure.attachment_type.PNG)
        allure.dynamic.severity(allure.severity_level.CRITICAL)
        allure.link("https://jira.example.com/ISSUE-123", name="Related issue")

    # @pytest.mark.parametrize(
    #     "username, password, result",
    #     [
    #         # ("problem_user", "secret_sauce", False),
    #         ("standard_user", "secret_sauce", True),
    #
    #     ]
    # )
    # def test_byu_products(self, username, password, result):
    #     pass
