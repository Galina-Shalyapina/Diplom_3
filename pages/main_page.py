from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from locators.main_page_locators import MainPageLocators
from config import BASE_URL

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def click_constructor(self):
        self.driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

    def click_order_feed(self):
        self.driver.find_element(*MainPageLocators.ORDER_FEED_BUTTON).click()

    def click_login(self):
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

    def click_ingredient(self):
        self.driver.find_element(*MainPageLocators.INGREDIENT).click()

    def close_modal(self):
        self.driver.find_element(*MainPageLocators.MODAL_CLOSE_BUTTON).click()

    def get_ingredient_counter(self):
        return self.driver.find_element(*MainPageLocators.INGREDIENT_COUNTER)
    
    def get_burger_text(self):
        return self.driver.find_element(*MainPageLocators.BURGER_TEXT)

    def drag_and_drop_ingredient_to_constructor(self, ingredient_index=0):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.INGREDIENT)
        )
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_AREA)
        )
        ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT)
        constructor = self.driver.find_element(*MainPageLocators.CONSTRUCTOR_AREA)
        ActionChains(self.driver).click_and_hold(
            ingredients[ingredient_index]
        ).move_to_element(constructor).release().perform()

    def click_order_button(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON).click()

    def get_order_number(self):
        locator = MainPageLocators.ORDER_NUMBER

        # Берем значение из элемента или по умолчанию
        old_text = self.driver.find_element(*locator).text or "9999"

        # Ждем, пока текст НЕ станет отличаться от старого
        WebDriverWait(
            self.driver,
            10,
            ignored_exceptions=(StaleElementReferenceException,)
        ).until(
            lambda d: d.find_element(*locator).text != old_text
        )

        return self.driver.find_element(*locator).text

    def is_modal_open(self, timeout=5):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(MainPageLocators.MODAL_CLOSE_BUTTON)
            )
            return True
        except Exception:
            return False

    def is_modal_closed(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(MainPageLocators.MODAL_CLOSE_BUTTON)
            )
            return True
        except Exception:
            return False
