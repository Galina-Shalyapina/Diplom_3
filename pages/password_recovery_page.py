import allure
from config import BASE_URL
from locators.password_recovery_locators import PasswordRecoveryLocators
from pages.base_page import BasePage


class PasswordRecoveryPage(BasePage):
    @allure.step("Открытие страницы восстановления пароля")
    def open(self):
        self.open_url(f"{BASE_URL}reset-password")

    @allure.step("Ввод email для восстановления пароля: {email}")
    def enter_email(self, email):
        self.send_keys(PasswordRecoveryLocators.EMAIL_INPUT, email)

    @allure.step("Нажатие кнопки 'Восстановить'")
    def click_recover(self):
        self.click(PasswordRecoveryLocators.RECOVER_BUTTON)

    @allure.step("Нажатие кнопки 'Показать пароль'")
    def click_show_password(self):
        self.click(PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON)

    @allure.step("Получение элемента ввода пароля")
    def get_password_input(self):
        return self.find_element(PasswordRecoveryLocators.PASSWORD_INPUT)

    @allure.step("Получение сфокусированного элемента ввода пароля")
    def get_focused_password_input(self):
        return self.find_element(PasswordRecoveryLocators.PASSWORD_INPUT_FOCUSED)
