from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest
import time

#@pytest.mark.skip(reason = "debugging")
@pytest.mark.need_review
@pytest.mark.parametrize('n', [1, 2, 3, 4, 5, 6,\
                                 pytest.param(7, marks=pytest.mark.xfail(reason="programmer is too lazy to fix it :)")),\
                               8, 9])
def test_guest_can_add_product_to_basket(browser, n):
    browser.delete_all_cookies()  #если захотим все сделать в одном браузере
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'+str(n)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product()

@pytest.mark.xfail(reason = "Known bug, waiting for fix")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

@pytest.mark.xfail(reason = "Known bug, waiting for fix")
def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_dissapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_product()
    basket_page.is_empty()

@pytest.mark.register_user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        password = '1234567890987654321'
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.add_product()
