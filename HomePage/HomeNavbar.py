import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
class HomeNavbar(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(3)

    def test_validate_logo(self):
        value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[2]/span[1]/img")
        self.assertTrue(value,"Validate logo")

    def test_validate_name(self):
        value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[2]/span[1]/span")
        self.assertTrue(value,"Validate name")

    def test_validate_btn_search(self):
        value = self.validate_is_exist(By.XPATH,'//*[@id="searchQuery"]/span/mat-icon[2]')
        self.assertTrue(value,"Validate btn search")

    def test_validate_btn_lenguage(self):
        value = self.validate_is_exist(By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]')
        self.assertTrue(value,"Validate btn lenguage")

    def test_validate_btn_change_account(self):
        value = self.validate_is_exist(By.XPATH,'//*[@id="navbarAccount"]')
        self.assertTrue(value,"Validate btn account")

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def validate_is_exist(self, how, what):
        try: displayed = self.driver.find_element(by=how, value=what).is_displayed()
        except NoSuchElementException: return False
        return displayed

if __name__ == '__main__':
    unittest.main()