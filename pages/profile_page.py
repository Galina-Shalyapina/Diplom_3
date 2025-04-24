from config import BASE_URL
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(f"{BASE_URL}profile")

    def click_profile(self):
        self.driver.find_element(*ProfilePageLocators.PROFILE_BUTTON).click()

    def click_order_history(self):
        self.driver.find_element(*ProfilePageLocators.ORDER_HISTORY_TAB).click()

    def click_logout(self):
        self.driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
