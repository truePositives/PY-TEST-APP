from playwright.sync_api import Page
class dashboard:
    #locators : (can be seperated in a Locator class file (later))
    jobBot_logo = "//span[@class='fs-4']"
    logout_btn = "button.btn.btn-outline-light"

    def __init__(self,page: Page) -> None:
        self.page = page
    
    def get_dashboard_logo(self):
        return self.page.locator(self.jobBot_logo)
    
    def get_logout_btn(self):
        return self.page.locator(self.logout_btn)
    
    def click_logout_btn(self):
        self.get_logout_btn().click()
