import time

from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from selenium.webdriver.support.select import Select

class Add_new_user(BasePage):


     # xpath of web_element of search functionality
     Admin1=(By.XPATH,"//*[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][1]")
     username=(By.XPATH,"//div[*/label[contains(text(),'Username')]]//input[@class='oxd-input oxd-input--active']")
     search_button=(By.XPATH,"//button[@type='submit']")

     add_record_button=(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']//i")

     #add new user locators

     Userrole1=(By.XPATH,"//div[*/label[contains(text(),'User Role')]]//div[@class='oxd-select-text-input']")
     Userroleadmin=(By.XPATH,"//*[contains(text(),'Admin')]")
     Employee_name=(By.XPATH,"//div[*/label[contains(text(),'Employee Name')]]//input[@placeholder='Type for hints...']")
     status=(By.XPATH,"//div[*/label[contains(text(),'Status')]]//div[@class='oxd-select-text oxd-select-text--active']")
     statusenable=(By.XPATH,"//*[contains(text(),'Enabled')]")
     Username=(By.XPATH,"//div[*/label[contains(text(),'Username')]]//input[@class='oxd-input oxd-input--active']")
     Password=(By.XPATH,"//div[*/label[text()='Password']]//*[@class='oxd-input oxd-input--active']")
     Confirm_password=(By.XPATH,"//div[*/label[text()='Confirm Password']]//*[@class='oxd-input oxd-input--active']")
     Save_button=(By.XPATH,"//button[@type='submit']")
     Name = (By.XPATH,"//*[text()='Thomas Kutty Benny']")

     #click on admin
     def click_on_admin(self):
         return self.find(self.Admin1).click()

      # to search the user
     def search_user(self, username: str):

        self.find(self.username).send_keys(username)
        #self.find(self.userrole).click()
        #self.find(self.Employeename).send_keys(Employeename)
       # self.find(self.status).click()
        self.find(self.search_button).click()




      #click on add button
     def add_new_user_click(self):
         return self.find(self.add_record_button).click()

      # add new user
     def add_newuser(self,Username:str, Password:str, Confirm_password:str):
         time.sleep(5)

         self.find(self.Userrole1).click()
         self.find(self.Userroleadmin).click()
         time.sleep(3)
         self.find(self.Employee_name).send_keys("Thomas")
         time.sleep(5)
         self.find(self.Name).click()
         time.sleep(3)
         self.find(self.status).click()
         self.find(self.statusenable).click()
         time.sleep(3)
        # Select(self.find(self.status)).select_by_index(2)
         self.find(self.Username).send_keys(Username)
         self.find(self.Password).send_keys(Password)
         self.find(self.Confirm_password).send_keys(Confirm_password)
         self.find(self. Save_button).click()
         time.sleep(3)
