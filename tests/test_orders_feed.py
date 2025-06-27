import allure
from pages.home_page import HomePage
from pages.header import HeaderPage
from pages.orders_feed_page import OrdersFeedPage


class TestOrdersFeed:

    @allure.title('Создание заказа: счётчики и раздел «В работе»')
    def test_orders_counters_and_in_progress(self, driver):
        home = HomePage(driver)
        header = HeaderPage(driver)
        feed = OrdersFeedPage(driver)

        header.go_to_feed()
        all_before = feed.get_all_time()
        today_before = feed.get_today()

        header.go_to_constructor()
        home.add_ingredient(0)
        home.click_place_order()
        home.close_order_popup()

        header.go_to_feed()
        all_after = feed.get_all_time()
        today_after = feed.get_today()
        in_progress = feed.get_in_progress()

        assert all_after == all_before + 1
        assert today_after == today_before + 1
        assert len(in_progress) > 0
