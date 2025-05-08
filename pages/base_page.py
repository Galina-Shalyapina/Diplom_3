import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def _wait_for_element_condition(self, locator, timeout, condition, find_all=False):
        try:
            if find_all:
                return WebDriverWait(self.driver, timeout).until(condition(locator))
            return WebDriverWait(self.driver, timeout).until(condition(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Элемент(ы) с локатором {locator} не найден(ы) или условие не выполнено в течение {timeout} секунд."
            )

    @allure.step("Открытие URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    @allure.step("Поиск элемента с локатором: {locator}")
    def find_element(self, locator, timeout=10):
        return self._wait_for_element_condition(
            locator, timeout, EC.presence_of_element_located
        )

    @allure.step("Поиск всех элементов с локатором: {locator}")
    def find_elements(self, locator, timeout=10):
        return self._wait_for_element_condition(
            locator, timeout, EC.presence_of_all_elements_located, find_all=True
        )

    @allure.step("Клик по элементу с локатором: {locator}")
    def click(self, locator, timeout=10):
        element = self._wait_for_element_condition(
            locator, timeout, EC.element_to_be_clickable
        )
        element.click()

    @allure.step("Ввод текста '{text}' в элемент с локатором: {locator}")
    def send_keys(self, locator, text, timeout=10):
        element = self._wait_for_element_condition(
            locator, timeout, EC.visibility_of_element_located
        )
        element.clear()
        element.send_keys(text)

    @allure.step("Получение текста из элемента с локатором: {locator}")
    def get_text(self, locator, timeout=10):
        element = self._wait_for_element_condition(
            locator, timeout, EC.visibility_of_element_located
        )
        return element.text

    @allure.step("Проверка, отображается ли элемент с локатором {locator}")
    def is_displayed(self, locator, timeout=5):
        try:
            self._wait_for_element_condition(
                locator, timeout, EC.visibility_of_element_located
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Проверка, что элемент с локатором {locator} не отображается/невидим")
    def is_invisible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    @allure.step("Получение текущего URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Выполнение действий ActionChains")
    def perform_action_chains(self, actions: ActionChains):
        actions.perform()

    @allure.step("Ожидание видимости элемента с локатором {locator}")
    def wait_for_element_visibility(self, locator, timeout=10):
        return self._wait_for_element_condition(
            locator, timeout, EC.visibility_of_element_located
        )

    @allure.step("Ожидание невидимости элемента с локатором {locator}")
    def wait_for_element_invisibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    @allure.step("Ожидание присутствия элемента с локатором {locator} в DOM")
    def wait_for_element_presence(self, locator, timeout=10):
        return self._wait_for_element_condition(
            locator, timeout, EC.presence_of_element_located
        )

    @allure.step(
        "Ожидание, пока текст элемента {locator} не станет отличаться от '{reference_text}' и не будет пустым"
    )
    def wait_for_text_to_be_different_and_not_empty(
        self, locator, reference_text, timeout=10
    ):
        WebDriverWait(
            self.driver, timeout, ignored_exceptions=(StaleElementReferenceException,)
        ).until(
            lambda drv: drv.find_element(*locator).text.strip()
            != reference_text.strip()
            and drv.find_element(*locator).text.strip() != ""
        )

    @allure.step("Ожидание выполнения пользовательского условия")
    def wait_for_condition(self, condition, timeout=10, ignored_exceptions=None):
        if ignored_exceptions is None:
            ignored_exceptions = (StaleElementReferenceException,)
        return WebDriverWait(
            self.driver, timeout, ignored_exceptions=ignored_exceptions
        ).until(condition)

    @allure.step(
        "Получение атрибута '{attribute_name}' из элемента с локатором: {locator}"
    )
    def get_attribute(self, locator, attribute_name, timeout=10):
        element = self._wait_for_element_condition(
            locator, timeout, EC.presence_of_element_located
        )
        return element.get_attribute(attribute_name)

    @allure.step("Ожидание, пока URL не будет содержать: {partial_url}")
    def wait_for_url_to_contain(self, partial_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))
