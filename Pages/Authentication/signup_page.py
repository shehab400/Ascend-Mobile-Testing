from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Authentication.locaters import SignupLocators  # Import SignupLocators

class SignupPage(BasePage):
    """ Page Object for Signup Page """
    FIRSTNAME_FIELD = SignupLocators.FIRSTNAME_FIELD
    LASTNAME_FIELD = SignupLocators.LASTNAME_FIELD
    EMAIL_FIELD = SignupLocators.EMAIL_FIELD
    PASSWORD_FIELD = SignupLocators.PASSWORD_FIELD
    CONTINUE_BUTTON = SignupLocators.CONTINUE_BUTTON
    MESSAGE = ''
    INVALID_EMAIL = SignupLocators.INVALID_EMAIL
    INVALID_PASSWORD = SignupLocators.INVALID_PASSWORD
    EXISTING_EMAIL = SignupLocators.EXISTING_EMAIL

    def enter_first_name(self, first_name):
        self.click(self.FIRSTNAME_FIELD)
        self.send_keys(self.FIRSTNAME_FIELD, first_name)
     
    def enter_last_name(self, last_name):
        self.click(self.LASTNAME_FIELD)
        self.send_keys(self.LASTNAME_FIELD, last_name)
    
    def enter_email(self, email):
        self.click(self.EMAIL_FIELD)
        self.send_keys(self.EMAIL_FIELD, email)
        print("✅ Entered Email")

    def enter_password(self, password):
        self.click(self.PASSWORD_FIELD)
        self.send_keys(self.PASSWORD_FIELD, password)
        print("✅ Entered Password")

    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)
