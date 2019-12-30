from browser import Browser
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from pages.base_page import BasePage


def before_all(context):
    context.browser = Browser()


def after_all(context):
    context.browser.browser_quit()


def base_page():
    return BasePage()


def header_page():
    return HeaderPage()


def login_page():
    return LoginPage()
