import os
from singletonMeta import SingletonMeta 
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class GlobalMethos(metaclass=SingletonMeta):


    def __init__(self,driver):
        self.driver = driver
    
    def wait_element(self, how, what):
        return WebDriverWait(self.driver, 200) \
        .until(EC.presence_of_element_located((how, what)))

    def click_button(self, element):
        element.click()

    def validate_is_exist(self, element):
        try: displayed = element.is_displayed()
        except NoSuchElementException: return False
        return displayed

    def take_screenshot(driver, module, name):
        directory = os.getcwd() + "/screenshots/" + module
        if not os.path.exists(directory):
            os.makedirs(directory)

        file_name = f"{name}.png"
        file_path = f"{directory}/{file_name}"
        
        driver.save_screenshot(file_path)