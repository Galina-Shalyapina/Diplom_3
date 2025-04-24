# Stellar Burgers UI & API Autotests

## Описание проекта

Этот проект содержит автоматизированные UI- и API-тесты для веб-приложения [Stellar Burgers](https://stellarburgers.nomoreparties.site/). Тесты реализованы с использованием Python, Selenium, Pytest и Allure.

---

## Структура проекта

```
Diplom_3/
├── pages/            # Page Object классы для различных страниц
├── locators/         # Локаторы для Page Object
├── tests/            # Тестовые сценарии (UI и API)
├── allure-results/   # Каталог для хранения результатов Allure
├── requirements.txt  # Зависимости проекта
├── config.py         # Конфигурация
├── conftest.py       # Настройки драйверов и фикстуры
└── README.md         # Описание проекта
```

---

## Основные технологии
- Python 3.8+
- Selenium WebDriver
- Webdriver Manager
- Pytest
- Allure (для генерации отчетов)
- Requests (для API-тестов)

---

## Быстрый старт

### 1. Установка зависимостей
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Запуск тестов

#### UI-тесты с Allure:
```bash
pytest --alluredir=allure-results
```

#### Генерация и просмотр Allure-отчета:
```bash
allure serve allure-results
```

#### Запуск с выбором браузера:
```bash
pytest --browser=chrome
pytest --browser=firefox
```

---

## Организация тестов
- Каждый тест — отдельный метод в классе.
- Используется фикстура browser для управления драйвером Selenium.
- Данные пользователей и тестовые заказы создаются через API и удаляются после тестов.
- Поддерживается кросс-браузерное тестирование.

---

## Переменные окружения и конфиг
- Основные URL хранятся в `config.py`:
  - `BASE_URL` — основной URL сайта
  - `BASE_API_URL` — URL API
---
