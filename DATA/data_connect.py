from dataclasses import dataclass, field

@dataclass
class URL:
    """url подключения к сайту"""
    url: str = "https://www.saucedemo.com/"

@dataclass
class Users:
    """список пользователей"""
    standard_user: str = "standard_user"
    locked_out_user: str = "locked_out_user"
    problem_user: str = "problem_user"
    performance_glitch_user: str = "performance_glitch_user"
    error_user: str = "error_user"
    visual_user: str = "visual_user"
    password: str = "secret_sauce"

@dataclass
class PegaAuthentication:
    """список полей на странице аутентификации"""
    marker: str = "id"
    title_lgn: str = "user-name"
    title_pswrd: str = "password"
    title_enter: str = "login-button"
    title_enter_err: str = "login_button_container"
    additional_locator_error: str = '/div/form/div[3]/h3'

@dataclass
class PegaElements:
    """локаторы """
    marker: str = "id"
    title_inventory: str = "inventory_container"
    add_title_inventory: str = '/ div'
    locator_div: dict = field(default_factory= lambda  :
    {'name':'inventory_item_name',
                      'price':'inventory_item_price',
                      'inventory_item_img':'inventory_item_img'})