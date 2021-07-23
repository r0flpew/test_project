from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="en",
                     help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox" or browser_name == "ff":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("intl.accept_languages", user_language)
        driver = webdriver.Firefox(firefox_profile=profile)
    else:
        raise pytest.UsageError("--browser_name should be defined (chrome or firefox)")

    yield driver
    driver.quit()


