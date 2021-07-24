from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='login-username']")
    LOGIN_PASS_FIELD = (By.CSS_SELECTOR, "input[name='login-password']")
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='login_submit']")

    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='registration-email']")
    REG_PASS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    REG_PASS_CONFIRM_FIELD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REG_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")
    REG_SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class ProductPageLocators():
    BASKET_ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_NAME_ORIGINAL = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_NAME_CONFIRMED = (By.CSS_SELECTOR, "#messages div:first-child strong")
    BASKET_PRICE_MESSAGE = (By.CSS_SELECTOR, "#messages div:nth-child(3) strong")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a[href=\"/en-gb/basket/\"].btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_CONTENT = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_LIST = (By.CSS_SELECTOR, ".basket-items")
