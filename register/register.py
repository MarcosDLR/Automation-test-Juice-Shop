import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import random
class register_user(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")
        time.sleep(3)

    def test_register(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
        validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if validatePoppup.is_displayed() == True:
            validatePoppup.click()
        result = False
        self.driver.find_element(By.XPATH,'//*[@id="navbarAccount"]').click()
        self.driver.find_element(By.XPATH,'//*[@id="navbarLoginButton"]').click()
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="newCustomerLink"]/a')))
        self.driver.find_element(By.XPATH,'//*[@id="newCustomerLink"]/a').click()
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.ID, 'emailControl')))
        user = "test"+ str(random.random()) +"@gmail.com"
        password = "Just a test"
        self.driver.find_element(By.ID,'emailControl').send_keys(user)
        self.driver.find_element(By.ID,'passwordControl').send_keys(password)
        self.driver.find_element(By.ID,'repeatPasswordControl').send_keys(password)
        self.driver.find_element(By.XPATH,'//*[@id="registration-form"]/div[1]/mat-form-field[1]/div/div[1]/div[3]').click()
        self.driver.find_elements(By.TAG_NAME,'mat-option')[1].click()
        self.driver.find_element(By.ID,'securityAnswerControl').send_keys("Just a test")
        self.driver.find_element(By.ID,'registerButton').click()
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1')))
        self.driver.find_element(By.ID,'email').send_keys(user)
        self.driver.find_element(By.ID,'password').send_keys(password)
        self.driver.find_element(By.ID,'loginButton').click()
        validate_error = self.validate_is_exist(By.CLASS_NAME,'error')
        if validate_error == False:
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