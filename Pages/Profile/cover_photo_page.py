from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import CoverPhotoLocaters  # Import LoginLocators

class CoverPhotoPage(BasePage):
    """ Page Object for Login Page """
    UPLOAD_PHOTO_BUTTON = CoverPhotoLocaters.UPLOAD_PHOTO_BUTTON
    CLOSE_BUTTON = CoverPhotoLocaters.CLOSE_BUTTON
    SAVE_BUTTON = CoverPhotoLocaters.SAVE_BUTTON
    TAKE_PHOTO_BUTTON = CoverPhotoLocaters.TAKE_PHOTO_BUTTON
    UPLOAD_FROM_GALLERY_BUTTON = CoverPhotoLocaters.UPLOAD_FROM_GALLERY_BUTTON
    
    

    def click_upload_photo(self):
        self.click(self.UPLOAD_PHOTO_BUTTON)
    
    def click_close(self):
        self.click(self.CLOSE_BUTTON)
    
    def click_save(self):
        self.click(self.SAVE_BUTTON)
    
    def click_take_photo(self):
        self.click(self.TAKE_PHOTO_BUTTON)
    
    def click_upload_from_gallery(self):
        self.click(self.UPLOAD_FROM_GALLERY_BUTTON)
    
    
    def get_message(self):
        return self.get_text(self.MESSAGE)
    