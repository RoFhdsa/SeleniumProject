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
class pages_authentication:
    """список полей на странице аутентификации"""
    marker: str = "id"
    title_lgn: str = "user-name"
    title_pswrd: str = "password"
    title_enter: str = "login-button"

