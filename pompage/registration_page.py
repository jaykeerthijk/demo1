
from selenium.webdriver.common.by import By


class RegistrationPage():
    _rdo_male = "gender-male"
    _rdo_female = "gender-female"
    _txt_first_name = "FirstName"
    _txt_last_name = "LastName"
    _txt_email = "Email"
    _txt_password = "Password"
    _txt_confirm_password = "ConfirmPassword"
    _btn_register = "register-button"
    _class_reg_complet = "register"

    def __init__(self, driver):
        self.driver = driver

    def registration_select_male(self):
        self.driver.find_element(by=By.ID, value=self._rdo_male).click()

    def registration_select_female(self):
        self.driver.find_element(by=By.ID, value=self._rdo_female).click()

    def registration_enter_first_name(self, fname):
        self.driver.find_element(by=By.NAME, value=self._txt_first_name).send_keys(fname)

    def registration_enter_last_name(self, lname):
        self.driver.find_element(by=By.NAME, value=self._txt_last_name).send_keys(lname)

    def registration_enter_email(self, email):
        self.driver.find_element(by=By.ID, value=self._txt_email).send_keys(email)

    def registration_enter_password(self, password):
        self.driver.find_element(by=By.ID, value=self._txt_password).send_keys(password)

    def registration_enter_confirm_password(self, password):
        self.driver.find_element(by=By.ID, value=self._txt_confirm_password).send_keys(password)

    def registration_click_register(self):
        self.driver.find_element(by=By.ID, value=self._btn_register).click()

    def registration_complelet(self):
        self.driver.find_element(by=By.ID, value=self._class_reg_complet)