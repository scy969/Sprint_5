from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, AuthPageLocators, ProfilePageLocators

class TestLogin:

    def test_login_user(self, driver, wait):
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()

        email = "123000@mail.ru"
        password = "12345678kk22kk"

        driver.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*AuthPageLocators.LOGIN_SUBMIT_BUTTON).click()

        profile_name = wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_NAME)
        )
        profile_picture = wait.until(
            EC.visibility_of_element_located(ProfilePageLocators.PROFILE_PICTURE)
        )

        assert profile_name.is_displayed(), "Имя пользователя не отображается после логина"
        assert profile_picture.is_displayed(), "Фото профиля не отображается после логина"