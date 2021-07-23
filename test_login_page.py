from .pages.login_page import LoginPage

link = "https://selenium1py.pythonanywhere.com/accounts/login/"

def test_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()

def test_user_should_see_login_url(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_user_should_see_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_user_should_see_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()
