import allure

@allure.feature('Личный кабинет')
class TestProfile:
    @allure.step('Переход в личный кабинет')
    def test_navigate_to_profile(self, browser, login):
        profile_page = login
        with allure.step('Клик по кнопке профиля'):
            profile_page.click_profile()
        with allure.step('Проверить url'):
            assert '/account' in browser.current_url

    @allure.step('Переход в историю заказов')
    def test_navigate_to_order_history(self, browser, login):
        profile_page = login
        with allure.step('Клик по кнопке профиля'):
            profile_page.click_profile()
        with allure.step('Клик по истории заказов'):
            profile_page.click_order_history()
        with allure.step('Проверить url истории заказов'):
            assert '/account/order-history' in browser.current_url

    @allure.step('Выход из аккаунта')
    def test_logout(self, browser, login):
        profile_page = login
        with allure.step('Клик по кнопке профиля'):
            profile_page.click_profile()
        with allure.step('Клик по кнопке выхода'):
            profile_page.click_logout()
        with allure.step('Проверить переход на страницу логина'):
            assert 'login' in browser.current_url
