from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Have products in the basket"

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_IS_EMPTY), "No text about basket is empty"
