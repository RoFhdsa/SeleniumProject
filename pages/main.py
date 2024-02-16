from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from  DATA.data_test import PegaElements as pe, PegaAuthentication as pa
from src.Products.ProductSQL import ProductSQL
from pages.mediator import Mediator



class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""

    # category_locator = "//a[text()='{}'][@class]"
    category_locator = "//*[@{}='{}']"

    def check_authentication_field(self) -> True or TimeoutException:
        """Проверка наличия элементов"""
        a = self.wait_element_located(By.XPATH,
                                      self.category_locator.format(
                                      pa.marker, pa.title_lgn))
        print(f' visibility_of_all_elements_located  = {a[0] , type(a[0])}')
        return True

    def check_log_in(self, username, password) ->True or TimeoutException:
        return self.authenticate (username, password)

    def check_products(self, username, password) -> True or TimeoutException:
        self.authenticate(username, password)
        product_page = self.get_elements()
        print(f'product_page ={product_page}')
        return product_page
