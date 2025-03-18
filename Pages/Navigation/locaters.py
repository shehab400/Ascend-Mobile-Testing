from appium.webdriver.common.appiumby import AppiumBy as By

class SideBarLocators:
    MYPROFILE_BUTTON = (By.ID, 'com.linkedin.android:id/identity_mirror_component_profile_name')
    SETTINGS_BUTTON = (By.ID, 'com.linkedin.android:id/home_nav_premium_upsell_text_view')
    SIGNOUT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("sign_out")')
    CONFIRM_SIGNOUT = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/growth_login_remember_me_pre_logout_bottomsheet_negative_option")')
    CONFIRM_SIGNOUT_2 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')