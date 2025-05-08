import allure
from config import BASE_URL
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открытие страницы входа")
    def open(self):
        self.open_url(f"{BASE_URL}login")

    @allure.step("Ввод email: {email}")
    def enter_email(self, email):
        self.send_keys(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Ввод пароля")
    def enter_password(self, password):
        self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Нажатие кнопки 'Войти'")
    def click_login(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Нажатие ссылки 'Забыли пароль?'")
    def click_forgot_password(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)
