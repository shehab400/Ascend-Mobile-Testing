from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage
from Pages.old_pages.landing_page import WelcomePage

class SignupPage(BasePage):
    """ Page Object for Signup Page """
    
    FIRSTNAME_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_join_fragment_first_name")')
    LASTNAME_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_join_fragment_last_name")')
    EMAIL_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_login_join_fragment_email_address")')
    PASSWORD_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_login_join_fragment_password")')
    AGREE_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_join_fragment_join")')

    def enter_first_last_name(self, first_name, last_name):
        self.find_element(self.FIRSTNAME_FIELD).click()
        self.send_keys(self.FIRSTNAME_FIELD, first_name)
        self.find_element(self.LASTNAME_FIELD).click()
        self.send_keys(self.LASTNAME_FIELD, last_name)
        print("✅ Wrote 'First and Last Name'")
    
    def enter_email(self, email):
        self.find_element(self.EMAIL_FIELD).click()
        self.send_keys(self.EMAIL_FIELD, email)
        print("✅ Entered Email")

    def enter_password(self, password):
        self.find_element(self.PASSWORD_FIELD).click()
        self.send_keys(self.PASSWORD_FIELD, password)
        print("✅ Entered Password")

    def tap_agree(self):
        self.click(self.AGREE_BUTTON)
