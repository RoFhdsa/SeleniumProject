from selenium.webdriver.common.by import By

from DATA.data_page_login.data_locator import LoginPageLocators
from PEGAS.mediator import Mediator

class LoginPage(Mediator):
    """Класс, описывающий страницу входа"""

    def __init__(self, driver):
        super().__init__(driver)

    def enter_username(self, username):
        """Вводит имя пользователя"""
        print(f' LoginPageLocators.USERNAME_INPUT = {LoginPageLocators.USERNAME_INPUT}')
        print(f' LoginPageLocators.USERNAME_INPUT = {LoginPageLocators.USERNAME_INPUT.by}')
        self.send_information(LoginPageLocators.USERNAME_INPUT.by, LoginPageLocators.USERNAME_INPUT.locator, username)

    def enter_password(self, password):
        """Вводит пароль"""
        
        self.send_information(LoginPageLocators.PASSWORD_INPUT.by, LoginPageLocators.PASSWORD_INPUT.locator, password)

    def click_login_button(self):
        """Нажимает кнопку входа"""
        self.click(LoginPageLocators.LOGIN_BUTTON.by, LoginPageLocators.LOGIN_BUTTON.locator)

