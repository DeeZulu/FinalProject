from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
