from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class MainPage(BasePage):
    def go_to_profile_settings(self):
        self.browser.find_element(*LoginPageLocators.AVATAR_ICON).click()
        self.browser.find_element(*MainPageLocators.PROFILE_SETTINGS).click()
        self.should_be_profile_settings_url()

    def should_be_profile_settings_url(self):
        assert "settings" in self.browser.current_url, "URL SETTINGS IS NOT FOUNDED"  # наличие строки "settings" в url
                                                                                                            # страницы