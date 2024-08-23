import time
from Pages.Login_page import LoginPage
from Pages.Search_page import SearchPage
from Pages.dashboard_page import DashboardPage

# to search a particular username
def test_search(driver):

    search_page = SearchPage(driver)
    search_page.execute_search("Bhuvaneshwar")
    dashboard_page = DashboardPage(driver)
    assert dashboard_page.actual_heading() == "Dashboard", "Heading is different"
    time.sleep(1)

    search_page.back_to_dashboard()
    time.sleep(4)