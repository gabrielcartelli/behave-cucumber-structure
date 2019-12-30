from behave import *
from nose.tools import assert_equal
import environment as env


@given('que acesso a página da CWI')
def step_impl(context):
    env.base_page().access_page("https://cwi.com.br")


@when('clico no botão de login')
def step_impl(context):
    env.header_page().click_button_login()


@then('devo visualizar página de login')
def step_impl(context):
    assert_equal(env.login_page().get_title_login(), "Login")
