
from selenium.webdriver.common.by import By


class HomePage:
    lnk_text_register = "Register"
    lnk_text_login = "Log in"
    partial_lnk_text_shoppingcart = "Shopping cart"
    btn_add_tocart = "//a[text()='14.1-inch Laptop']/../..//input"


    def __init__(self, driver):
        self.driver = driver

    def home_click_register(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnk_text_register).click()

    def home_click_login(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnk_text_login).click()

    def home_click_register_text(self):
        return self.driver.find_element(by=By.LINK_TEXT, value=self.lnk_text_register).text()

    def home_click_shopping_cart(self):
        return self.driver.find_element(by=By.PARTIAL_LINK_TEXT, value=self.partial_lnk_text_shoppingcart).click()

    def home_click_add_tocart(self):
        return self.driver.find_element(by=By.XPATH, value=self.btn_add_tocart).click()

