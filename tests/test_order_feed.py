import allure
from pages.order_feed_page import OrderFeedPage
from conftest import create_order

@allure.feature('Лента заказов')
class TestOrderFeed:
    @allure.step('Открытие модального окна заказа')
    def test_order_card_opens_modal(self, browser):
        page = OrderFeedPage(browser)
        with allure.step('Открыть страницу ленты заказов'):
            page.open()
        with allure.step('Кликнуть по карточке заказа'):
            page.click_order_card()
            assert page.is_order_modal_open()

    @allure.step('Появление заказа пользователя в ленте')
    def test_profile_orders_appear_in_feed(self, browser, create_order):
        order_number = create_order
        feed_page = OrderFeedPage(browser)
        with allure.step('Открыть страницу ленты заказов'):
            feed_page.open()
        with allure.step('Проверить наличие заказа в ленте'):
            assert order_number in ''.join(feed_page.get_list_order_numbers())

    @allure.step('Увеличение счетчика выполненных заказов после нового заказа')
    def test_total_done_increases_after_new_order(self, browser, request):
        page = OrderFeedPage(browser)
        with allure.step('Открыть страницу ленты заказов'):
            page.open()
        with allure.step('Сохранить текущее количество выполненных заказов'):
            total_before = page.get_total_done()
        with allure.step('Создать новый заказ'):
            request.getfixturevalue("create_order")
        with allure.step('Обновить страницу ленты заказов'):
            page.open()
        with allure.step('Проверить увеличение количества выполненных заказов'):
            total_after = page.get_total_done()
            assert total_after > total_before

    @allure.step('Увеличение счетчика заказов за сегодня после нового заказа')
    def test_total_today_increases_after_new_order(self, browser, request):
        page = OrderFeedPage(browser)
        with allure.step('Открыть страницу ленты заказов'):
            page.open()
        with allure.step('Сохранить текущее количество заказов за сегодня'):
            total_today_before = page.get_total_today()
        with allure.step('Создать новый заказ'):
            request.getfixturevalue("create_order")
        with allure.step('Обновить страницу ленты заказов'):
            page.open()
        with allure.step('Проверить увеличение количества заказов за сегодня'):
            total_today_after = page.get_total_today()
            assert total_today_after > total_today_before

    @allure.step('Появление номера заказа в "В работе" после заказа')
    def test_order_number_appears_in_progress_after_order(self, browser, create_order):
        order_number = create_order
        feed_page = OrderFeedPage(browser)
        with allure.step('Открыть страницу ленты заказов'):
            feed_page.open()
        with allure.step('Проверить наличие заказа в "В работе"'):
            assert order_number in ''.join(feed_page.get_in_progress_order_numbers())
