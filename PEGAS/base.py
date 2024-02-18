from datetime import datetime
from os import mkdir
import string, secrets
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    """Предоставляет методы для работы с веб-элементами."""

    def __init__(self, driver):
        self.driver = driver

    def get_all_elements(self,
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
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((by, locator)))

    def click(self,
              by: By,
              locator: str,
              timeout=30
              ) -> None:
        """
        Нажимает на элемент, предварительно ожидая его кликабельности.

        :param by: Стратегия поиска элемента.
        :param locator: Локатор элемента.
        :param timeout: Время ожидания элемента в секундах.
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, locator))).click()

    def find_element(self, by: By, locator: str):
        """
        Возвращает список элементов, найденных по локатору.
        :param by: Стратегия поиска элемента.
        :param locator: Локатор элемента.
        """
        print(f'self.driver.find_element(by, locator) = {self.driver.find_element(by, locator)}')
        return self.driver.find_element(by, locator)

    def find_input_field(self, by: By, locator: str, key: str):
        """
        Возвращает список элементов, найденных по локатору.
        :param by: Стратегия поиска элемента.
        :param locator: Локатор элемента.
        """
        element = self.driver.find_element(by, locator)
        element.send_keys(key)

    def return_actual_url(self):
        return self.driver.current_url

    def create_screenshot(self, name_screenshot: str) -> str:
        path = self.create_dir() + name_screenshot + '.png'
        self.driver.get_screenshot_as_file(path)
        return path

    @staticmethod
    def create_dir() -> str:
        dir_data = datetime.date(datetime.today()).strftime('%d-%m-%y')
        try:
            mkdir(dir_data)
        except FileExistsError:
            pass
        alph = string.digits + string.ascii_uppercase
        id = ''.join(secrets.choice(alph) for r in range(32))
        return dir_data + '\\'+id +'_'
