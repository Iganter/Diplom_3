from pages.header import HeaderPage


def test_navigation_constructor_and_feed(driver):
    header = HeaderPage(driver)
    header.go_to_constructor()
    assert header.get_active_tab_text() == "Конструктор"

    header.go_to_feed()
    assert header.get_active_tab_text() == "Лента Заказов"
