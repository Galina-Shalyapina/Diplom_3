import allure
from pages.profile_page import ProfilePage

from locators.profile_page_locators import ProfilePageLocators


@allure.feature("Личный кабинет")
class TestProfile:
    @allure.title('Переход в личный кабинет по клику на кнопку "Личный кабинет"')
    def test_navigate_to_profile(self, browser, login):
        profile_page = ProfilePage(browser)

        with allure.step('Клик по кнопке "Личный кабинет" (для перехода в профиль)'):
            profile_page.click_profile()
            profile_page.wait_for_url_to_contain("/account")
        with allure.step("Проверить URL личного кабинета"):
            assert "/account" in profile_page.get_current_url()

    @allure.title('Переход в раздел "История заказов" из личного кабинета')
    def test_navigate_to_order_history(self, browser, login):
        profile_page = ProfilePage(browser)

        with allure.step("Перейти в основной раздел личного кабинета"):
            profile_page.click_profile()
            profile_page.wait_for_url_to_contain("/account", timeout=5)
            profile_page.wait_for_element_visibility(
                ProfilePageLocators.ORDER_HISTORY_TAB
            )

        with allure.step('Клик по вкладке "История заказов"'):
            profile_page.click_order_history()
            profile_page.wait_for_url_to_contain("/order-history", timeout=5)

        with allure.step("Проверить URL истории заказов"):
            assert "/order-history" in profile_page.get_current_url()

    @allure.title("Выход из аккаунта")
    def test_logout(self, browser, login):
        profile_page = ProfilePage(browser)

        with allure.step("Перейти в основной раздел личного кабинета"):
            profile_page.click_profile()
            profile_page.wait_for_url_to_contain("/account", timeout=5)
            profile_page.wait_for_element_visibility(ProfilePageLocators.LOGOUT_BUTTON)

        with allure.step('Клик по кнопке "Выход"'):
            profile_page.click_logout()

        with allure.step("Проверить переход на страницу логина (по URL)"):
            profile_page.wait_for_url_to_contain("login", timeout=5)
            assert "login" in profile_page.get_current_url()
