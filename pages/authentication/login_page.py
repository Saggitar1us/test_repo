import re

from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.shadow_link = page.locator("a:has-text('Powered by Skif.pro')")
        self.email_input = page.locator("input[type='email'], input[name='email'], input[name='login']").first
        self.password_input = page.locator("input[type='password'], input[name='password']").first
        self.submit_button = page.locator("button[type='submit'], button:has-text('Войти'), button:has-text('Login')").first

    def check_visible_text(self):
        expect(self.shadow_link).to_contain_text("Powered by Skif.pro")

    def login(self, username: str, password: str):
        self.email_input.fill(username)
        self.password_input.fill(password)
        self.submit_button.click()

    def assert_logged_in(self):
        expect(self.page).not_to_have_url(re.compile(r"login|auth", re.IGNORECASE))
        expect(self.password_input).to_have_count(0)
