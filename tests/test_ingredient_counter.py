from pages.home_page import HomePage


def test_ingredient_counter_increments(driver):
    home = HomePage(driver)
    before = home.get_ingredient_counter()
    home.add_ingredient()
    after = home.get_ingredient_counter()
    assert after > before
