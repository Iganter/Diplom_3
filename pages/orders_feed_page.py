import allure
from pages.base_page import BasePage
from locators.orders_feed_page_locators import OrdersFeedPageLocators


class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.loc = OrdersFeedPageLocators()

    @allure.step('Получаем счётчик за всё время')
    def get_all_time(self):
        return int(self.get_text(self.loc.COUNTER_ALL_TIME))

    @allure.step('Получаем счётчик за сегодня')
    def get_today(self):
        return int(self.get_text(self.loc.COUNTER_TODAY))

    @allure.step('Получаем список номеров заказов в работе')
    def get_in_progress(self):
        return [e.text for e in self.finds(self.loc.IN_PROGRESS_LIST)]
