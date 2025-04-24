from config import BASE_URL
from locators.order_feed_locators import OrderFeedLocators

class OrderFeedPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}feed")

    def click_order_card(self):
        self.driver.find_element(*OrderFeedLocators.ORDER_CARD).click()

    def is_order_modal_open(self):
        return self.driver.find_element(*OrderFeedLocators.ORDER_MODAL).is_displayed()

    def close_modal(self):
        self.driver.find_element(*OrderFeedLocators.MODAL_CLOSE_BUTTON).click()

    def get_total_done(self):
        return int(self.driver.find_element(*OrderFeedLocators.TOTAL_DONE).text)

    def get_total_today(self):
        return int(self.driver.find_element(*OrderFeedLocators.TOTAL_TODAY).text)

    def get_list_order_numbers(self):
        return [el.text for el in self.driver.find_elements(*OrderFeedLocators.LIST_ORDER_NUMBER) if el.text.strip().isdigit()]

    def get_in_progress_order_numbers(self):
        return [el.text for el in self.driver.find_elements(*OrderFeedLocators.IN_PROGRESS_ORDER_NUMBER) if el.text.strip().isdigit()]
