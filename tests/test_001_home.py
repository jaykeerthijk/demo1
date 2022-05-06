from time import sleep

import pytest
from selenium.webdriver import Chrome
from pompage.home_page import HomePage


class Test_001_homepagetitle:

    def test_home_title(self, setup):
        self.driver = setup
        act_title = self.driver.title
        if act_title == "Demo Web Shop":
            assert True
        else:
            assert False


    def test_login(self,setup):
        self.driver = setup
        hp = HomePage(setup)
        sleep(5)
        hp.home_click_register()
        act_title = self.driver.title
        if act_title == "Demo Web Shop. Register":
            assert True
        else:
            assert False

