import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LOADING_ANIMATION = (By.XPATH, "//*[@alt='loading animation']/parent::div")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ждём, пока исчезнет загрузочный спиннер")
    def wait_loading(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADING_ANIMATION))

    @allure.step("Находим элемент по локатору: {locator}")
    def find(self, locator):
        self.wait_loading()
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Находим все элементы по локатору: {locator}")
    def finds(self, locator):
        self.wait_loading()
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator):
        self.wait_loading()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return element

    @allure.step("Получаем текст элемента: {locator}")
    def get_text(self, locator):
        self.wait_loading()
        return self.find(locator).text

    @allure.step("Проверяем наличие элемента на странице: {locator}")
    def is_present(self, locator):
        return bool(self.driver.find_elements(*locator))
