
import time
import random

import pytest
import allure
from src.Products.ProductSQL import ProductSQL
from src.Products.product_data import Products



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

    @pytest.mark.parametrize(
        "username, password, result",
        [
            # ("problem_user", "secret_sauce", False),
            ("standard_user", "secret_sauce", True),

        ]
    )
    def test_byu_products(self, main_page, username, password, result):
        """Тест на приобритение продукта"""

        original_product = ProductSQL.get_product()
        any_product = random.choices (original_product, k=2)
        print(f' any_product = {any_product}')
        main_page.buy_products(username, password, any_product)

        pass
