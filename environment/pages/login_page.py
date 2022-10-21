import time

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def authorization_user(self):
        email = "dima.sveshnikov.81@mail.ru"
        password = "Rfrniyg12345%"
        email_input = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        password_input = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD)
        self.is_url_present()
        self.is_title_correct("Log In")
        self.should_be_login_url()
        self.should_be_login_link()
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)
        password_input.click()
        password_input.clear()
        password_input.send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        self.should_be_authorized_user()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL LOGIN IS NOT FOUNDED"  # наличие строки "логин" в url страницы

    def should_be_login_link(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_BUTTON), "Login link is not presented"  # Проверка есть ли на странице
                                                                                                # кнопка авторизации

    def should_be_authorized_user(self):
        assert self.is_element_present(*LoginPageLocators.AVATAR_ICON), "User icon is not presented," \
                                                                        " probably unauthorised user"  # Показывает успешна ли авторизация

