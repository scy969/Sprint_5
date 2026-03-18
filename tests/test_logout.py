from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators
from test_data import EXISTING_EMAIL, EXISTING_PASSWORD


class TestLogout:

    def test_logout_user(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(EXISTING_EMAIL)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(EXISTING_PASSWORD)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        logout_button = wait.until(
            EC.presence_of_element_located(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        login_button = wait.until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается после логаута"
