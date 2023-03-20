import sys
from selenium.webdriver.common.by import By
from globalMethos import GlobalMethos

sys.path.append("src/BaseElements")

class DrawerMenu(GlobalMethos): 


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"] \
                      /app-welcome-banner/div/div[2]/button[2]')
        self.subHeader = (By.CLASS_NAME, 'side-subHeader')
    
    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_btn_drawer(self):
        return self.driver.find_element(By.XPATH, '/html/body/app-root \
                                        /div/mat-sidenav-container/mat-sidenav-content/app-navbar/ \
                                        mat-toolbar/mat-toolbar-row/button[1]/span[1]')
    
    def get_sub_header(self):
        return self.driver.find_elements(*self.subHeader)
    
    def get_list_content(self):
        return self.driver.find_elements(By.CLASS_NAME, 'mat-list-item-content')

    def close_popup_init(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
    
    def validate_drawer_displed(self):
        return super().validate_is_exist(self.get_btn_drawer())
    
    def click_drawer(self):
        super().click_button(self.get_btn_drawer())
    
    def wait_header(self):
        super().wait_element(*self.subHeader)

    def validate_btn_drawer_exist(self):
        """Validar si el boton del drawer existe"""
        super().validate_is_exist(self.get_btn_drawer())
        return super().validate_is_exist(self.get_btn_drawer())
    
    def test_btn_drawer_exist_content(self):
        """Validar si el drawer tiene contenido

            Nota: Primero quitamos el popup que aparece en el principio, luego
            Le damos click al botón que se encuentra en el navbar y luego
            verificamos la cantidad de elementos que hay en el drawer
        """
        if len(self.get_sub_header()) == 3 and \
        len(self.get_list_content()) == 6:
            return True
        else:
            return False