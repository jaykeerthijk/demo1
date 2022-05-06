from time import sleep

from pompage.home_page import HomePage
from pompage.registration_page import RegistrationPage
from pompage.login_page import LoginPage
import pytest

class Test_Registration():

    data = ["male", "jay", "b", "jay@gmail.com", "jay123", "jay123"]
    email = "jk#@gmail.com"
    password = "jay123"

    # def test_register(self, setup):
    #     hp = HomePage(setup)
    #     sleep(5)
    #     hp.home_click_register()
    #     rp = RegistrationPage(setup)
    #     if self.data[0] == "male":
    #         rp.registration_select_male()
    #     else:
    #         rp.registration_select_female()
    #     rp.registration_enter_first_name(self.data[1])
    #     rp.registration_enter_last_name(self.data[2])
    #     rp.registration_enter_email(self.data[3])
    #     rp.registration_enter_password(self.data[4])
    #     rp.registration_enter_confirm_password(self.data[5])
    #     sleep(4)
    #     if rp.registration_complelet():
    #         assert True
    #     else:
    #         assert False

    def test_login(self, setup):
        hp = HomePage(setup)
        sleep(5)
        hp.home_click_login()

        lp = LoginPage(setup)
        lp.login_enter_email(self.email)
        lp.login_enter_password(self.password)
        lp.login_click_login()
        return setup


        # if  == self.email:
        #     assert True
        # else:
        #     assert False







