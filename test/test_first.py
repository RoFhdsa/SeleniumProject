import time

import pytest

from DATA.data_connect import pages_authentication

@pytest.mark.parametrize (
"username, password", [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
    ]
)
def test_user_pwd(main_page, username, password):
    # main_page.get_element_by_attribute(pages_authentication.marker, pages_authentication.title)
    # main_page.check_authentication_field()
    main_page.check_log_in(username, password)
    time.sleep(5)
    # main_page.check_categoriescheck_categories(pages_authentication.marker, pages_authentication.title)