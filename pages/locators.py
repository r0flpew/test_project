from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_NAME_ORIGINAL = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_NAME_CONFIRMED = (By.CSS_SELECTOR, "#messages div:first-child strong")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")
