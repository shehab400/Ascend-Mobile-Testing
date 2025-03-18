from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Authentication.locaters import LoginLocators  # Import LoginLocators

class LoginPage(BasePage):
    """ Page Object for Login Page """
    
    EMAIL_FIELD = LoginLocators.EMAIL_FIELD
    PASSWORD_FIELD = LoginLocators.PASSWORD_FIELD
    SIGN_IN_GOOGLE = LoginLocators.SIGN_IN_GOOGLE
    GOOGLE_MAIL =   LoginLocators.GOOGLE_MAIL
    GOOGLE_PASSWORD = LoginLocators.GOOGLE_PASSWORD
    GOOGLE_NEXT_BUTTON = LoginLocators.GOOGLE_NEXT_BUTTON
    CONTINUE_BUTTON = LoginLocators.CONTINUE_BUTTON
    FORGOT_PASSWORD = LoginLocators.FORGOT_PASSWORD
    MESSAGE = LoginLocators.MESSAGE
    REMEMBER_ME = LoginLocators.REMEMBER_ME
    WELCOME_MESSAGE = LoginLocators.WELCOME_MESSAGE
    WRONG_PASSWORD_OR_EMAIL_MESSAGE = LoginLocators.WRONG_PASSWORD_OR_EMAIL_MESSAGE
    EMAIL_ADDRESS_IS_NOT_VALID = LoginLocators.EMAIL_ADDRESS_IS_NOT_VALID
    EMPTY_PASSWORD = LoginLocators.EMPTY_PASSWORD  
    JOIN_LINKEDIN = LoginLocators.JOIN_LINKEDIN
    #Facebook login is not working donot forget to add locators for facebook login

    def enter_email(self, email):
        self.click(self.EMAIL_FIELD)
        self.send_keys(self.EMAIL_FIELD, email)

    def enter_password(self, password):
        self.click(self.PASSWORD_FIELD) 
        self.send_keys(self.PASSWORD_FIELD, password)
        
    def click_continue(self):
        self.click(self.CONTINUE_BUTTON)

    def click_forgot_password(self):
        self.click(self.FORGOT_PASSWORD)
    
    def click_remember_me(self):
        self.click(self.REMEMBER_ME)
    
    def click_sign_in_google(self):
        self.click(self.SIGN_IN_GOOGLE)
    
    def enter_google_mail(self, email):
        self.click(self.GOOGLE_MAIL)
        self.send_keys(self.GOOGLE_MAIL, email)
    
    def enter_google_password(self, password):
        self.click(self.GOOGLE_PASSWORD)
        self.send_keys(self.GOOGLE_PASSWORD, password)

    def get_message(self):
        return self.get_text(self.MESSAGE)
    
    def click_join_linkedin(self):
        self.click(self.JOIN_LINKEDIN)