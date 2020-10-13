from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini .btn-default:nth-child(1)")


class LoginPageLocators():
    LOGIN_URL = "/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRMATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    PRODUCT_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    TOTAL_COST_OF_BASKET_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert:nth-child(3)>.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages>.alert:nth-child(1)>.alertinner')


class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
    TEXT_BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
