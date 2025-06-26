from selenium.webdriver.common.by import By


class OrdersFeedPageLocators:
    COUNTER_ALL_TIME = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )
    COUNTER_TODAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )
    IN_PROGRESS_LIST = (
        By.XPATH,
        "//*[contains(@class,'_orderListReady')]/li[contains(@class,'digits')]"
    )
