import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from globalMethos import globalMethos
import random

class Login:

    def __init__(self,driver):
        self.driver = driver
        self.popup = '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]'
        self.card_login = '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1'
        self.global_methods = globalMethos(self.driver)
    
    def get_popup_init(self):
        return self.driver.find_element(By.XPATH, self.popup)
    
    def get_btn_account(self):
        return self.driver.find_element(By.XPATH, By.XPATH,'//*[@id="navbarAccount"]')
    
    def get_btn_login(self):
        return self.driver.find_element(By.XPATH, By.XPATH,'//*[@id="navbarLoginButton"]')
    
    def get_login_card(self):
        return self.driver.find_element(By.XPATH, self.card_login)
    
    def get_email_input(self):
        return self.driver.find_element(By.ID, 'email')
    
    def get_password_input(self):
        return self.driver.find_element(By.ID, 'password')
    
    def get_login_summit(self):
        return self.driver.find_element(By.ID, 'loginButton')
    
    def errorClass(self):
        return self.driver.find_element(By.CLASS_NAME, 'error')
    
    def test_login_incorrect(self):
        """
            Hacer login y verificar si sale el mensaje de error  que dice:

            'Invalid email or password.'
        """
        boton = self.global_methods.wait_element(By.XPATH, self.popup)
        self.global_methods.click_button(boton)
        result = False
        self.global_methods.click_button(self.get_btn_account())
        self.global_methods.click_button(self.get_btn_login())
        user = "test"+ str(random.random()) +"@gmail.com"
        password = "Just a test"
        self.global_methods.wait_element(By.XPATH, self.card_login)
        self.get_email_input().send_keys(user)
        self.get_password_input().send_keys(password)
        self.global_methods.click_button(self.get_login_summit())
        if self.validate_is_exist(self.errorClass()) == True:
            if self.errorClass().text == "Invalid email or password.":
                result = True
        return result