import pytest
from selenium import webdriver
from DATA.data_connect import URL
from pages.mediator import Mediator
from pages.main import MainPage
# from data.other import Routes
# from data.search import Categories
import time
@pytest.fixture()
def drivers ():
    """инициализация драйвера"""
    driver = webdriver.Chrome()
    driver.get(URL.url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(drivers):
    """Предоставляет объект для работы с главной страницей."""
    return MainPage(drivers)
