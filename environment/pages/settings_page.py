import random, string
from .base_page import BasePage
from .locators import SettingsPageLocators
from selenium.webdriver.support.ui import WebDriverWait


class SettingsPage(BasePage):

    def edit_input_name(self):
        name = ''.join(random.choice(string.ascii_letters) for i in range(10)) #рандомное имя, чтобы не возвращаться
        # к подбору данных
        self.should_be_input_name_to_be_clickable()
        input_name = self.browser.find_element(*SettingsPageLocators.INPUT_NAME)
        input_name.click()
        input_name.clear()
        input_name.send_keys(name) # Здесь можно например сделать тест в виде конструкции if|else и убрать
                                        # данные например куда нибудь в атрибуты, не писать каждый раз, подтягивать откуда нибудь
        self.click_actions(*SettingsPageLocators.STR_NAME)
        self.should_be_successfully_message()

    def should_be_input_name_to_be_clickable(self):
        assert self.is_element_to_be_clickable(*SettingsPageLocators.INPUT_NAME), "input name is not clickable" #
        # проверяет кликабельность интересующего нас поля

    def should_be_successfully_message(self):
        self.is_element_present(*SettingsPageLocators.SUCCESSFULLY_MESSAGE)
        suc_mess = self.browser.find_element(*SettingsPageLocators.SUCCESSFULLY_MESSAGE)
        assert suc_mess.text == "Settings successfully saved", "DISAPPEARED SUCCESSFULLY MESSAGE"

