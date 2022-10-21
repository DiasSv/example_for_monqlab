import pytest
import time
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.settings_page import SettingsPage


class TestChangeNameFromSettingsPage():

    @pytest.fixture(scope="function", autouse=True)
    def test_setup(self, browser):
        link = "https://app.clockify.me/"
        page = LoginPage(browser, link)
        page.open()
        page.authorization_user()

    def test_user_change_name(self, browser):
        link = "https://app.clockify.me/user/settings"   #Здесь на самом деле долго думал, просто использовать
                                                        # ссылку, или с помощью автотестов после авторизации добираться до нужной страницы
        page = SettingsPage(browser, link)
        page.open()
        page.edit_input_name()
        time.sleep(4)