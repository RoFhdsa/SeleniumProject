from dataclasses import dataclass

from selenium.webdriver.common.by import By

@dataclass
class ElementLocator:
    by: By
    locator: str

@dataclass
class LoginPageLocators:
    USERNAME_INPUT: ElementLocator = ElementLocator(By.ID, "user-name")
    PASSWORD_INPUT: ElementLocator = ElementLocator(By.ID, "password")
    LOGIN_BUTTON: ElementLocator = ElementLocator(By.ID, "login-button")

