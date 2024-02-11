from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

from pages.mediator import Mediator



class MainPage(Mediator):
    """Предоставляет функционал для работы с главной страницей."""

    category_locator = "//a[text()='{}'][@class]"

    def check_categories(self, ) -> True or TimeoutException:
        """Проверка"""
        self.wait_element_located(By.XPATH, self.category_locator.format())
        return True
