from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from pages.base import Base

from DATA.data_test import PegaAuthentication as pa, PegaElements as pe

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

    def get_elements (self,) -> list:
        elements =self.get_all_elements(By.XPATH, self.category_locator.format(pe.marker,
                                                                     pe.title_inventory) + pe.add_title_inventory)
        element_data = []
        for element in elements:
            product = {}
            product['name'] = element.find_element(By.CLASS_NAME,
                                                   'inventory_item_name').text  # Получаем название товара
            product['price'] = element.find_element(By.CLASS_NAME, 'inventory_item_price').text  # Получаем цену товара
            product['image'] = element.find_element(By.CLASS_NAME, 'inventory_item_img').find_element(By.TAG_NAME,
                                                                                                      'img').get_attribute(
                'src')  # Получаем атрибут 'src' картинки
            element_data.append(product)

        return element_data
    # def processing_elements(self, elements, dict_locator):
    #     search_value = {}
    #     for locator, values in dict_locator.items():
    #         {
    #
    #         }[locator]
    #     for element in elements:
    #
    #             search_value ['name'] = element.find_element(By.CLASS_NAME,
    #                                                'inventory_item_name').text
    #     pass
