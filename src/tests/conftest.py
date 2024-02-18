import os
from dotenv import load_dotenv
load_dotenv()
from playwright.sync_api import Playwright
import pytest

@pytest.fixture(scope="class")
def setup_teardown(playwright: Playwright):
    try:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(os.getenv('URL'))
        yield page
        page.close()
        context.close()
    except Exception as e:
        print(f"Error in Browser Fixture: {e}")


