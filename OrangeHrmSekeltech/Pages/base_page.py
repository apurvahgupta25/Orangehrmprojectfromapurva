from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self._driver = driver
        self._wait = WebDriverWait(self._driver, 30)
        self._action = ActionChains(self._driver)

    # to find the web element
    def find(self, locator):

        return self._driver.find_element(*locator)

     # to refresh the web_browser
    def window_handle1(self):
        return self._driver.refresh()
