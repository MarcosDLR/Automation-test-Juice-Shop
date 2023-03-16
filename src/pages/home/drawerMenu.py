import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from globalMethos import globalMethos

class DrawerMenu(): 

    def __init__(self,driver):
        self.driver = driver
        self.popup = '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]'
        self.subHeader = 'side-subHeader'
        self.global_methods = globalMethos(self.driver)
    
    def get_popup_init(self):
        return self.driver.find_element(By.XPATH, self.popup)
    
    def get_btn_drawer(self):
        return self.driver.find_element(By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[1]/span[1]')
    
    def get_sub_header(self):
        return self.driver.find_elements(By.CLASS_NAME, self.subHeader)
    
    def get_list_content(self):
        return self.driver.find_elements(By.CLASS_NAME, 'mat-list-item-content')

    def validate_btn_drawer_exist(self):
        """
            Validar si el boton del drawer existe
        """

        boton = self.global_methods.wait_element(By.XPATH, self.popup)
        self.global_methods.click_button(boton)
        value = self.global_methods.validate_is_exist(self.get_btn_drawer())
        return value
    
    def test_btn_drawer_exist_content(self):
        """
            Validar si el drawer tiene contenido

            Nota: Primero quitamos el popup que aparece en el principio, luego
            Le damos click al botón que se encuentra en el navbar y luego
            verificamos la cantidad de elementos que hay en el drawer
        """
        boton = self.global_methods.wait_element(By.XPATH, self.popup)
        self.global_methods.click_button(boton)
        result = False
        btn_drawer = self.global_methods.validate_is_exist(self.get_btn_drawer())
        if btn_drawer == True:
            self.global_methods.click_button(self.get_btn_drawer())
            self.global_methods.wait_element(By.CLASS_NAME, self.subHeader)
            if len(self.get_sub_header()) == 3 and len(self.get_list_content()) == 6:
                result = True
        return result