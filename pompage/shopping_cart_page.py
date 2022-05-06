
from selenium.webdriver.common.by import By

class Shopping_Cart():
    xpath_laptop = "(//a[text()='14.1-inch Laptop'])[2]"

    def __init__(self, driver):
        self.driver = driver


    def shopping_cart_check(self):
        return self.driver.find_element(by=By.XPATH, value=self.xpath_laptop)