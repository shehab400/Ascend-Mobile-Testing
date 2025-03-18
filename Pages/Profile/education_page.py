from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import AddEditEducationPageLocaters  # Import LoginLocators

class EducationPage(BasePage):
    """ Page Object for Login Page """
    SCHOOL_TEXT_BOX = AddEditEducationPageLocaters.SCHOOL_TEXT_BOX
    DEGREE_TEXT_BOX = AddEditEducationPageLocaters.DEGREE_TEXT_BOX
    FIELD_OF_STUDY_TEXT_BOX = AddEditEducationPageLocaters.FIELD_OF_STUDY_TEXT_BOX
    START_DATE = AddEditEducationPageLocaters.START_DATE
    END_DATE = AddEditEducationPageLocaters.END_DATE
    GRADE_TEXT_BOX = AddEditEducationPageLocaters.GRADE_TEXT_BOX
    ACTIVITIES_TEXT_BOX = AddEditEducationPageLocaters.ACTIVITIES_TEXT_BOX
    DESCRIPTION_TEXT_BOX = AddEditEducationPageLocaters.DESCRIPTION_TEXT_BOX
    SAVE_BUTTON = AddEditEducationPageLocaters.SAVE_BUTTON
    ADD_SKILLS_BUTTON = AddEditEducationPageLocaters.ADD_SKILLS_BUTTON
    ADD_MEDIA_BUTTON = AddEditEducationPageLocaters.ADD_MEDIA_BUTTON
    
    
    def enter_school(self, school):
        self.send_keys(self.SCHOOL_TEXT_BOX, school)
    
    def enter_degree(self, degree):
        self.send_keys(self.DEGREE_TEXT_BOX, degree)
    
    def enter_field_of_study(self, field_of_study):
        self.send_keys(self.FIELD_OF_STUDY_TEXT_BOX, field_of_study)
    
    def enter_start_date(self, start_date):
        self.send_keys(self.START_DATE, start_date)
    
    def enter_end_date(self, end_date):
        self.send_keys(self.END_DATE, end_date)
    
    def enter_grade(self, grade):
        self.send_keys(self.GRADE_TEXT_BOX, grade)
    
    
    def enter_activities(self, activities):
        self.send_keys(self.ACTIVITIES_TEXT_BOX, activities)
    
    def enter_description(self, description):
        self.send_keys(self.DESCRIPTION_TEXT_BOX, description)
    
    def click_save(self):
        self.click(self.SAVE_BUTTON)
    
    def click_add_skills(self):
        self.click(self.ADD_SKILLS_BUTTON)
    
    def click_add_media(self):
        self.click(self.ADD_MEDIA_BUTTON)
    
    
    def get_message(self):
        return self.get_text(self.MESSAGE)
    