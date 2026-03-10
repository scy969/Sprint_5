from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, CreateAdLocators, ProfilePageLocators, ModalLocators, AuthPageLocators
from test_data import EXISTING_EMAIL, EXISTING_PASSWORD
import time

class TestCreateAd:

    def test_create_ad_not_authorized(self, driver, wait):
        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()

        wait.until(EC.visibility_of_element_located(ModalLocators.AUTH_MODAL_TITLE))

        assert driver.find_element(
            *ModalLocators.AUTH_MODAL_TITLE).is_displayed(), "Модальное окно авторизации не отобразилось"

    def test_create_ad_authorized(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_NAME)
        )

        driver.find_element(*MainPageLocators.CREATE_AD_BUTTON).click()
        wait.until(EC.visibility_of_element_located(CreateAdLocators.TITLE_INPUT))

        driver.find_element(*CreateAdLocators.TITLE_INPUT).send_keys("Тестовое объявление")
        driver.find_element(*CreateAdLocators.CATEGORY_ARROW).click()
        wait.until(
            EC.element_to_be_clickable(CreateAdLocators.FIRST_CATEGORY)
        ).click()

        driver.find_element(*CreateAdLocators.CITY_ARROW).click()
        wait.until(EC.element_to_be_clickable(CreateAdLocators.FIRST_CITY)).click()

        wait.until(EC.element_to_be_clickable(CreateAdLocators.DESCRIPTION_INPUT))
        driver.find_element(*CreateAdLocators.DESCRIPTION_INPUT).send_keys("Описание объявления")

        driver.find_element(*CreateAdLocators.PRICE_INPUT).send_keys("500")
        driver.find_element(*CreateAdLocators.PUBLISH_BUTTON).click()

        time.sleep(1)

        wait.until(
            EC.element_to_be_clickable(ProfilePageLocators.PROFILE_PICTURE)
            )

        driver.find_element(*ProfilePageLocators.PROFILE_PICTURE).click()

        assert driver.find_element(*ProfilePageLocators.FIRST_CARD).is_displayed(), "Карточка отсутствует"
