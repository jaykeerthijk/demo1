from time import sleep

from pompage import shopping_cart_page
from pompage.home_page import HomePage
import pytest
from tests.test_registration import Test_Registration
from pompage.shopping_cart_page import Shopping_Cart

def test_add_cart(setup1):
    Test_Registration.test_login()
    hp = HomePage(setup1)
    hp.home_click_add_tocart()
    hp.home_click_shopping_cart()
    sc = Shopping_Cart(setup1)
    if sc.shopping_cart_check().visible():
        assert True
    else:
        assert False

