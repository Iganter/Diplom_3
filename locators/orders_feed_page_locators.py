from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    COUNTER_ALL_TIME = (
        By.XPATH,
        "//div[p[text()='Выполнено за все время:']]/p[2]"
    )
    COUNTER_TODAY = (
        By.XPATH,
        "//div[p[text()='Выполнено за сегодня:']]/p[2]"
    )
    IN_PROGRESS_LIST = (
        By.XPATH,
        "//*[contains(@class,'_orderListReady')]/li[contains(@class,'digits')]"
    )
