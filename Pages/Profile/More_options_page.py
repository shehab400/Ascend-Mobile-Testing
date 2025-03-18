from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import MoreOptionsPageLocaters  # Import LoginLocators

class MoreOptionsPage(BasePage):
    """ Page Object for Login Page """
    SHARE_PROFILE_BUTTON = MoreOptionsPageLocaters.SHARE_PROFILE_BUTTON
    CONTACT_INFO_BUTTON = MoreOptionsPageLocaters.CONTACT_INFO_BUTTON
    PERSONAL_DEMOGRAPHIC_INFO_BUTTON = MoreOptionsPageLocaters.PERSONAL_DEMOGRAPHIC_INFO_BUTTON
    ACTIVITY_BUTTON = MoreOptionsPageLocaters.ACTIVITY_BUTTON
    ABOUT_PROFILE_BUTTON = MoreOptionsPageLocaters.ABOUT_PROFILE_BUTTON
    BACK_BUTTON = MoreOptionsPageLocaters.BACK_BUTTON
    MY_ITEMS_BUTTON = MoreOptionsPageLocaters.MY_ITEMS_BUTTON
    
    

    def click_share_profile(self):
        self.click(self.SHARE_PROFILE_BUTTON)
    
    def click_contact_info(self):
        self.click(self.CONTACT_INFO_BUTTON)
    
    def click_personal_demographic_info(self):
        self.click(self.PERSONAL_DEMOGRAPHIC_INFO_BUTTON)
    
    def click_activity(self):
        self.click(self.ACTIVITY_BUTTON)
    
    def click_about_profile(self):
        self.click(self.ABOUT_PROFILE_BUTTON)
    
    def click_back_button(self):
        self.click(self.BACK_BUTTON)
    
    def click_my_items(self):
        self.click(self.MY_ITEMS_BUTTON)
    
        
    
    
    def get_message(self):
        return self.get_text(self.MESSAGE)
    