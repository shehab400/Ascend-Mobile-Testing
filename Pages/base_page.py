from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        """ Initialize the BasePage with the Appium driver """
        self.driver = driver

    def find_element(self, locator, timeout=10):
        """ Wait for an element to be present and return it """
        return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator))
    def click(self, locator):
        """ Click an element after waiting for it to be visible """
        element = self.find_element(locator)
        element.click()

    def send_keys(self, locator, text):
        """ Find an element and enter text into it """
        element = self.find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        """ Get text from an element """
        return self.find_element(locator).text
