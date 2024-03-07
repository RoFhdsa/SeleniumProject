import os
import secrets
import string
from datetime import datetime
from telnetlib import EC

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Base:
    """Предоставляет методы для работы с веб-элементами."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_for_element(self, by: By, locator: str, timeout=10):
        """Ожидает появления элемента на странице."""
        try:
            element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            return element
        except TimeoutException:
            raise TimeoutException(
                f"Элемент с локатором '{locator}' по средствам '{by}' не был найден за {timeout} секунд")

    def click(self, by: By, locator: str, timeout=10):
        """Выполняет клик по элементу."""
        element = self.wait_for_element(by, locator, timeout)
        element.click()

    def find_element(self, by: By, locator: str):
        """Находит элемент на странице."""
        return self.driver.find_element(by, locator)

    def find_elements(self, by: By, locator: str):
        """Находит все элементы на странице."""
        return self.driver.find_elements(by, locator)

    def scroll_into_view(self, element):
        """Прокручивает страницу так, чтобы элемент был виден."""
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # Методы для работы с URL и создания скриншотов
    def return_actual_url(self):
        """Возвращает текущий URL страницы."""
        return self.driver.current_url

    def create_screenshot(self, name_screenshot: str) -> str:
        """
        Создает скриншот страницы.

        :param name_screenshot: Имя скриншота.
        :return: Путь к созданному скриншоту.
        """
        alph = string.digits + string.ascii_uppercase
        id = ''.join(secrets.choice(alph) for r in range(32))
        path = f'{self.create_dir()}{os.path.sep}{name_screenshot}{id}.png'
        self.driver.get_screenshot_as_file(path)
        return path

    @staticmethod
    def create_dir() -> str:
        """
        Создает директорию для сохранения логов и скриншотов.

        :return: Путь к созданной директории.
        """
        path = f'logs_files{os.path.sep}{datetime.now().strftime("%Y-%m-%d")}'
        os.makedirs(path, exist_ok=True)
        return path

    # Остальные методы класса Base...
