from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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

    def register_new_user(self, email, password):
        login_input = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        pass_input1 = self.browser.find_element(*LoginPageLocators.REG_PASS_FIELD)
        pass_input2 = self.browser.find_element(*LoginPageLocators.REG_PASS_CONFIRM_FIELD)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_SUBMIT_BUTTON)

        login_input.send_keys(email)
        pass_input1.send_keys(password)
        pass_input2.send_keys(password)
        reg_button.click()

        WebDriverWait(self.browser, 15).until(
            ec.element_to_be_clickable(LoginPageLocators.REG_SUCCESS_MESSAGE)
        )

