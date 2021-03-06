from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_INPUT = (By.CSS_SELECTOR, "#id_registration-password1") 	
    PASSWORD2_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_SABMIT = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>p.price_color")
    ALERT_MSG_ADD = (By.CSS_SELECTOR, ".alert-success .alertinner")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    ALERT_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_BASKET = (By.CSS_SELECTOR, "span>a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_AMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")	