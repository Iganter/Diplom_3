from selenium.webdriver.common.by import By


class HeaderPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "(//a[@href='/'])[1]")
    ORDERS_FEED_BUTTON = (By.XPATH, "(//a[@href='/feed'])[1]")
    ACTIVE_TAB = (By.CSS_SELECTOR, "a[aria-current='page'] p")
