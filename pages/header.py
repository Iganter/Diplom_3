import allure
from pages.base_page import BasePage
from locators.header_locators import HeaderPageLocators


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.loc = HeaderPageLocators()

    @allure.step('Переход на Конструктор')
    def go_to_constructor(self):
        self.click(self.loc.CONSTRUCTOR_BUTTON)

    @allure.step('Переход на Ленту заказов')
    def go_to_feed(self):
        self.click(self.loc.ORDERS_FEED_BUTTON)

    @allure.step('Получаем текст активного таба')
    def get_active_tab_text(self):
        return self.get_text(self.loc.ACTIVE_TAB)
