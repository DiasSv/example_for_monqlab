from selenium.webdriver.common.by import By


class BasePageLocators():
    pass


class LoginPageLocators():
    AVATAR_ICON = (By.XPATH, "//avatar")
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]|//button[contains(text(), " Log In ")]')
    INPUT_EMAIL = (By.CSS_SELECTOR, 'input#email')
    INPUT_PASSWORD = (By.CSS_SELECTOR, 'input#password')


class MainPageLocators():
    PROFILE_SETTINGS = (By.XPATH, '//div//a[@routerlink="/user/settings"]')


class SettingsPageLocators:
    INPUT_NAME = (By.XPATH, '//div//label[contains(text(),"Name")]/following-sibling::input')
    SUCCESSFULLY_MESSAGE = (By.XPATH, '//div[@id="toast-container"]//div[@aria-label="Settings successfully saved"]')
    STR_NAME = (By.XPATH, '//div//label[contains(text(),"Name")]')
