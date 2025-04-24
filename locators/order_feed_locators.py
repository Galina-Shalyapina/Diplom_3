from selenium.webdriver.common.by import By

class OrderFeedLocators:
    ORDER_CARD = (By.CSS_SELECTOR, '.OrderHistory_listItem__2x95r.mb-6')
    ORDER_MODAL = (By.CSS_SELECTOR, '.Modal_orderBox__1xWdi.Modal_modal__contentBox__sCy8X.p-10')
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, '[data-test="modal-close"]')
    TOTAL_DONE = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')
    TOTAL_TODAY = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')
    IN_PROGRESS_ORDER_NUMBER = (By.CSS_SELECTOR, 'ul.OrderFeed_orderList__cBvyi > li.text_type_digits-default')
    LIST_ORDER_NUMBER = (By.CSS_SELECTOR, 'ul.OrderFeed_orderList__cBvyi > li')
