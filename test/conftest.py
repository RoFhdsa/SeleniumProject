import pytest
from selenium import webdriver


from src.Products.ProductSQL import ProductSQL
from src.db import Base, syns_engine
from src.Products import models_product
from DATA.data_test import URL
from pages.main import MainPage
from src.Products.product_data import Products

@pytest.fixture(scope='session', autouse=True)
def create_tables ():
    Base.metadata.drop_all(syns_engine)
    Base.metadata.create_all(syns_engine)
    p = Products()
    ProductSQL.insert_data(p.product)

@pytest.fixture()
def drivers():

    """инициализация драйвера"""
    driver = webdriver.Chrome()
    driver.get(URL.url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(drivers):
    """Предоставляет объект для работы с главной страницей."""
    return MainPage(drivers)
