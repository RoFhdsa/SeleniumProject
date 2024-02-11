from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from DATA.data_connect import pages_authentication
from pages.base import Base

from DATA.data_connect import pages_authentication

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
    pass

    # def add_favorites_first_advt(self):
    #     """Добавляет первое в списке объявление в избранное."""
    #     self.get_element_by_attribute(ElementAttributes.marker, "favorites-add").click()
    #     return self
