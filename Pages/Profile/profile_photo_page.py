from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import ProfilePhotoPageLocaters  # Import LoginLocators

class ProfilePhotoPage(BasePage):
    """ Page Object for Login Page """
    ADD_PROFILE_PHOTO_BUTTON = ProfilePhotoPageLocaters.ADD_PROFILE_PHOTO_BUTTON
    ADD_FRAME_BUTTON = ProfilePhotoPageLocaters.ADD_FRAME_BUTTON
    CLOSE_PROFILE_PHOTO_BAR_BUTTON = ProfilePhotoPageLocaters.CLOSE_PROFILE_PHOTO_BAR_BUTTON
    
    
    
    def click_add_profile_photo(self):
        self.click(self.ADD_PROFILE_PHOTO_BUTTON)
    
    def click_add_frame(self):
        self.click(self.ADD_FRAME_BUTTON)
    
    def click_close_profile_photo_bar(self):
        self.click(self.CLOSE_PROFILE_PHOTO_BAR_BUTTON)
    
    
    def get_message(self):
        return self.get_text(self.MESSAGE)
    