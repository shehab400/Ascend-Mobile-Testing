from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from Pages.base_page import BasePage  # Import BasePage

class LoginPage(BasePage):
    """ Page Object for Login Page """
    
    FIRSTNAME_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_join_fragment_first_name")')
    LASTNAME_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_join_fragment_last_name")')
    PASSWORD_FIELD = (By.ID, "com.example:id/password")
    LOGIN_BUTTON = (By.ID, "com.example:id/login_button")
    WELCOME_MESSAGE = (By.ID, "com.example:id/welcome_message")

    def enter_username(self, username):
        self.send_keys(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    def tap_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_welcome_message(self):
        return self.get_text(self.WELCOME_MESSAGE)
