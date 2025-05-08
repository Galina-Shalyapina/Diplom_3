import allure
from pages.order_feed_page import OrderFeedPage
from locators.order_feed_locators import OrderFeedLocators


@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Открытие модального окна заказа по клику на карточку в ленте")
    def test_order_card_opens_modal(self, browser):
        page = OrderFeedPage(browser)
        with allure.step("Открыть страницу ленты заказов"):
            page.open()
            page.wait_for_element_visibility(OrderFeedLocators.ORDER_CARD)
        with allure.step("Кликнуть по карточке заказа"):
            page.click_order_card()
            assert page.is_order_modal_open(), "Модальное окно заказа не открылось"

    @allure.title("Заказ пользователя появляется в общей ленте заказов")
    def test_profile_orders_appear_in_feed(self, browser, create_order):
        order_number_created = create_order
        feed_page = OrderFeedPage(browser)
        with allure.step("Открыть страницу ленты заказов"):
            feed_page.open()
            feed_page.wait_for_condition(
                lambda drv: order_number_created in feed_page.get_list_order_numbers(),
                timeout=15,
            )
        with allure.step("Проверить наличие заказа в ленте"):
            list_of_orders_text = feed_page.get_list_order_numbers()
            assert (
                order_number_created in list_of_orders_text
            ), f"Созданный заказ {order_number_created} не найден в ленте {list_of_orders_text}"

    @allure.title('Счетчик "Выполнено за все время" увеличивается после нового заказа')
    def test_total_done_increases_after_new_order(self, browser, request):
        page = OrderFeedPage(browser)
        with allure.step(
            "Открыть страницу ленты заказов и получить начальное значение счетчика"
        ):
            page.open()
            page.wait_for_element_visibility(OrderFeedLocators.TOTAL_DONE)
            total_before = page.get_total_done()

        with allure.step("Создать новый заказ (через фикстуру)"):
            request.getfixturevalue("create_order")

        with allure.step(
            "Обновить страницу ленты заказов и ожидать увеличения счетчика"
        ):
            page.open()
            page.wait_for_condition(
                lambda drv: page.get_total_done() > total_before, timeout=15
            )
        with allure.step("Проверить увеличение количества выполненных заказов"):
            total_after = page.get_total_done()
            assert (
                total_after > total_before
            ), f"Счетчик 'Выполнено за все время' не увеличился. Было: {total_before}, стало: {total_after}"

    @allure.title('Счетчик "Выполнено за сегодня" увеличивается после нового заказа')
    def test_total_today_increases_after_new_order(self, browser, request):
        page = OrderFeedPage(browser)
        with allure.step(
            'Открыть страницу ленты заказов и получить начальное значение счетчика "Выполнено за сегодня"'
        ):
            page.open()
            page.wait_for_element_visibility(OrderFeedLocators.TOTAL_TODAY)
            total_today_before = page.get_total_today()

        with allure.step("Создать новый заказ (через фикстуру)"):
            request.getfixturevalue("create_order")

        with allure.step(
            "Обновить страницу ленты заказов и ожидать увеличения счетчика"
        ):
            page.open()
            page.wait_for_condition(
                lambda drv: page.get_total_today() > total_today_before, timeout=15
            )
        with allure.step("Проверить увеличение количества заказов за сегодня"):
            total_today_after = page.get_total_today()
            assert (
                total_today_after > total_today_before
            ), f"Счетчик 'Выполнено за сегодня' не увеличился. Было: {total_today_before}, стало: {total_today_after}"

    @allure.title('Номер нового заказа появляется в секции "В работе" после оформления')
    def test_order_number_appears_in_progress_after_order(self, browser, create_order):
        order_number_created = create_order
        feed_page = OrderFeedPage(browser)
        with allure.step(
            'Открыть страницу ленты заказов и ожидать появления заказа "В работе"'
        ):
            feed_page.open()
            feed_page.wait_for_condition(
                lambda drv: order_number_created
                in feed_page.get_in_progress_order_numbers(),
                timeout=15,
            )
        with allure.step('Проверить наличие заказа в секции "В работе"'):
            in_progress_orders = feed_page.get_in_progress_order_numbers()
            assert (
                order_number_created in in_progress_orders
            ), f"Созданный заказ {order_number_created} не найден в секции 'В работе': {in_progress_orders}"
