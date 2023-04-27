from behave import *
from functions import get_code


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def get_codeTest(context):
    get_code('https://ticapsoriginal.com/static/sitemaps2.xml')


@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
