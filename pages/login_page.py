from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_url_contains("login"), "word 'login' should be in page url"


    def should_be_login_form(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_FORM), "user should see login form"

    def should_be_register_form(self):
        assert self.is_element_present(LoginPageLocators.REGISTER_FORM), "user should see register form"