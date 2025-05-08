import allure
from config import BASE_URL
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step("Прямое открытие страницы профиля")
    def open(self):
        self.open_url(f"{BASE_URL}profile")

    @allure.step("Нажатие кнопки/ссылки 'Профиль'")
    def click_profile(self):
        self.click(ProfilePageLocators.PROFILE_BUTTON)

    @allure.step("Нажатие вкладки 'История заказов' в профиле")
    def click_order_history(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_TAB)

    @allure.step("Нажатие кнопки 'Выход' и ожидание страницы входа")
    def click_logout(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)
        self.wait_for_element_presence(LoginPageLocators.LOGIN_BUTTON)
