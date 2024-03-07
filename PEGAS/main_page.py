import time

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from DATA.data_test import PegaAuthentication as pa, PegaCatalog as pc, PegaBasket as pb
from PEGAS.mediator import Mediator


class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""
    category_locator = "//*[@{}='{}']"

    def check_log_in(self, username, password) ->str:
        return self.authenticate (username, password)

    def check_products(self, username, password) -> str:
        """ПРОВЕРКА НАЛИЧИЯ ТОВАРОВ НА СТРАНИЦЕ КАТАЛОГА"""
        with allure.step(f"Логин под пользователем {username}"):
            self.authenticate(username, password)
            product_page = self.get_products_with_page_catalogs(pc.locator_xpath_products)
            screenshot_product_page = self.create_screenshot(username)
            allure.attach.file(screenshot_product_page, attachment_type=allure.attachment_type.PNG)
            return product_page

    def buy_products (self, username, password, products_choices) -> str:
        with allure.step(f"Логин под пользователем {username}"):
            self.check_log_in(username, password)
        names_products_choices = [row.get('name') for row in products_choices]
        self.add_product_to_basket (names_products_choices, pc.locator_xpath_products)
        # перейти в корзину, сверить продукт, ктоорый был заявлен с тем, который был куплен
        self.click(by=By.XPATH, locator='//*[@id="shopping_cart_container"]/a')
        product_page = self.get_products_basket(pb.locator_xpath_products)

        #products = self.get_all_elements(By.CSS_SELECTOR, pc.locator_product)
        #product_choice = [element for element in products if element.text.lower() == product_name['name'].lower()][0]
        #print(f' product_choice = {product_choice, type (product_choice), product_choice.text}')
        # button = product_choice.find_element(By.XPATH,
        #button = self.click(By.CSS_SELECTOR,
         #                                      'button.btn.btn_primary.btn_small.btn_inventory')

        #print(f' button = {button}')
        # выбрать 4 проудкта и добавив их в корзину
        # проверить, что 4 проудкта выбраны и добавлены в корзину (значок корзины)
        # перейти в корзину
        # проверить, что выбраны те продукты, которые были куплены
        # оформить заказ
        # дойти до конечной формы
        # product_page = self.get_products_with_page_catalogs()
        # screenshot = self.create_screenshot(username)
        # allure.attach.file(screenshot, attachment_type=allure.attachment_type.PNG)
        #
        # allure.attach.file(screenshot, attachment_type=allure.attachment_type.PNG)
        # print(f'product_page ={product_page}')
        # return product_page
