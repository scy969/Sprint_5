from selenium.webdriver.support import expected_conditions as EC
from conftest import registration_data
from test_data import EXISTING_EMAIL, EXISTING_PASSWORD
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators


class TestRegistration:

    def test_success_registration(self, driver, wait, registration_data):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(registration_data["email"])
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(registration_data["password"])
        driver.find_element(*AuthPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(registration_data["password"])
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BUTTON).click()

        profile_name = wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_NAME)
        )
        profile_picture = wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_PICTURE)
        )

        assert profile_name.is_displayed(), "Имя пользователя не отображается"
        assert profile_picture.is_displayed(), "Фото профиля не отображается"

    def test_invalid_email_registration(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys("invalidemail")
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))
        wait.until(EC.visibility_of_element_located(AuthPageLocators.ERROR_MESSAGE))

        assert driver.find_element(*AuthPageLocators.ERROR_MESSAGE).text == "Ошибка", "Сообщение об ошибке отсутствует"
        assert driver.find_element(*AuthPageLocators.EMAIL_ERROR_CONTAINER).is_displayed()
        assert driver.find_element(*AuthPageLocators.PASSWORD_ERROR_CONTAINER).is_displayed()
        assert driver.find_element(*AuthPageLocators.SUBMIT_PASSWORD_ERROR_CONTAINER).is_displayed()

    def test_existing_user_registration(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.NO_ACCOUNT_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*AuthPageLocators.SUBMIT_PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*AuthPageLocators.CREATE_ACCOUNT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(AuthPageLocators.EMAIL_INPUT))
        wait.until(EC.visibility_of_element_located(AuthPageLocators.ERROR_MESSAGE))

        assert driver.find_element(*AuthPageLocators.ERROR_MESSAGE).text == "Ошибка", "Cообщение об ошибке отсутствует"
        assert driver.find_element(
            *AuthPageLocators.EMAIL_ERROR_CONTAINER).is_displayed(), "Инпут почты не выделен красным"
        assert driver.find_element(
            *AuthPageLocators.PASSWORD_ERROR_CONTAINER).is_displayed(), "Инпут пароля не выделен красным"
        assert driver.find_element(
            *AuthPageLocators.SUBMIT_PASSWORD_ERROR_CONTAINER).is_displayed(), "Инпут подтверждения пароля не выделен красным"
