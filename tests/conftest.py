
from selenium.webdriver import Chrome
import pytest
from tests.test_registration import Test_Registration

@pytest.fixture
def setup():
    driver = Chrome("driver/chromedriver.exe")
    driver.get("http://demowebshop.tricentis.com")
    yield driver
    driver.close()

@pytest.fixture
def setup1():
    driver = Chrome("driver/chromedriver.exe")
    driver.get("http://demowebshop.tricentis.com")
    yield Test_Registration.test_login()
    driver.close()