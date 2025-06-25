from pages.home_page import HomePage


def test_ingredient_popup_open_close(driver):
    home = HomePage(driver)
    assert home.is_popup_open() is False

    home.click_ingredient()
    assert home.is_popup_open() is True
    assert home.get_popup_ingredient_name() != ""
    home.close_popup()

    assert home.is_popup_open() is False
