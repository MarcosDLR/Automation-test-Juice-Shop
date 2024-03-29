import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from globalMethos import globalMethos

class Navbar(globalMethos):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)
    
    def get_logo(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[2]/span[1]/img")
    
    def get_name(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[2]/span[1]/span")
    
    def get_btn_serch(self):
        return self.driver.find_element(By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')
    
    def get_btn_lenguaje(self):
        return self.driver.find_element(By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]')
    
    def get_btn_change_account(self):
        return self.driver.find_element(By.XPATH, '//*[@id="navbarAccount"]')


    def validate_logo(self):
        return super().validate_is_exist(self.get_logo())

    def validate_name(self):
        return super().validate_is_exist(self.get_name())

    def validate_btn_search(self):
        return super().validate_is_exist(self.get_btn_serch())

    def validate_btn_lenguage(self):
        return super().validate_is_exist(self.get_btn_lenguaje())

    def validate_btn_change_account(self):
        return super().validate_is_exist(self.get_btn_change_account())
    
