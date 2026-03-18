import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from config import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)


fake = Faker()


@pytest.fixture
def registration_data():
    """Генерирует email и пароль для нового пользователя"""
    return {
        "email": fake.email(),
        "password": fake.password(
            length=10, special_chars=True, digits=True,
            upper_case=True, lower_case=True
        )
    }
