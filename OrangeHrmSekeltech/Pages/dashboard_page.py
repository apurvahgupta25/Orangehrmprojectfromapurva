from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class DashboardPage(BasePage):
    heading = (By.XPATH, "//*[@class='oxd-topbar-header-breadcrumb']/h6")


    # to check the heading of the page
    def actual_heading(self):
        return self.find(self.heading).text





