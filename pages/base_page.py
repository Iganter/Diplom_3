from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LOADING_ANIMATION = (By.XPATH, "//*[@alt='loading animation']/parent::div")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_loading(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADING_ANIMATION))

    def find(self, locator):
        self.wait_loading()
        return self.wait.until(EC.visibility_of_element_located(locator))

    def finds(self, locator):
        self.wait_loading()
        return self.wait.until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        self.wait_loading()
        element = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()
        return element

    def get_text(self, locator):
        self.wait_loading()
        return self.find(locator).text

    def is_present(self, locator):
        return bool(self.driver.find_elements(*locator))
