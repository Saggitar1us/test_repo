import pytest
from pages.authentication.login_page import LoginPage
from config import settings

pytestmark = pytest.mark.skipif(
    not settings.login_username or not settings.login_password,
    reason="Set LOGIN_USERNAME and LOGIN_PASSWORD in .env for login test",
)

@pytest.mark.regression
@pytest.mark.auth
@pytest.mark.smoke
def test_successful_login(login_page: LoginPage):
    login_page.visit(str(settings.base_url))
    login_page.check_visible_text()

    login_page.login(settings.login_username, settings.login_password)
    login_page.assert_logged_in()
