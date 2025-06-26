from selenium.webdriver.common.by import By


class HeaderPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//nav//a[@href='/' and .//p[text()='Конструктор']]")
    ORDERS_FEED_BUTTON = (By.XPATH, "//nav//a[@href='/feed' and .//p[text()='Лента Заказов']]")
    ACTIVE_TAB = (By.CSS_SELECTOR, "a[aria-current='page'] p")
