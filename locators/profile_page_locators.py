from selenium.webdriver.common.by import By

class ProfilePageLocators:
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    ORDER_HISTORY_TAB = (By.XPATH, "//a[contains(@href, '/account/order-history')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
