import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class DrawerMenu(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")

    def test_btn_drawer_exist(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
        validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if validatePoppup.is_displayed() == True:
            validatePoppup.click()
        value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]/span[1]")
        self.assertTrue(value,"Validate if button drawer exist")
    
    def test_btn_drawer_exist_content(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
        validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if validatePoppup.is_displayed() == True:
            validatePoppup.click()
        result = False
        value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]/span[1]")
        print(value)
        if value == True:
            self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]").click()
            time.sleep(1)
            sessions = self.driver.find_elements(By.CLASS_NAME,"side-subHeader")
            content_list = self.driver.find_elements(By.CLASS_NAME,"mat-list-item-content")
            if len(sessions) == 3 and len(content_list) == 6:
                result = True
        self.assertTrue(result,"Validate if drawer content")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def validate_is_exist(self, how, what):
        try: displayed = self.driver.find_element(by=how, value=what).is_displayed()
        except NoSuchElementException: return False
        return displayed

if __name__ == '__main__':
    unittest.main()