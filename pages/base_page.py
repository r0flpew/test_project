from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

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