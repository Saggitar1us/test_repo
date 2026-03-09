import pytest
from playwright.sync_api import Page, Playwright

from config import settings
from tools.playwright.pages import initialize_playwright_page

@pytest.fixture(params=settings.browsers, ids=[browser.value for browser in settings.browsers])
def browser_page(playwright: Playwright, request: pytest.FixtureRequest) -> Page:
    browser_name = request.param.value
    yield from initialize_playwright_page(playwright, browser_name=browser_name)
