import time

import allure
from pages.main_page import MainPage


@allure.feature('Основной функционал')
class TestMainFunctionality:
    @allure.step('Переход к разделу Конструктор через ленту заказов')
    def test_navigate_to_constructor(self, browser):
        main_page = MainPage(browser)
        with allure.step('Открыть главную страницу'):
            main_page.open()
        with allure.step('Перейти в ленту заказов'):
            main_page.click_order_feed()
            assert 'feed' in browser.current_url
        with allure.step('Вернуться в конструктор'):
            main_page.click_constructor()
            burger_text = main_page.get_burger_text()
            assert burger_text.is_displayed()

    @allure.step('Переход к ленте заказов')
    def test_navigate_to_order_feed(self, browser):
        main_page = MainPage(browser)
        with allure.step('Открыть главную страницу'):
            main_page.open()
        with allure.step('Перейти в ленту заказов'):
            main_page.click_order_feed()
            assert 'feed' in browser.current_url

    @allure.step('Открытие модального окна ингредиента')
    def test_ingredient_modal_opens(self, browser):
        main_page = MainPage(browser)
        with allure.step('Открыть главную страницу'):
            main_page.open()
        with allure.step('Кликнуть по ингредиенту'):
            main_page.click_ingredient()
            assert main_page.is_modal_open(), "Модальное окно не открылось!"

    @allure.step('Закрытие модального окна ингредиента')
    def test_ingredient_modal_closes(self, browser):
        main_page = MainPage(browser)
        with allure.step('Открыть главную страницу'):
            main_page.open()
        with allure.step('Кликнуть по ингредиенту'):
            main_page.click_ingredient()
        with allure.step('Закрыть модальное окно'):
            main_page.close_modal()
            assert main_page.is_modal_closed(timeout=3), "Модальное окно не закрылось!"

    @allure.step('Проверка увеличения счетчика ингредиентов')
    def test_ingredient_counter_increases(self, browser):
        main_page = MainPage(browser)
        with allure.step('Открыть главную страницу'):
            main_page.open()
        with allure.step('Получить значение счетчика до добавления'):
            counter_before = int(main_page.get_ingredient_counter().text)
        with allure.step('Перетащить ингредиент в конструктор'):
            main_page.drag_and_drop_ingredient_to_constructor()
        with allure.step('Получить значение счетчика после добавления'):
            counter_after = int(main_page.get_ingredient_counter().text)
            time.sleep(2)
            assert counter_after == counter_before + 2 # 2 ингредиента (булочки) добавляются в конструктор

    @allure.step('Авторизованный пользователь может оформить заказ')
    def test_logged_in_user_can_order(self, browser, user, login):
        main_page = MainPage(browser)
        with allure.step('Перетащить ингредиенты в конструктор'):
            main_page.drag_and_drop_ingredient_to_constructor()
        with allure.step('Оформить заказ'):
            main_page.click_order_button()
            order_number = main_page.get_order_number()
            assert order_number.isdigit(), "Номер заказа не отображается!"
            assert "Ваш заказ начали готовить" in browser.page_source, "Сообщение о начале готовки не отображается!"
