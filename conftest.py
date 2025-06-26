import pytest
from selenium import webdriver

from pages.login_page import LoginPage
from data import Data
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    if browser == "firefox":
        drv = webdriver.Firefox()
    else:
        drv = webdriver.Chrome()
    drv.set_window_size(1920, 1080)
    try:
        drv.get(Urls.BASE_URL)
        LoginPage(drv).login(Data.EMAIL, Data.PASSWORD)
        yield drv
    finally:
        drv.quit()
