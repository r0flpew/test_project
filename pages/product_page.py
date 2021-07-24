from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def product_add(self):
        add_button = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BUTTON)
        add_button.click()

    def get_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return price

    def get_product_name_original(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ORIGINAL).text
        return name

    def check_product_name(self, orig_name):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CONFIRMED).text
        assert orig_name == product_name, f"Product expected: {orig_name}, got: {product_name}"

    def check_product_price(self, orig_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MESSAGE).text
        assert orig_price == basket_price, f"Expected price: {orig_price}, got: {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(ProductPageLocators.PRODUCT_NAME_CONFIRMED), \
            "success message presented (should not be)"

    def should_success_message_disappear(self):
        assert self.is_disappeared(ProductPageLocators.PRODUCT_NAME_CONFIRMED), \
            "success message must disappear"
