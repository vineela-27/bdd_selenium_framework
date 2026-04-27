from behave import given, when, then
from pages.login_page import LoginPage
from utils.logger import get_logger
from datetime import datetime
import os

logger = get_logger("Steps")

@given('user is on login page')
def step_open(context):
    logger.info(f"Test started at {datetime.now()}")
    context.page = LoginPage(context.driver)
    context.page.open()

@when('user enters valid username and password')
def step_valid(context):
    context.page.login(os.getenv("VALID_USERNAME"), os.getenv("VALID_PASSWORD"))

@when('user enters invalid username and password')
def step_invalid(context):
    context.page.login("wrong", "wrong")

@when('clicks on login button')
def step_click(context):
    context.page.click_login()

@then('user should see success message')
def step_success(context):
    assert "You logged into a secure area!" in context.page.get_message()

@then('user should see error message')
def step_error(context):
    assert "Your username is invalid!" in context.page.get_message()
