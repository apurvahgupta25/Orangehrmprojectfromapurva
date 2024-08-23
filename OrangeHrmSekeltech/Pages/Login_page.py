from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class LoginPage(BasePage):
    username = (By.NAME, "username")
    password = (By.NAME, "password")
    submit_button = (By.XPATH, "//*[@type='submit']")


       # to login on the Login_page
    def execute_login(self, username: str, password: str):
        self.find(self.username).send_keys(username)
        self.find(self.password).send_keys(password)
        self.find(self.submit_button).click()

