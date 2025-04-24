from config import BASE_URL
from locators.password_recovery_locators import PasswordRecoveryLocators

class PasswordRecoveryPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}reset-password")

    def enter_email(self, email):
        self.driver.find_element(*PasswordRecoveryLocators.EMAIL_INPUT).send_keys(email)

    def click_recover(self):
        self.driver.find_element(*PasswordRecoveryLocators.RECOVER_BUTTON).click()

    def click_show_password(self):
        self.driver.find_element(*PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON).click()

    def get_password_input(self):
        return self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_INPUT)

    def get_focused_password_input(self):
        return self.driver.find_element(*PasswordRecoveryLocators.PASSWORD_INPUT_FOCUSED)
