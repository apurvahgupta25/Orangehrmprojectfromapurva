import time

import pytest
from selenium import webdriver


#@pytest.fixture(scope="class")
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.implicitly_wait(2)
    driver.maximize_window()
    yield driver

    driver.quit()

