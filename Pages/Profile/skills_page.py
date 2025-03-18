from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Profile.locaters import SkillsPageLocaters  # Import SkillsPageLocaters
from logger import logger
#not working due to entered skill issue (coludnt find the enter skill elment)
class SkillsPage(BasePage):
    """ Page Object for Skills Page """
    
    SKILL_TEXT_BOX = SkillsPageLocaters.SKILL_TEXT_BOX
    SKILL_TEXT_BOX_AFTER_CLICK = SkillsPageLocaters.SKILL_TEXT_BOX_AFTER_CLICK
    ENTERED_SKILL_BUTTON = None
    CLEAR_SKILL_BUTTON = SkillsPageLocaters.CLEAR_SKILL_BUTTON
    CHECKBOX_IS_SKILL_FROM_EDUCATION = SkillsPageLocaters.CHECKBOX_IS_SKILL_FROM_EDUCATION
    CHECKBOX_FOLLOW_THIS_SKILL = SkillsPageLocaters.CHECKBOX_FOLLOW_THIS_SKILL
    SAVE_BUTTON = SkillsPageLocaters.SAVE_BUTTON
    ADD_MORE_SKILLS_BUTTON = SkillsPageLocaters.ADD_MORE_SKILLS_BUTTON
    NO_THANKS_BUTTON = SkillsPageLocaters.NO_THANKS_BUTTON
    EDIT_SKILL_BUTTTON = SkillsPageLocaters.EDIT_SKILL_BUTTTON
    DELETE_SKILL_BUTTON = SkillsPageLocaters.DELETE_SKILL_BUTTON
    BACK_BUTTON = SkillsPageLocaters.BACK_BUTTON
    
    def get_message(self):
        return self.get_text(self.MESSAGE)
    
    def update_entered_skill_element(self, skill):
        self.ENTERED_SKILL_BUTTON = (By.XPATH, '//android.widget.TextView[contains(@resource-id, "com.linkedin.android:id/typeahead_text") and contains(@text, "{}")]'.format(skill))
        print(self.ENTERED_SKILL_BUTTON)
        logger.info("Updated entered skill element")
    
    def enter_skill(self, skill):
        self.click(self.SKILL_TEXT_BOX)
        self.send_keys(self.SKILL_TEXT_BOX_AFTER_CLICK, skill)
        self.update_entered_skill_element(skill)
        logger.info("Entered skill: {}".format(skill))
    
    def click_clear_skill(self):
        self.click(self.CLEAR_SKILL_BUTTON)
    
    def click_is_skill_from_education(self):
        self.click(self.CHECKBOX_IS_SKILL_FROM_EDUCATION)
    
    def click_follow_this_skill(self):
        self.click(self.CHECKBOX_FOLLOW_THIS_SKILL)
    
    def click_save(self):
        self.click(self.SAVE_BUTTON)
    
    def click_add_more_skills(self):
        self.click(self.ADD_MORE_SKILLS_BUTTON)
    
    def click_no_thanks(self):
        self.click(self.NO_THANKS_BUTTON)
    
    def click_edit_skill(self):
        self.click(self.EDIT_SKILL_BUTTTON)
    
    def click_delete_skill(self):
        self.click(self.DELETE_SKILL_BUTTON)
    
    def click_back(self):
        self.click(self.BACK_BUTTON)