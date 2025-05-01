from appium.webdriver.common.appiumby import AppiumBy as By

class HomeLocators:
    SIDEBAR_BUTTON = (By.ACCESSIBILITY_ID, 'My Profile and Communities')
    WELCOME_MESSAGE = (By.ID, 'com.linkedin.android:id/summary_header')
    CLOSE_BUTTON = (By.ACCESSIBILITY_ID, 'Close')
    SEARCH_BAR = (By.ID, 'com.linkedin.android:id/search_bar') 
    SEARCH_BAR_SEND_TEXT = (By.ID, 'com.linkedin.android:id/search_bar_edit_text')
    MESSAGING_BUTTON =  (By.ID, 'com.linkedin.android:id/home_messaging')
    VIEW_THE_FULL_POST = (By.ID, 'com.linkedin.android:id/feed_render_item_text') #to click on post to view all engagments 
    REACTIONS_COUNT = (By.ID , 'com.linkedin.android:id/feed_conversations_reactions_count')# you can view a;; the post and engagments via clicking on it
    LIKE_BUTTON = (By.ACCESSIBILITY_ID, 'Like') 
    LIKE_BUTTON1 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/feed_social_actions_like").instance(0)')# IN CASE OF MORE THAN ONE [OST]
    
    #ADD LOVE , CLELEBRATE , INSIGHTFUL , CURIOUS , SUPPORTIVE , FUNNY , INTERESTED BUTTONS
    COMMENT_BUTTON = (By.ACCESSIBILITY_ID, 'Comment')
    SHARE_BUTTON = (By.ACCESSIBILITY_ID, 'Send')
    VIEW_PROFILE_FROM_POST_BUTTON = (By.ID, 'com.linkedin.android:id/feed_actor_image')
    POST_OPTIONS = (By.ACCESSIBILITY_ID, 'Post options')
    SAVE_POST_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/feed_control_panel_container").instance(0)')
    SHARE_VIA_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/feed_control_panel_container").instance(1)')
    REPORT_POST_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/feed_control_panel_container").instance(4)')
    WRITE_POST = (By.ID , 'com.linkedin.android:id/share_compose_text_input_entities')
    ADD_PHOTO_TO_POST = (By.ACCESSIBILITY_ID, 'Photo')
    MORE_BUTTON = (By.ACCESSIBILITY_ID, 'More')
    ADD_EVENT_TO_POST = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/detour_icon").instance(1)')
    ADD_JOB_TO_POST = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/detour_icon").instance(3)')
    ADD_DOCUMENT_TO_POST = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/detour_icon").instance(5)')
    CHOOSE_DOCUMENT_FILE = (By.ID , 'com.linkedin.android:id/choose_document')
    WRITE_DOCUMENT_TITLE = (By.ID , 'com.linkedin.android:id/document_title')
    DOCUMENT_FILE  = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.documentsui:id/icon_thumb").instance(0)')
    NEXT_BUTTON = (By.ID , 'com.linkedin.android:id/document_detour_toolbar_next_button')
    POST_BUTTON = (By.ID , 'com.linkedin.android:id/share_compose_post_button')
    POST_INFO = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/feed_actor_info_container").instance(0)')
    POST_UPLOADED_SUCCESFUL_MESSAGE = (By.ID, 'com.linkedin.android:id/ad_banner_action_button')
    COMMENTS_AND_REPOST_COUNT = (By.ID, 'com.linkedin.android:id/feed_reactions_count')
    WRITE_COMMENT = (By.ID, 'com.linkedin.android:id/comment_bar_edit_text')
    TAG_USER_BUTTON = (By.ID, 'com.linkedin.android:id/feed_actor_info_container')
    VIEW_SAVED_POSTS = (By.ID, 'com.linkedin.android:id/ad_banner_action_button')
    EDIT_SAVED_POSTS = (By.ACCESSIBILITY_ID, 'More actions')
    UNSAVE_POST_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.linkedin.android:id/bottom_sheet_container").instance(0)')
    DISSMISS_BUTTON0 = (By.ID, 'com.linkedin.android:id/search_filter_name')
    # SIDEBAR BUTTONS
    EMPTY_POSTS_MESSAGE =(By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Posts")')
    NOTIFICATION_FREEZE_BUTTON = (By.ID, 'ccom.linkedin.android:id/push_re_enable_bottomsheet_neg_btn')
    ADD_IMAGE_BUTOTN = (By.ID, 'com.google.android.providers.media.module:id/button_add')
    NEXT_BUTTON2 = (By.ID, 'com.linkedin.android:id/media_editor_next_button')
    POST_COMMENT_BUTTON = (By.ID, 'com.linkedin.android:id/comment_box_toolbar_post_button')