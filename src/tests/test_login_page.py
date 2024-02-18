import os
from dotenv import load_dotenv
import pytest
load_dotenv()
from playwright.async_api import expect,Page
from pytest_bdd import given, scenario, then, when, parsers
import asyncio
from ..pages.login_page import login

@scenario('../features/login.feature','Success User Login')
def scenario_name():
    pass

@given('goto login page')
def test_goto_login(setup_teardown):
    page = setup_teardown
    creds= {'email' : os.getenv('EMAIL'), 'pass' : os.getenv('PASS') }
    print(page.title())
    dashboard_page = login(page).do_login(creds=creds)
    page.wait_for_selector("button.btn.btn-outline-light")
    # dashboard_page.click_logout_btn()
    print('success')
    
    

# @when(parsers.parse('user enters valid username {email} and password {password}'))
# async def step_user_enters_valid_credentials(setup_teardown,email, password):
#     # page = setup_teardown
#     # await page
#     pass

# @then('clicks the login button')
# def step_user_clicks_login_button():
#     # Your implementation goes here
#     pass

# @then('the user should be redirected to the dashboard page')
# def step_user_redirected_to_dashboard():
#     # Your implementation goes here
#     pass




