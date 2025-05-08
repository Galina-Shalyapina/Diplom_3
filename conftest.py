import uuid
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config import BASE_API_URL
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser to use: chrome or firefox"
    )

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        service = ChromeService(ChromeDriverManager().install())
        options = ChromeOptions()
        driver = webdriver.Chrome(options=options, service=service)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user():
    register_url = f"{BASE_API_URL}auth/register"
    user_data = {
        "name": "TestUser",
        "email": f"test_{uuid.uuid4()}@yandex.ru",
        "password": "secure_password"
    }
    response = requests.post(register_url, json=user_data)
    assert response.status_code == 200

    yield user_data

    access_token = response.json().get("accessToken")
    if access_token:
        headers = {"Authorization": access_token}
        requests.delete(register_url, headers=headers)


@pytest.fixture(scope="function")
def login(browser, user):
    login_page = LoginPage(browser)
    login_page.open()
    login_page.enter_email(user["email"])
    login_page.enter_password(user["password"])
    login_page.click_login()
    return ProfilePage(browser)

@pytest.fixture(scope="function")
def create_order(browser, login):
    main_page = MainPage(browser)
    main_page.drag_and_drop_ingredient_to_constructor()
    main_page.click_order_button()
    order_number = main_page.get_order_number()
    return order_number
