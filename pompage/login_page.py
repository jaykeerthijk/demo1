from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    # Class variables
    _txt_email = "Email"
    _txt_password = "Password"
    _btn_login = "//input[@value='Log in']"

    def login_enter_email(self, email):
        self.driver.find_element(by=By.NAME, value=self._txt_email).send_keys(email)

    def login_enter_password(self, password):
        self.driver.find_element(by=By.NAME, value= self._txt_password).send_keys(password)

    def login_click_login(self):
        self.driver.find_element(by=By.XPATH, value=self._btn_login).click()