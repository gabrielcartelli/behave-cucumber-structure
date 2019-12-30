from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HeaderPageLocator(object):
    BUTTON_LOGIN = (By.CSS_SELECTOR, ".main-header-login-content .title")


class HeaderPage(BasePage):
    def click_button_login(self):
        self.click(*HeaderPageLocator.BUTTON_LOGIN)

