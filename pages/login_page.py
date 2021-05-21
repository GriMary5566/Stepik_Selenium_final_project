from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        link_url = self.browser.current_url        
        assert "login" in link_url, "Substring 'login' is absent in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):        
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_input.send_keys(email)
        password1_input = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        password1_input.send_keys(password)
        password2_input = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        password2_input.send_keys(password)
        button_reg_submit = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SABMIT)
        button_reg_submit.click()
    