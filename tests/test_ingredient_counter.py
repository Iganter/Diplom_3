import allure
from pages.home_page import HomePage


class TestIngredientCounter:

    @allure.title('Увеличение счётчика ингредиента при добавлении в корзину')
    def test_ingredient_counter_increments(self, driver):
        home = HomePage(driver)
        before = home.get_ingredient_counter()
        home.add_ingredient()
        after = home.get_ingredient_counter()
        assert after > before
