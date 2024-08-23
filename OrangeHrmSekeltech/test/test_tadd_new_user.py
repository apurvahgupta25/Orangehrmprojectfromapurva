from Pages.t_new_userpage import Add_new_user
from Pages.dashboard_page import DashboardPage
import time

def test_search_user(driver):
    add_new_user= Add_new_user(driver)
    add_new_user.click_on_admin()
    add_new_user.search_user("Admin",)
    time.sleep(2)
    dashboard_page =DashboardPage(driver)
    assert dashboard_page.actual_heading() == "Admin", "Heading is different"
    time.sleep(2)






def test_add_user(driver):
    add_user1=Add_new_user(driver)

    print("Going to click Add button")
    add_user1.add_new_user_click()
    add_user1.add_newuser("Mohit","Qwerty@123","Qwerty@123")
    time.sleep(4)

