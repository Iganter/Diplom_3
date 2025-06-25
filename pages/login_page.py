import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators
from locators.home_page_locators import HomePageLocators
from data import Data


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.loc = LoginPageLocators()

    @allure.step('Авторизация пользователя через UI')
    def login(self, email, password):
        self.click(HomePageLocators.LOGIN_ACCOUNT_BUTTON)
        self.find(self.loc.LOGIN_LABEL)
        self.find(self.loc.EMAIL_INPUT).send_keys(email)
        self.find(self.loc.PASSWORD_INPUT).send_keys(password)
        self.click(self.loc.LOGIN_BUTTON)
        self.wait.until(EC.url_to_be(Data.BASE_URL))
