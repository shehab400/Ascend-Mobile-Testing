from Pages.Profile.profile_page import ProfiePage
from Pages.Navigation.sidebar import SideBarPage
from Pages.Feed.home_page import HomePage
from Pages.Profile.work_experience_page import WorkExperiencePage
import time
from logger import logger

def test_work_experience_page(appium_driver):
    logger.info("Testing education page")
    profile_page = ProfiePage(appium_driver) 
    home_page = HomePage(appium_driver)
    experience_page = WorkExperiencePage(appium_driver)
    sidebar_page = SideBarPage(appium_driver)
    logger.info("clicking sidebar in home page")
    home_page.click_Sidebar()
    time.sleep(1)
    logger.info("clicking my profile in sidebar")
    sidebar_page.click_Myprofile()
    time.sleep(1)
    logger.info("clicking edit profile in profile page")
    appium_driver.swipe(583, 1900, 583, 50, 1000)
    appium_driver.swipe(583, 1000, 583, 400, 1000)
    time.sleep(1)
    profile_page.click_add_experience()
    time.sleep(1)
    experience_page.enter_title('Software Engineer')
    experience_page.select_employment_type('Full-time')
    experience_page.enter_company_name('Google')
    experience_page.check_currently_working()
    
    
    time.sleep(5)