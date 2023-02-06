import time

from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product(self):
        product_name = self.get_product_name()
        product_price = self.get_product_price()
        #print(product_name, product_price)  #for debug
        btn_add = self.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add.click()
        self.solve_quiz_and_get_code()  #disabled after solved

        inf_product_added = self.find_element(*ProductPageLocators.INF_PRODUCT_ADDED)
        inf_product_added = inf_product_added.text
        inf_basket_total = self.find_element(*ProductPageLocators.INF_BASKET_TOTAL)
        inf_basket_total = inf_basket_total.text
        #print(inf_product_added, inf_basket_total)  #for debug

        assert product_name == inf_product_added, "The name of added product is different"
        assert product_price == inf_basket_total, "The price of added product is different"
        #time.sleep(3)

    def get_product_name(self):
        product_name = self.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name = product_name.text
        return product_name

    def get_product_price(self):
        product_price = self.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = product_price.text
        return product_price

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Should be dissapeared, but did not"

