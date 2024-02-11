from DATA.data_connect import pages_authentication


def test_user_pwd(main_page):
    main_page.get_element_by_attribute(pages_authentication.marker, pages_authentication.title)
    # main_page.check_categoriescheck_categories(pages_authentication.marker, pages_authentication.title)