from .base_page import BasePage
from .locators import BasketPageLocators

url = "http://selenium1py.pythonanywhere.com/basket/"


class BasketPage(BasePage):
    def is_basket_empty(self):
        assert self.is_not_element_present(BasketPageLocators.ITEMS_LIST), "items list is present, should not"

    def is_basket_message_present(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text
        assert isinstance(message, str) and len(message) > 0, "message about empty basket is not present"
