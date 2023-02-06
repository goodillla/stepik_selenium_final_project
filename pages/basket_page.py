from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_have_product(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Basket has product, but should not"

    def is_empty(self):
        basket_text = self.find_element(*BasketPageLocators.EMPTY_BASKET)
        basket_text = basket_text.text
        assert 'basket is empty' in basket_text,\
            "Basket has product, but should be empty"

