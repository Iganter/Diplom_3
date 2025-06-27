import allure
from pages.home_page import HomePage


class TestIngredientPopup:

    @allure.title('Открытие и закрытие попапа с деталями ингредиента')
    def test_ingredient_popup_open_close(self, driver):
        home = HomePage(driver)
        assert home.is_popup_open() is False

        home.click_ingredient()
        assert home.is_popup_open() is True
        assert home.get_popup_ingredient_name() != ""

        home.close_popup()
        assert home.is_popup_open() is False
