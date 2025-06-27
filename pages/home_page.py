import allure
from seletools.actions import drag_and_drop
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.loc = HomePageLocators()

    @allure.step('Открываем попап ингредиента #{idx}')
    def click_ingredient(self, idx=0):
        self.click_nth(self.loc.INGREDIENT_TILES, idx)

    @allure.step('Проверяем, открыт ли попап')
    def is_popup_open(self):
        return self.is_present(self.loc.POPUP_WINDOW)

    @allure.step('Получаем название ингредиента в попапе')
    def get_popup_ingredient_name(self):
        return self.get_text(self.loc.POPUP_INGREDIENT_NAME)

    @allure.step('Закрываем попап ингредиента')
    def close_popup(self):
        # теперь простой click по локатору
        self.click(self.loc.POPUP_CLOSE_BUTTON)

    @allure.step('Добавляем ингредиент #{idx} в корзину')
    def add_ingredient(self, idx=0):
        tile = self.finds(self.loc.INGREDIENT_TILES)[idx]
        basket = self.find(self.loc.CONSTRUCTOR_BASKET)
        drag_and_drop(self.driver, tile, basket)

    @allure.step('Нажать кнопку «Оформить заказ»')
    def click_place_order(self):
        self.click(self.loc.ORDER_BUTTON)

    @allure.step('Закрыть окно подтверждения заказа')
    def close_order_popup(self):
        self.click(self.loc.POPUP_CLOSE_BUTTON)

    @allure.step('Получаем значение счётчика ингредиента #{idx}')
    def get_ingredient_counter(self, idx=0):
        return int(self.finds(self.loc.INGREDIENT_COUNTERS)[idx].text)
