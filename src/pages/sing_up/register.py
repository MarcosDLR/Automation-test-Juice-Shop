import sys
sys.path.append("src/BaseElements")
from globalMethods import GlobalMethods
from singletonMeta import SingletonMeta
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class Register(GlobalMethods,metaclass=SingletonMeta):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        self.card_login = (By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-login/div/mat-card/h1')
        self.customer_link = (By.XPATH, '//*[@id="newCustomerLink"]/a')
        self.btn_login = (By.XPATH, '//*[@id="navbarLoginButton"]')
        self.error_message = (By.CLASS_NAME, 'error')
        self.email_control = (By.ID, 'emailControl')

    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_btn_account(self):
        return self.driver.find_element(By.XPATH, '//*[@id="navbarAccount"]')
    
    def get_btn_login(self):
        return self.driver.find_element(*self.btn_login)
    
    def get_customer_link(self):
        return self.driver.find_element(*self.customer_link)
    
    def get_btn_password_control(self):
        return self.driver.find_element(By.ID, 'passwordControl')
    
    def get_btn_password_repeat_control(self):
        return self.driver.find_element(By.ID, 'repeatPasswordControl')

    def get_registration_form(self):
        return self.driver.find_element(By.XPATH,'//*[@id="registration-form"]/div[1]/mat-form-field[1]/div/div[1]/div[3]')
    
    def get_registration_options(self):
        return self.driver.find_elements(By.TAG_NAME, 'mat-option')
    
    def get_security_answer(self):
        return self.driver.find_element(By.ID, 'securityAnswerControl')
    
    def get_registration_btn(self):
        return self.driver.find_element(By.ID, 'registerButton')
    
    def get_email_input(self):
        return self.driver.find_element(By.ID, 'email')
    
    def get_password_input(self):
        return self.driver.find_element(By.ID, 'password')
    
    def get_login_btn(self):
        return self.driver.find_element(By.ID, 'loginButton')
    
    def errorClass(self):
        return self.driver.find_element(*self.error_message)
    
    def remove_popup_init(self):
        button = super().wait_element(*self.popup)
        super().click_button(button)
    
    def click_account_btn(self):
        super().click_button(self.get_btn_account())
    
    def click_login_btn(self):
        btn = super().wait_element(*self.btn_login)
        super().click_button(btn)
    
    def btn_customer(self):
        button_customer = super().wait_element(*self.customer_link)
        super().click_button(button_customer)
    
    def set_user(self, value):
        email_control = super().wait_element(*self.email_control)
        email_control.send_keys(value)
    
    def set_password_and_repeat(self, value):
        self.get_btn_password_control().send_keys(value)
        self.get_btn_password_repeat_control().send_keys(value)
    
    def click_register_form(self):
        super().click_button(self.get_registration_form())
    
    def click_register_options(self):
        super().click_button(self.get_registration_options()[1])
    
    def set_security_answer(self, value):
        self.get_security_answer().send_keys(value)
        self.get_registration_btn().click()
    
    def wait_login_card(self):
        super().wait_element(*self.card_login)
    
    def set_email_input(self, value):
        self.get_email_input().send_keys(value)
    
    def set_password_input(self, value):
        self.get_password_input().send_keys(value)

    def click_login_btn_form(self):
        super().click_button(self.get_login_btn())

    def test_register(self):
        try:
            if super().validate_is_exist(self.errorClass()):
                return False
            else:
                return True
        except NoSuchElementException: return True
