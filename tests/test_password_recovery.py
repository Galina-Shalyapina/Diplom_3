import allure
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage

@allure.feature('Восстановление пароля')
class TestPasswordRecovery:
    @allure.step('Переход на страницу восстановления пароля')
    def test_navigate_to_password_recovery(self, browser):
        login_page = LoginPage(browser)
        with allure.step('Открыть страницу логина'):
            login_page.open()
        with allure.step('Кликнуть "Забыли пароль?"'):
            login_page.click_forgot_password()
        with allure.step('Проверить url восстановления пароля'):
            assert 'forgot-password' in browser.current_url

    @allure.step('Отправка email для восстановления пароля')
    def test_password_recovery_submit(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открыть страницу восстановления пароля'):
            recovery_page.open()
        with allure.step('Ввести email'):
            recovery_page.enter_email('testuser@example.com')
        with allure.step('Кликнуть "Восстановить"'):
            recovery_page.click_recover()
        with allure.step('Проверить появление поля для нового пароля'):
            password_input = recovery_page.get_password_input()
            assert password_input.is_displayed(), "Поле для ввода пароля не отображается после восстановления"

    @allure.step('Показать пароль и выделить поле')
    def test_show_password_highlights_field(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step('Открыть страницу восстановления пароля'):
            recovery_page.open()
        with allure.step('Ввести email'):
            recovery_page.enter_email('testuser@example.com')
        with allure.step('Кликнуть "Восстановить"'):
            recovery_page.click_recover()
        with allure.step('Кликнуть "Показать пароль"'):
            recovery_page.click_show_password()
        with allure.step('Проверить, что поле выделено'):
            password_input = recovery_page.get_focused_password_input()
            assert 'focused' in password_input.get_attribute('class')
