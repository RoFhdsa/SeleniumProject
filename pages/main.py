from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from  DATA.data_connect import pages_authentication

from pages.mediator import Mediator



class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""

    # category_locator = "//a[text()='{}'][@class]"
    category_locator = "//*[@{}='{}']"

    def check_authentication_field(self) -> True or TimeoutException:
        """Проверка наличия элементов"""
        a = self.wait_element_located(By.XPATH,
                                  self.category_locator.format(
                                      pages_authentication.marker, pages_authentication.title_lgn))
        print(f' visibility_of_all_elements_located  = {a[0] , type(a[0])}')
        return True

    def check_log_in(self, username, password) ->True or TimeoutException:

        self.authentication(username, password)
         # вызываем в медиаторе метод аутентиафикации передвая в него наш логин
         # self.find_element(By.XPATH, self.category_locator.format(
         #                              pages_authentication.marker, pages_authentication.title_lgn), "standard_user")
         # self.find_element(By.XPATH, self.category_locator.format(
         #     pages_authentication.marker, pages_authentication.title_pswrd), "secret_sauce")
         # self.click(By.XPATH,  self.category_locator.format(
         #     pages_authentication.marker, pages_authentication.title_enter))
