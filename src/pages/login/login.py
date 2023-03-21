import sys
import random
from selenium.webdriver.common.by import By
from globalMethos import GlobalMethos

sys.path.append("src/BaseElements")

class Login(GlobalMethos):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"] \
                      /app-welcome-banner/div/div[2]/button[2]')
        self.card_login = (By.XPATH, '/html/body/app-root/div/ \
                           mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1')
        self.error_message = (By.CLASS_NAME, 'error')
    
    def get_btn_account(self):
        return self.driver.find_element(By.XPATH, '//*[@id="navbarAccount"]')
    
    def get_btn_login(self):
        return self.driver.find_element(By.XPATH, '//*[@id="navbarLoginButton"]')
    
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
    
    def remove_init_popup(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)

    def click_account_btn(self):
        super().click_button(self.get_btn_account())
    
    def click_login_btn(self):
        super().click_button(self.get_btn_login())
    
    def wait_login_card(self):
        super().wait_element(*self.card_login)
    
    def set_user_in_input(self):
        user = "test"+ str(random.random()) +"@gmail.com"
        self.get_email_input().send_keys(user)
    
    def set_password_in_input(self,value):
        self.get_password_input().send_keys(value)
    
    def click_login_summit(self):
        super().click_button(self.get_login_summit())
    
    def wait_login_error(self):
        super().wait_element(*self.error_message)
    
    def validate_error_login(self):
        if super().validate_is_exist(self.errorClass()) == True:
            if self.errorClass().text == "Invalid email or password.":
                return True
            else:
                return False