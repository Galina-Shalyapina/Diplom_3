import allure
from config import BASE_URL
from locators.order_feed_locators import OrderFeedLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Открытие страницы ленты заказов")
    def open(self):
        self.open_url(f"{BASE_URL}feed")

    @allure.step("Клик по карточке заказа")
    def click_order_card(self):
        self.click(OrderFeedLocators.ORDER_CARD)

    @allure.step("Проверка, открыто ли модальное окно заказа")
    def is_order_modal_open(self):
        return self.is_displayed(OrderFeedLocators.ORDER_MODAL)

    @allure.step("Закрытие модального окна на странице ленты заказов")
    def close_modal(self):
        self.click(OrderFeedLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение общего количества выполненных заказов")
    def get_total_done(self):
        text = self.get_text(OrderFeedLocators.TOTAL_DONE)
        return int(text) if text.strip() else 0

    @allure.step("Получение количества заказов, выполненных сегодня")
    def get_total_today(self):
        text = self.get_text(OrderFeedLocators.TOTAL_TODAY)
        return int(text) if text.strip() else 0

    @allure.step("Получение списка номеров заказов из ленты")
    def get_list_order_numbers(self):
        elements = self.find_elements(OrderFeedLocators.LIST_ORDER_NUMBER)
        return [
            str(int(el.text.strip())) for el in elements if el.text.strip().isdigit()
        ]

    @allure.step("Получение списка номеров заказов в работе")
    def get_in_progress_order_numbers(self):
        elements = self.find_elements(OrderFeedLocators.IN_PROGRESS_ORDER_NUMBER)
        return [
            str(int(el.text.strip())) for el in elements if el.text.strip().isdigit()
        ]
