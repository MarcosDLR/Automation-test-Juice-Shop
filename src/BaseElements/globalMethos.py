from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class globalMethos:
    def __init__(self,driver):
        self.driver = driver
    
    def wait_element(self, how, what):
        return WebDriverWait(self.driver, 200).until(EC.presence_of_element_located((how, what)))

    def click_button(self,element):
        element.click()

    def validate_is_exist(self, element):
        try: displayed = element.is_displayed()
        except NoSuchElementException: return False
        return displayed
