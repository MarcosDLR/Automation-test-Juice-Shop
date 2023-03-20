import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from globalMethos import globalMethos

class Lenguaje(globalMethos):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')

    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_sidenav_content(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]")
    
    def get_actual_lenguaje(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]/span[1]/span")
    
    def get_lenguaje_list(self):
        return self.driver.find_elements(By.TAG_NAME, "mat-radio-button")

    def test_lenguage_change(self):
        """
            Cambiar el lenguaje de la página
        """
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        value = super().validate_is_exist(self.get_sidenav_content())
        if value == True:
            actual_lenguage = self.get_actual_lenguaje().text
            self.get_sidenav_content().click()
            list_lenguages = self.get_lenguaje_list()
            if len(list_lenguages) > 0:
                list_lenguages[0].click()
                new_lenguage = self.get_actual_lenguaje().text
        if actual_lenguage == new_lenguage:
            return False
        else:
            return True