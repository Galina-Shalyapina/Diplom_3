import allure
from selenium.webdriver.common.action_chains import ActionChains
from locators.main_page_locators import MainPageLocators
from config import BASE_URL
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открытие главной страницы")
    def open(self):
        self.open_url(BASE_URL)

    @allure.step("Нажатие кнопки 'Конструктор'")
    def click_constructor(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Нажатие кнопки 'Лента заказов'")
    def click_order_feed(self):
        self.click(MainPageLocators.ORDER_FEED_BUTTON)

    @allure.step("Нажатие кнопки 'Войти в аккаунт' на главной странице")
    def click_login(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self):
        self.click(MainPageLocators.INGREDIENT)

    @allure.step("Закрытие модального окна")
    def close_modal(self):
        self.click(MainPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step("Получение элемента счетчика ингредиентов")
    def get_ingredient_counter(self):
        return self.find_element(MainPageLocators.INGREDIENT_COUNTER)

    @allure.step("Получение текстового элемента конструктора бургера")
    def get_burger_text(self):
        return self.find_element(MainPageLocators.BURGER_TEXT)

    @allure.step(
        "Перетаскивание ингредиента с индексом {ingredient_index} в конструктор"
    )
    def drag_and_drop_ingredient_to_constructor(self, ingredient_index=0):
        self.wait_for_element_visibility(MainPageLocators.INGREDIENT)
        self.wait_for_element_visibility(MainPageLocators.CONSTRUCTOR_AREA)

        ingredients = self.find_elements(MainPageLocators.INGREDIENT)
        constructor_area = self.find_element(MainPageLocators.CONSTRUCTOR_AREA)

        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredients[ingredient_index]).move_to_element(
            constructor_area
        ).release()
        self.perform_action_chains(actions)

    @allure.step("Нажатие кнопки 'Оформить заказ'")
    def click_order_button(self):
        self.click(MainPageLocators.ORDER_BUTTON)

    @allure.step("Получение номера заказа из модального окна")
    def get_order_number(self):
        locator = MainPageLocators.ORDER_NUMBER
        self.wait_for_element_visibility(locator)

        initial_text = self.get_text(locator).strip()
        reference_text_for_wait = initial_text if initial_text.isdigit() else "9999"

        self.wait_for_condition(
            lambda drv: drv.find_element(*locator).text.strip().isdigit()
            and drv.find_element(*locator).text.strip() != reference_text_for_wait,
            timeout=10,
        )

        return self.get_text(locator).strip()

    @allure.step("Проверка, открыто ли модальное окно с деталями ингредиента")
    def is_modal_open(self, timeout=5):
        return self.is_displayed(MainPageLocators.MODAL_CLOSE_BUTTON, timeout=timeout)

    @allure.step("Проверка, закрыто ли модальное окно с деталями ингредиента")
    def is_modal_closed(self, timeout=5):
        return self.is_invisible(MainPageLocators.MODAL_CLOSE_BUTTON, timeout=timeout)
