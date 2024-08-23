import time

import pytest

from Pages.dashboard_page import DashboardPage
from Pages.Login_page import LoginPage
from Pages.Search_page import SearchPage
from Pages.dashboard_page import DashboardPage


# to go login
def test_login_positive(driver):
    login_page = LoginPage(driver)
    login_page.execute_login("Admin", "admin123")
    time.sleep(1)
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.actual_heading() == "Dashboard", "Heading is different"



