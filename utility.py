from Pages.Feed.home_page import HomePage
from Pages.Navigation.sidebar import SideBarPage
from Pages.Authentication.login_page import LoginPage
from Pages.Authentication.landing_page import LandingPage
from Pages.Profile.profile_page import ProfiePage
from Test_Cases_Data.Authentication import LoginTestCasesData as TC
import time
from logger import logger

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
        
    def login(appium_driver):
        login_page = LoginPage(appium_driver)
        landing_page = LandingPage(appium_driver)
        try:
            landing_page.click_sign_in_with_email()
        except:
            pass
        login_page.enter_email(TC.TEST_EMAIL)
        appium_driver.hide_keyboard()
        time.sleep(2)
        login_page.enter_password(TC.TEST_VALID_PASSWORD)
        appium_driver.hide_keyboard()
        time.sleep(2)
        login_page.click_remember_me()
        time.sleep(1)
        login_page.click_continue()
        time.sleep(2)
        try:
            HomePage.click_close_button()
        except: 
            pass
    

    def open_profile_page(appium_driver):
        home_page = HomePage(appium_driver)
        sidebar_page = SideBarPage(appium_driver)
        home_page.click_Sidebar()
        time.sleep(1)
        sidebar_page.click_Myprofile()
        time.sleep(1)
    