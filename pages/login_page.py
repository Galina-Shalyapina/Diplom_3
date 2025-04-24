from config import BASE_URL
from locators.login_page_locators import LoginPageLocators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}login")

    def enter_email(self, email):
        self.driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def click_forgot_password(self):
        self.driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
