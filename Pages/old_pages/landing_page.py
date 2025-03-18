from appium.webdriver.common.appiumby import AppiumBy as By  # Import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage  # Import your base page class

class WelcomePage(BasePage):
    """Handles the welcome screen popups"""

    AGREE_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/positive_button")')  # Update with correct ID
    ALLOW_NOTIFICATIONS_BUTTON = (By.XPATH ,("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"))  # Android example
    JOIN_NOW_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_prereg_fragment_join_button_primary")')  # Update with correct ID

    def handle_initial_popups(self):
        """Click Agree and Allow Notifications if they appear"""
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.AGREE_BUTTON)).click()
            print("✅ Clicked 'Agree to Terms'")
        except:
            print("⚠️ 'Agree to Terms' not found, skipping")

        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.ALLOW_NOTIFICATIONS_BUTTON)).click()
            print("✅ Clicked 'Allow Notifications'")
        except:
            print("⚠️ 'Allow Notifications' not found, skipping")
        
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.JOIN_NOW_BUTTON)).click()
            print("✅ Clicked 'Join Now'")
        except:
            print("⚠️ 'Join Now' not found, skipping")
