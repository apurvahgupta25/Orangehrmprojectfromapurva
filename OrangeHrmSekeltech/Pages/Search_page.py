import time

from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class SearchPage(BasePage):

    searchtxt=(By.XPATH,"//input[@class='oxd-input oxd-input--active']")
    serachbutton=(By.XPATH,"//*[@class='oxd-icon oxd-menu-icon']")
    dashboard=(By.LINK_TEXT,"Dashboard")

     # to search a element
    def execute_search(self,searchtxt:str):
        self.find(self.searchtxt).send_keys(searchtxt)
        self.find(self.serachbutton).click()
        time.sleep(10)

    # to refresh browser
    def back_to_dashboard(self):
        self.window_handle1()