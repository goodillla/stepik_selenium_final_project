from .pages.product_page import ProductPage
import pytest


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
