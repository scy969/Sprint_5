from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    CREATE_AD_BUTTON = (By.CSS_SELECTOR, "button.buttonPrimary.inButtonText")


class AuthPageLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Создать аккаунт']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")
    ERROR_MESSAGE = (By.XPATH, "//span[text()='Ошибка']")
    EMAIL_ERROR_CONTAINER = (By.XPATH, "//input[@name='email']/parent::div[contains(@class,'input_inputError')]")
    PASSWORD_ERROR_CONTAINER = (By.XPATH, "//input[@name='password']/parent::div[contains(@class,'input_inputError')]")
    SUBMIT_PASSWORD_ERROR_CONTAINER = (By.XPATH,
                                       "//input[@name='submitPassword']/parent::div[contains(@class,'input_inputError')]")


class ProfilePageLocators:
    MY_ADS_BLOCK = (By.XPATH, "//h2[text()='Мои объявления']")
    FIRST_CARD = (By.CSS_SELECTOR, ".profilePage_gridAndPaginaton__togPs .card:first-child")
    PROFILE_PICTURE = (By.CSS_SELECTOR, "button.circleSmall")
    PROFILE_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")


class CreateAdLocators:
    TITLE_INPUT = (By.NAME, "name")
    CATEGORY_ARROW = (
        By.XPATH,
        "//input[@name='category']/following-sibling::button"
    )
    FIRST_CATEGORY = (
        By.XPATH,
        "(//button[contains(@class,'dropDownMenu_btn')])[1]"
    )
    CONDITION_NEW = (By.CSS_SELECTOR, "input[name='condition'][value='Новый']")
    CITY_ARROW = (
        By.XPATH,
        "//input[@name='city']/following-sibling::button"
    )
    FIRST_CITY = (
        By.XPATH,
        "(//div[contains(@class, 'dropDownMenu_options')]//button)[1]"
    )
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.NAME, "price")
    PUBLISH_BUTTON = (By.XPATH, "//button[text()='Опубликовать']")


class ModalLocators:
    AUTH_MODAL_TITLE = (
        By.XPATH,
        "//form[contains(@class,'popUp_shell__LuyqR')]//*[contains(text(),'Чтобы разместить объявление, авторизуйтесь')]"
    )