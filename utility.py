from Pages.Feed.home_page import HomePage
from Pages.Navigation.sidebar import SideBarPage
import time

class UtilityFunctions:
    def signout(appium_driver):
        home_page = HomePage(appium_driver)
        side_bar_page = SideBarPage(appium_driver)
        home_page.click_Sidebar()
        side_bar_page.click_Settings()
        time.sleep(5)
        appium_driver.swipe(500, 1400, 500, 100, 1000)
        side_bar_page.click_Signout()
        side_bar_page.click_Confirm_Signout()