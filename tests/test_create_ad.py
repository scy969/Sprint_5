import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from locators import MainPageLocators, CreateAdLocators, ProfilePageLocators, ModalLocators, AuthPageLocators


class TestCreateAd:

    def test_create_ad_not_authorized(self, driver, wait):
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        wait.until(EC.visibility_of_element_located(ModalLocators.AUTH_MODAL_TITLE))

        assert driver.find_element(
            *ModalLocators.AUTH_MODAL_TITLE).is_displayed(), "Модальное окно авторизации не отобразилось"

    def test_create_ad_authorized(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        email = "123000@mail.ru"
        password = "12345678kk22kk"

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_NAME)
        )
        wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_PICTURE)
        )

        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        wait.until(EC.visibility_of_element_located(CreateAdLocators.TITLE_INPUT))

        driver.find_element(*CreateAdLocators.TITLE_INPUT).send_keys("Тестовое объявление")
        driver.find_element(*CreateAdLocators.CATEGORY_ARROW).click()

        wait.until(
            EC.element_to_be_clickable(CreateAdLocators.FIRST_CATEGORY)
        ).click()

        driver.find_element(*CreateAdLocators.CITY_ARROW).click()

        # Пожалуйста, подскажите адекватное решение, сейчас постоянно ловлю ElementNotInteractableException

        driver.execute_script("""
                            window.scrollTo({
                                top: document.body.scrollHeight,
                                left: 0,
                                behavior: 'smooth'
                            });
                        """)

        city_button = wait.until(
            EC.presence_of_element_located(CreateAdLocators.FIRST_CITY)
        )
        driver.execute_script("arguments[0].click();", city_button)

        wait.until(EC.element_to_be_clickable(CreateAdLocators.DESCRIPTION_INPUT)).send_keys("Описание объявления")

