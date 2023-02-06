from .pages.product_page import ProductPage
import pytest

n = 10  #зададим количество тестов
links = ['http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'+str(i) for i in range(n)]
@pytest.mark.parametrize('link', links)
@pytest.mark.parametrize('link', ["okay_link",
                                  pytest.param("bugged_link", marks=pytest.mark.xfail),
                                  "okay_link"])
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/" #?promo=newYear убрал чтоб не решать каждый раз
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product()
