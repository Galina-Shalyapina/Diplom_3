from selenium.webdriver.common.by import By

class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BURGER_TEXT = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT = (By.CSS_SELECTOR, ".BurgerIngredient_ingredient__image__3e-07.ml-4.mr-4")
    CONSTRUCTOR_AREA = (By.CSS_SELECTOR, ".constructor-element.constructor-element_pos_top")
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, ".counter_counter__num__3nue1")
    MODAL_CLOSE_BUTTON = (By.CSS_SELECTOR, ".Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK")
    ORDER_NUMBER = (By.CSS_SELECTOR, ".Modal_modal__title_shadow__3ikwq.Modal_modal__title__2L34m.text.text_type_digits-large.mb-8")
    MODAL_WITH_ORDER_LOADING = (By.CSS_SELECTOR, ".Modal_modal_opened__3ISw4.Modal_modal__P3_V5")
