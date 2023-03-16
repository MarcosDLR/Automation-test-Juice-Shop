import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from globalMethos import globalMethos
import random

class Login(globalMethos):

    def __init__(self,driver):
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        self.card_login = (By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1')
        self.error_message = (By.CLASS_NAME, 'error')
        super().__init__(driver)
    
    def get_btn_account(self):
        return self.driver.find_element(By.XPATH,'//*[@id="navbarAccount"]')
    
    def get_btn_login(self):
        return self.driver.find_element(By.XPATH,'//*[@id="navbarLoginButton"]')
    
    def get_login_card(self):
        return self.driver.find_element(*self.card_login)
    
    def get_email_input(self):
        return self.driver.find_element(By.ID, 'email')
    
    def get_password_input(self):
        return self.driver.find_element(By.ID, 'password')
    
    def get_login_summit(self):
        return self.driver.find_element(By.ID, 'loginButton')
    
    def errorClass(self):
        return self.driver.find_element(*self.error_message)
    
    def test_login_incorrect(self):
        """
            Hacer login y verificar si sale el mensaje de error  que dice:

            'Invalid email or password.'
        """
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        result = False
        super().click_button(self.get_btn_account())
        super().click_button(self.get_btn_login())
        user = "test"+ str(random.random()) +"@gmail.com"
        password = "Just a test"
        super().wait_element(*self.card_login)
        self.get_email_input().send_keys(user)
        self.get_password_input().send_keys(password)
        super().click_button(self.get_login_summit())
        super().wait_element(*self.error_message)
        if super().validate_is_exist(self.errorClass()) == True:
            if self.errorClass().text == "Invalid email or password.":
                result = True
        return result