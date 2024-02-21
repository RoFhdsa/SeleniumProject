import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PEGAS.base import Base

from DATA.data_test import PegaAuthentication as pa, PegaCatalog as pg

class Mediator(Base):
    def get_element_by_attribute(self, attribute_name: str, attribute_value: str) -> WebElement:
        """
                вернет элемент по его атрибуту
        :param attribute_name:
        :param attribute_value:
        """
        element_by_attribute = f"//*[@{attribute_name}='{attribute_value}']"
        print(f'element_by_attribute = {element_by_attribute}')
        return self.wait_element_located(locator=element_by_attribute, timeout=10)

    def get_products (self) -> list:

        elements = self.get_all_elements(By.XPATH, self.category_locator.format(pg.marker,
                                                                                pg.title_inventory) + pg.add_title_inventory)
        products = []
        for element in elements:
            product = Product (
                name= element.find_element(By.CLASS_NAME,
                                                   'inventory_item_name') , # Получаем название товара,
                price= element.find_element(By.CLASS_NAME, 'inventory_item_price'),  # Получаем цену товара,
                image= element.find_element(By.CLASS_NAME, 'inventory_item_img')
                            .find_element(By.TAG_NAME,'img').get_attribute('src'),  # Получаем атрибут 'src' картинки
                button_buy=element.find_element (By.CSS_SELECTOR, 'button.btn.btn_primary.btn_small.btn_inventory'),
                description=element.find_element(By.CLASS_NAME, 'inventory_item_desc'),
            )
            products.append(product)
        return products

    def authenticate (self, username: str, password: str)  -> str:
        self.find_input_field(By.XPATH, self.category_locator.format(
            pa.marker, pa.title_lgn), username)
        self.find_input_field(By.XPATH, self.category_locator.format(
            pa.marker, pa.title_pswrd), password)
        self.click(By.XPATH, self.category_locator.format(
            pa.marker, pa.title_enter))
        try:
            find_err_text = self.find_element(By.XPATH,
                                     self.category_locator.format(pa.marker,
                                                                    pa.title_enter_err) + pa.additional_locator_error)
            return find_err_text.text
        except:
            return self.return_actual_url()

    def get_products_with_page_catalogs (self, ) -> list:
        element_data = []
        products = self.get_products()
        for product in products:
            product_d = {}
            product_d['name'] = product.name.text
            product_d['price'] = product.price.text
            product_d['image'] = product.image
            element_data.append(product_d)
        return element_data

    def add_product_to_basket (self, name_choice_product) -> list:
        products_page = self.get_products()
        product_choice = [product for product in products_page if product.name.text.lower() == name_choice_product.lower()]
        print(f' product_choice = {product_choice[0].name.text}')
        print(f' name_choice_product = {name_choice_product}')
        r = product_choice[0].button_buy.click()
        time.sleep(6)




class Product ():

    def __init__(self,name, price, image, button_buy, description):
        self.name = name
        self.price = price
        self.image = image
        self.button_buy = button_buy
        self.description = description