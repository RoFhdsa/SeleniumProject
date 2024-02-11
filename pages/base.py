from typing import List

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Base:
    """Предоставляет методы для работы с веб-элементами."""

    def __init__(self, driver):
        self.driver = driver

    def wait_element_located(self,
                             by: By,
                             locator: str,
                             timeout=10
                             ) -> WebElement:
        """
        Ожидает появления веб-элемента на странице.

        :param by: Стратегия поиска элемента.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания элемента в секундах.
        """
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator)))

    def click(self,
              by: By,
              locator: str,
              timeout=10
              ) -> None:
        """
        Нажимает на элемент, предварительно ожидая его кликабельности.

        :param by: Стратегия поиска элемента.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания элемента в секундах.
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator))).click()

    def find_elements(self,
                      by: By,
                      locator: str
                      ) -> List[WebElement]:
        """
        Возвращает список элементов, найденных по локатору.

        :param by: Стратегия поиска элемента.
        :param locator: Локатор элемента.
        """
        return self.driver.find_elements(by, locator)
