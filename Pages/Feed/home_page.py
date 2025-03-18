from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Feed.locaters import HomeLocators  # Import LoginLocators

class HomePage(BasePage):
    """ Page Object for Login Page """
    
    SIDEBAR_BUTTON = HomeLocators.SIDEBAR_BUTTON
    WELCOME_MESSAGE = HomeLocators.WELCOME_MESSAGE
    
    # def enter_email(self, email):
    #     self.click(self.EMAIL_FIELD)
    #     self.send_keys(self.EMAIL_FIELD, email)

    # def enter_password(self, password):
    #     self.click(self.PASSWORD_FIELD) 
    #     self.send_keys(self.PASSWORD_FIELD, password)
        
    def click_Sidebar(self):
        self.click(self.SIDEBAR_BUTTON)

    # def click_forgot_password(self):
    #     self.click(self.FORGOT_PASSWORD)
    
    # def click_remember_me(self):
    #     self.click(self.REMEMBER_ME)
    
    # def click_sign_in_google(self):
    #     self.click(self.SIGN_IN_GOOGLE)
    
    # def enter_google_mail(self, email):
    #     self.click(self.GOOGLE_MAIL)
    #     self.send_keys(self.GOOGLE_MAIL, email)
    
    # def enter_google_password(self, password):
    #     self.click(self.GOOGLE_PASSWORD)
    #     self.send_keys(self.GOOGLE_PASSWORD, password)

    def get_message(self):
        return self.get_text(self.MESSAGE)
    
        