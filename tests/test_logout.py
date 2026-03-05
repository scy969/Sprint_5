from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators


class TestLogout:

    def test_logout_user(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        email = "123000@mail.ru"
        password = "12345678kk22kk"

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        logout_button = wait.until(
            EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        login_button = wait.until(
            EC.visibility_of_element_located(MainPageLocators.LOGIN_BUTTON)
        )
        assert login_button.is_displayed(), "Кнопка 'Вход и регистрация' не отображается после логаута"

        profile_name_elements = driver.find_elements(*ProfilePageLocators.PROFILE_NAME)
        profile_picture_elements = driver.find_elements(*ProfilePageLocators.PROFILE_PICTURE)

        assert len(profile_name_elements) == 0, "Имя пользователя всё ещё отображается после логаута"
        assert len(profile_picture_elements) == 0, "Аватар пользователя всё ещё отображается после логаута"
