import allure
from pages.login_page import LoginPage
from pages.password_recovery_page import PasswordRecoveryPage
from locators.password_recovery_locators import PasswordRecoveryLocators


@allure.feature("Восстановление пароля")
class TestPasswordRecovery:
    @allure.title(
        'Переход на страницу восстановления пароля по ссылке "Забыли пароль?"'
    )
    def test_navigate_to_password_recovery(self, browser):
        login_page = LoginPage(browser)
        with allure.step("Открыть страницу логина"):
            login_page.open()
        with allure.step('Кликнуть "Забыли пароль?"'):
            login_page.click_forgot_password()
            login_page.wait_for_url_to_contain("forgot-password")
        with allure.step("Проверить url страницы восстановления пароля"):
            assert "forgot-password" in login_page.get_current_url()

    @allure.title("Ввод email и отправка формы восстановления пароля")
    def test_password_recovery_submit(self, browser):
        recovery_page = PasswordRecoveryPage(browser)
        with allure.step("Открыть страницу восстановления пароля (где вводится email)"):
            recovery_page.open()
        with allure.step("Ввести email"):
            recovery_page.enter_email("testuser@example.com")
        with allure.step('Кликнуть "Восстановить"'):
            recovery_page.click_recover()

        with allure.step("Проверить появление поля для нового пароля"):
            recovery_page.wait_for_element_visibility(
                PasswordRecoveryLocators.PASSWORD_INPUT, timeout=10
            )
            password_input = recovery_page.get_password_input()
            assert (
                password_input.is_displayed()
            ), "Поле для ввода пароля не отображается после восстановления"

    @allure.title('Клик по иконке "показать пароль" делает поле пароля активным')
    def test_show_password_highlights_field(self, browser):
        recovery_page = PasswordRecoveryPage(browser)

        with allure.step(
            "Открыть страницу сброса/восстановления пароля и инициировать появление поля для нового пароля"
        ):
            recovery_page.open()
            recovery_page.enter_email("testuser@example.com")
            recovery_page.click_recover()
            recovery_page.wait_for_element_visibility(
                PasswordRecoveryLocators.PASSWORD_INPUT, timeout=10
            )
            recovery_page.wait_for_element_visibility(
                PasswordRecoveryLocators.SHOW_PASSWORD_BUTTON, timeout=5
            )

        with allure.step('Кликнуть "Показать пароль"'):
            recovery_page.click_show_password()
            recovery_page.wait_for_condition(
                lambda drv: "focused"
                in recovery_page.get_attribute(
                    PasswordRecoveryLocators.PASSWORD_INPUT_FOCUSED, "class"
                ),
                timeout=5,
            )

        with allure.step("Проверить, что поле ввода пароля выделено"):
            password_field_element = recovery_page.get_focused_password_input()
            class_attribute = password_field_element.get_attribute("class")
            assert (
                "focused" in class_attribute
            ), f"Поле пароля не содержит класс 'focused'. Текущие классы: '{class_attribute}'"
