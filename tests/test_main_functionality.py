import time

import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


@allure.feature("Основной функционал")
class TestMainFunctionality:
    @allure.title('Переход к разделу "Конструктор" через ленту заказов')
    def test_navigate_to_constructor(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            main_page.wait_for_url_to_contain("feed")
            assert "feed" in main_page.get_current_url()
        with allure.step("Вернуться в конструктор"):
            main_page.click_constructor()
            main_page.wait_for_element_visibility(MainPageLocators.BURGER_TEXT)
            burger_text_element = main_page.get_burger_text()
            assert burger_text_element.is_displayed()

    @allure.title("Переход к ленте заказов")
    def test_navigate_to_order_feed(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            main_page.wait_for_url_to_contain("feed")
            assert "feed" in main_page.get_current_url()

    @allure.title("Открытие модального окна ингредиента")
    def test_ingredient_modal_opens(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Кликнуть по ингредиенту"):
            main_page.click_ingredient()
            assert main_page.is_modal_open(), "Модальное окно не открылось!"

    @allure.title("Закрытие модального окна ингредиента")
    def test_ingredient_modal_closes(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Кликнуть по ингредиенту"):
            main_page.click_ingredient()
            main_page.wait_for_element_visibility(MainPageLocators.MODAL_CLOSE_BUTTON)
        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()
            assert main_page.is_modal_closed(timeout=3), "Модальное окно не закрылось!"

    @allure.title(
        "Проверка увеличения счетчика ингредиентов при добавлении в конструктор"
    )
    def test_ingredient_counter_increases(self, browser):
        main_page = MainPage(browser)
        with allure.step("Открыть главную страницу"):
            main_page.open()
        with allure.step("Получить значение счетчика до добавления"):
            main_page.wait_for_element_visibility(MainPageLocators.INGREDIENT_COUNTER)
            counter_before_text = main_page.get_ingredient_counter().text
            counter_before = int(counter_before_text)

        with allure.step("Перетащить ингредиент в конструктор"):
            main_page.drag_and_drop_ingredient_to_constructor()

        expected_counter_value_str = str(
            counter_before + 2
        )  # Булки добавляют 2 к счетчику
        with allure.step(
            f"Ожидание обновления счетчика до значения: {expected_counter_value_str}"
        ):
            main_page.wait_for_condition(
                lambda drv: main_page.get_ingredient_counter().text
                == expected_counter_value_str,
                timeout=5,
            )

        with allure.step("Получить значение счетчика после добавления"):
            counter_after_text = main_page.get_ingredient_counter().text
            counter_after = int(counter_after_text)
            assert (
                counter_after == counter_before + 2
            ), f"Счетчик ингредиентов не увеличился корректно. Ожидалось: {counter_before + 2}, факт: {counter_after}"

    @allure.title("Авторизованный пользователь может оформить заказ")
    def test_logged_in_user_can_order(self, browser, login):
        main_page = MainPage(browser)

        with allure.step("Перетащить ингредиенты в конструктор"):
            main_page.drag_and_drop_ingredient_to_constructor()
        with allure.step("Оформить заказ"):
            main_page.click_order_button()
            main_page.wait_for_element_visibility(MainPageLocators.ORDER_NUMBER)
            order_number = main_page.get_order_number()
            assert (
                order_number.isdigit()
            ), f"Номер заказа не отображается или не является числом: '{order_number}'"

            main_page.wait_for_condition(
                lambda drv: "Ваш заказ начали готовить" in drv.page_source, timeout=5
            )
            assert (
                "Ваш заказ начали готовить" in browser.page_source
            ), "Сообщение о начале готовки не отображается!"
