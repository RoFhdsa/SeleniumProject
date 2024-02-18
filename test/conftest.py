from datetime import datetime
from os import mkdir

import pytest
from selenium import webdriver


from src.Products.ProductSQL import ProductSQL
from src.db import Base, syns_engine
from src.Products import models_product
from DATA.data_test import URL
from PEGAS.main_page import MainPage
from src.Products.product_data import Products

@pytest.fixture(scope='session', autouse=True)
def create_tables ():
    """Подключенеи к БД"""
    print(f' Подключаюсь к базе')
    Base.metadata.drop_all(syns_engine)
    Base.metadata.create_all(syns_engine)
    print(f' Создаю таблицу и импортирую в не данные')
    p = Products()
    ProductSQL.insert_data(p.product)
    print(f'Завершил работы')

@pytest.fixture(scope='session')
def clear_DB (syns_engine):
    """Очистка СУБД"""
    print(f'Очищаю данные в базе')
    yield Base.metadata.drop_all(syns_engine)
    print(f'Очищаю данные в базе')


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

