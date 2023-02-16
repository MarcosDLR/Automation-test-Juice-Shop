import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class lenguage_test(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(3)

    def test_lenguage_change(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
        validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if validatePoppup.is_displayed() == True:
            validatePoppup.click()
        value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]")
        if value == True:
            actual_lenguage = self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]/span[1]/span").text
            print(actual_lenguage)
            self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]").click()
            list_lenguages = self.driver.find_elements(By.TAG_NAME,"mat-radio-button")
            if len(list_lenguages) > 0:
                list_lenguages[0].click()
                new_lenguage = self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]/span[1]/span").text
                print(new_lenguage)
        self.assertNotEquals(actual_lenguage,new_lenguage)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def validate_is_exist(self, how, what):
        try: displayed = self.driver.find_element(by=how, value=what).is_displayed()
        except NoSuchElementException: return False
        return displayed

if __name__ == '__main__':
    unittest.main()