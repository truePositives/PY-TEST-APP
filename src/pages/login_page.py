from playwright.sync_api import Page
from .dashboard_page import dashboard

class login:
    #locators : (can be seperated in a Locator class file (later))
    _email = "input[name=email]"
    _password = "input[type=password]"
    _login_btn = "button[type=submit]"

    def __init__(self,page: Page):
        self.page = page

    def email_locator(self):
        return self.page.locator(self._email)
    
    def pass_locator(self):
        return self.page.locator(self._email)

    def login_btn_locator(self):
        return self.page.locator(self._login_btn)
    
    # Actions
    
    def fill_email(self,email: str):
        self.email_locator().fill(email)

    def fill_password(self,password: str):
        self.email_locator().fill(password)
    
    def click_login_btn(self):
        self.login_btn_locator().click()
    
    ## Workflows 
    def do_login(self, creds: dict):
        email, password = creds['email'], creds['pass']
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_btn()

        return dashboard(self.page)
    