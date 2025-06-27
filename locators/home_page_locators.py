from selenium.webdriver.common.by import By


class HomePageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, '//button[text() = "Войти в аккаунт"]')
    INGREDIENT_TILES = (By.XPATH, "//a[contains(@class,'BurgerIngredient_ingredient')]")
    INGREDIENT_COUNTERS = (By.XPATH, "//*[contains(@class,'counter_counter__num')]")
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    POPUP_WINDOW = (By.XPATH, "//*[contains(@class,'Modal_modal_opened')]")
    POPUP_CLOSE_BUTTON = (By.XPATH, "//*[contains(@class,'Modal_modal_opened')]//button")
    POPUP_INGREDIENT_NAME = (
        By.XPATH,
        "//*[contains(@class,'Modal_modal_opened')]/div/div/p"
    )
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
