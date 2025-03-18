from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import EditProfilePageLocaters  

class EditProfiePage(BasePage):
    """ Page Object for Login Page """
    FIRST_NAME = EditProfilePageLocaters.FIRST_NAME
    LAST_NAME = EditProfilePageLocaters.LAST_NAME
    ADDITIONAL_NAME = EditProfilePageLocaters.ADDITIONAL_NAME
    HEADLINE = EditProfilePageLocaters.HEADLINE
    INDUSTRY = EditProfilePageLocaters.INDUSTRY
    SCHOOL = EditProfilePageLocaters.SCHOOL
    ADD_NEW_EDUCATION_BUTTON = EditProfilePageLocaters.ADD_NEW_EDUCATION_BUTTON
    LOCATION = EditProfilePageLocaters.LOCATION
    CITY = EditProfilePageLocaters.CITY
    # EDIT CONTACT INFO , WEBSITE, SHOW SCHOOL INFO CHECKBOX
    
    
    
    def click_first_name(self):
        self.click(self.FIRST_NAME)
    
    def click_last_name(self):
        self.click(self.LAST_NAME)
    
    def click_additional_name(self):
        self.click(self.ADDITIONAL_NAME)
    
    def click_headline(self):
        self.click(self.HEADLINE)
    
    def click_industry(self):
        self.click(self.INDUSTRY)
    
    def click_school(self):
        self.click(self.SCHOOL)
    
    def click_add_new_education(self):
        self.click(self.ADD_NEW_EDUCATION_BUTTON)
    
    def click_location(self):
        self.click(self.LOCATION)
    
    def click_city(self):
        self.click(self.CITY)  
    
    