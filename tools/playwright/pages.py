from playwright.sync_api import Playwright, Page
from config import settings

def initialize_playwright_page(
        playwright: Playwright,
        browser_name: str = "chromium"
) -> Page:
    browser_type = getattr(playwright, browser_name, None)
    if browser_type is None:
        raise ValueError(f"Unsupported browser: {browser_name}")

    browser = browser_type.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    yield page

    browser.close()
