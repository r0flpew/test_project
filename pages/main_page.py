from .base_page import BasePage
from .locators import MainPageLocators  # пока не используется, но локаторы будут нужны при добавлении новых методов.


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
