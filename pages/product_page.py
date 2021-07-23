from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def product_add(self):
        add_button = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def get_product_name_original(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ORIGINAL).text
        return name


    def get_product_name_from_confirmation(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CONFIRMED).text
        return name

    def get_basket_price_from_confirmation(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
        return basket_price
