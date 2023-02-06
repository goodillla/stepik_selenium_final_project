from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_login = self.find_element(*LoginPageLocators.INPUT_LOGIN)
        input_login.send_keys(email)
        input_password = self.find_element(*LoginPageLocators.INPUT_PASSWORD)
        input_password.send_keys(password)
        input_password_confirm = self.find_element(*LoginPageLocators.INPUT_PASSWORD_CONFIRM)
        input_password_confirm.send_keys(password)
        button_register = self.find_element(*LoginPageLocators.BTN_REGISTER)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'There is no "login" text in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form not present'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form not present'