import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage

@pytest.fixture
def login_page(browser_page: Page) -> LoginPage:
    return LoginPage(page=browser_page)
