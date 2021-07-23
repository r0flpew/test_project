from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()

    product_name_orig = page.get_product_name_original()
    product_price = page.get_product_price()

    page.product_add()

    product_name_confirmed = page.get_product_name_from_confirmation()
    basket_price = page.get_basket_price_from_confirmation()

    assert product_name_orig == product_name_confirmed, f"Product expected: {product_name_orig}, got: {product_name_confirmed}"
    assert product_price == basket_price, f"Expected price: {product_price}, got: {basket_price}"
