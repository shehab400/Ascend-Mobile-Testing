from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.Authentication.locaters import ForgotpassLocaters  # Import ForgotpassLocaters

class ForgotPassword(BasePage):
    """ Page Object for Login Page """
    
    EMAIL_FIELD = ForgotpassLocaters.EMAIL_FIELD
    NEXT_BUTTON = ForgotpassLocaters.NEXT_BUTTON
    VERFICATOIN_CODE = ForgotpassLocaters.VERFICATOIN_CODE
    RESEND_CODE = ForgotpassLocaters.RESEND_CODE
    SUBMIT_BUTTON = ForgotpassLocaters.SUBMIT_BUTTON
    CHANGE_MAIL = ForgotpassLocaters.CHANGE_MAIL
  

    def enter_email(self, email):
        self.click(self.EMAIL_FIELD)
        self.send_keys(self.EMAIL_FIELD, email)
  
    def click_next(self):
        self.click(self.NEXT_BUTTON)

    def click_resend_code(self):
        self.click(self.RESEND_CODE)
    
    def click_submit(self):
        self.click(self.SUBMIT_BUTTON)
    
    def click_change_mail(self):
        self.click(self.CHANGE_MAIL)
        
    def enter_verification_code(self, code):
        self.click(self.VERFICATOIN_CODE)
        self.send_keys(self.VERFICATOIN_CODE,code)
       
          
    def get_message(self):
        return self.get_text(self.MESSAGE)
    