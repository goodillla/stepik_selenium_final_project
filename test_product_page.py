from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

'''
#n = 10  #зададим количество тестов
#links = [i for i in range(n)]
@pytest.mark.parametrize('n', [1, 2, 3, 4, 5, 6,\
                                 pytest.param(7, marks=pytest.mark.xfail(reason="proger is too lazy fix it :)")),\
                                 8, 9])
def test_guest_can_add_product_to_basket(browser, n):
    browser.delete_all_cookies()  #если захотим все сделать в одном браузере
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'+str(n)
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product()
'''
'''
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

def test_message_disappeared_after_adding_product_to_basket(browser):
    browser.delete_all_cookies()
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product()
    product_page.should_dissapeared()
'''

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_have_product()
    basket_page.is_empty()
