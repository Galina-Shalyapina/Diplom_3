from selenium.webdriver.common.by import By

class PasswordRecoveryLocators:
    EMAIL_INPUT = (By.NAME, "name")
    RECOVER_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, ".input__icon-action")
    PASSWORD_INPUT = (By.CSS_SELECTOR, ".input.pr-6.pl-6.input_type_password.input_size_default")
    PASSWORD_INPUT_FOCUSED = (By.CSS_SELECTOR, ".input__placeholder.text.noselect.text_type_main-default.input__placeholder-focused")
