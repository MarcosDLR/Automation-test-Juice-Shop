import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from globalMethos import globalMethos
import random
from selenium.common.exceptions import NoSuchElementException

class Register(globalMethos):

    def __init__(self,driver):
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        self.card_login = (By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1')
        self.customer_link = (By.XPATH, '//*[@id="newCustomerLink"]/a')
        self.error_message = (By.CLASS_NAME, 'error')
        self.email_control = (By.ID, 'emailControl')
        super().__init__(driver)

    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_btn_account(self):
        return self.driver.find_element(By.XPATH,'//*[@id="navbarAccount"]')
    
    def get_btn_login(self):
        return self.driver.find_element(By.XPATH,'//*[@id="navbarLoginButton"]')
    
    def get_customer_link(self):
        return self.driver.find_element(*self.customer_link)
    
    def get_btn_password_control(self):
        return self.driver.find_element(By.ID,'passwordControl')
    
    def get_btn_password_repeat_control(self):
        return self.driver.find_element(By.ID,'repeatPasswordControl')

    def get_registration_form(self):
        return self.driver.find_element(By.XPATH,'//*[@id="registration-form"]/div[1]/mat-form-field[1]/div/div[1]/div[3]')
    
    def get_registration_options(self):
        return self.driver.find_elements(By.TAG_NAME,'mat-option')
    
    def get_security_answer(self):
        return self.driver.find_element(By.ID,'securityAnswerControl')
    
    def get_registration_btn(self):
        return self.driver.find_element(By.ID,'registerButton')
    
    def get_email_input(self):
        return self.driver.find_element(By.ID,'email')
    
    def get_password_input(self):
        return self.driver.find_element(By.ID,'password')
    
    def get_login_btn(self):
        return self.driver.find_element(By.ID,'loginButton')
    
    def errorClass(self):
        return self.driver.find_element(*self.error_message)

    def test_register(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        super().click_button(self.get_btn_account())
        super().click_button(self.get_btn_login())
        boton_customer = super().wait_element(*self.customer_link)
        super().click_button(boton_customer)

        email_control = super().wait_element(*self.email_control)
        user = "test"+ str(random.random()) +"@gmail.com"
        password = "Just a test"
        email_control.send_keys(user)

        self.get_btn_password_control().send_keys(password)
        self.get_btn_password_repeat_control().send_keys(password)
        super().click_button(self.get_registration_form())
        super().click_button(self.get_registration_options()[1])
        self.get_security_answer().send_keys("Just a test")
        self.get_registration_btn().click()
        super().wait_element(*self.card_login)

        self.get_email_input().send_keys(user)
        self.get_password_input().send_keys(password)
        super().click_button(self.get_login_btn())
        
        try:
            if super().validate_is_exist(self.errorClass()):
                return False
            else:
                return True
        except NoSuchElementException: return True
