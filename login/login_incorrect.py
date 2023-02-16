import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
class login_incorrect(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(3)

    def test_login_incorrect(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
        validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if validatePoppup.is_displayed() == True:
            validatePoppup.click()
        result = False
        self.driver.find_element(By.XPATH,'//*[@id="navbarAccount"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="navbarLoginButton"]').click()
        user = "test"+ str(random.random()) +"@gmail.com"
        password = "Just a test"
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1')))
        self.driver.find_element(By.ID,'email').send_keys(user)
        self.driver.find_element(By.ID,'password').send_keys(password)
        self.driver.find_element(By.ID,'loginButton').click()
        time.sleep(1)
        validate_error = self.validate_is_exist(By.CLASS_NAME,'error')
        if validate_error == True:
            if self.driver.find_element(By.CLASS_NAME,'error').text == "Invalid email or password.":
                result = True
        self.assertTrue(result)


    @classmethod
    def tearDown(self):
        self.driver.quit()

    def validate_is_exist(self, how, what):
        try: displayed = self.driver.find_element(by=how, value=what).is_displayed()
        except NoSuchElementException: return False
        return displayed

if __name__ == '__main__':
    unittest.main()