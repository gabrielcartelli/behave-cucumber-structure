from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPageLocator(object):
    TITLE_LOGIN = (By.CSS_SELECTOR, '#login .header .title')


class LoginPage(BasePage):
    def get_title_login(self):
        return self.get_text(*LoginPageLocator.TITLE_LOGIN)
