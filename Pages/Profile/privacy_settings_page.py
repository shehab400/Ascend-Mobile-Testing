from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import PrivacySettingsPageLocaters  # Import SkillsPageLocaters
from logger import logger
#not working due to entered skill issue (coludnt find the enter skill elment)
class PrivacySettingsPage(BasePage):
    """ Page Object for Skills Page """
    DARK_MODE_PAGE = PrivacySettingsPageLocaters.DARK_MODE_PAGE
    DARK_MODE_BUTTON = PrivacySettingsPageLocaters.DARK_MODE_BUTTON
    LIGHT_MODE_BUTTON = PrivacySettingsPageLocaters.LIGHT_MODE_BUTTON
    SHOWING_PROFILE_PHOTOS_PAGE = PrivacySettingsPageLocaters.SHOWING_PROFILE_PHOTOS_PAGE
    PEOPLE_YOU_UNFOLLOWED_PAGE = PrivacySettingsPageLocaters.PEOPLE_YOU_UNFOLLOWED_PAGE
    CLOSE_ACCOUNT_BUTTON = PrivacySettingsPageLocaters.CLOSE_ACCOUNT_BUTTON
      
    
    
    def click_dark_mode_page(self):
        self.click(self.DARK_MODE_PAGE)
    
    def click_dark_mode_button(self):
        self.click(self.DARK_MODE_BUTTON)
    
    def click_light_mode_button(self):
        self.click(self.LIGHT_MODE_BUTTON)
    
    def click_showing_profile_photos_page(self):
        self.click(self.SHOWING_PROFILE_PHOTOS_PAGE)
    
    def click_people_you_unfollowed_page(self):
        self.click(self.PEOPLE_YOU_UNFOLLOWED_PAGE)
    
    def click_close_account_button(self):
        self.click(self.CLOSE_ACCOUNT_BUTTON)
    
    
    