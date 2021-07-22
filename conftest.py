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
    #user_language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome()
    elif browser_name == "firefox" or browser_name == "ff":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be defined (chrome or firefox)")

    yield driver
    driver.quit()


