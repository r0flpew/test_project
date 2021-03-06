from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
import math


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        from .login_page import LoginPage
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        return LoginPage(browser=self.browser,
                         url=self.browser.current_url)  # возвращаем объект loginpage, если он нужен

    def go_to_basket_page(self):
        from .basket_page import BasketPage
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_link.click()
        return BasketPage(browser=self.browser,
                          url=self.browser.current_url)  # возвращаем объект basketpage, если он нужен

    def should_be_login_link(self):
        assert self.is_element_present(BasePageLocators.LOGIN_LINK), "user should see login_link"

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector):
        try:
            self.browser.find_element(*selector)
        except NoSuchElementException as e:
            return False
        return True

    def is_url_contains(self, str_to_search):
        url = self.browser.current_url
        if str_to_search in url:
            return True
        else:
            return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(selector))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                ec.presence_of_element_located(selector))
        except TimeoutException:
            return False

        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                    " probably unauthorised user"
