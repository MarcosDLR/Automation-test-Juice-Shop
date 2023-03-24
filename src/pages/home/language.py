import sys
sys.path.append("src/BaseElements")
from globalMethods import GlobalMethods
from singletonMeta import SingletonMeta
from selenium.webdriver.common.by import By


class Language(GlobalMethods,metaclass=SingletonMeta):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')

    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_sideNav_content(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]")
    
    def get_actual_language(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/button[4]/span[1]/span")
    
    def get_language_list(self):
        return self.driver.find_elements(By.TAG_NAME, "mat-radio-button")
    
    def close_popup_init(self):
        button = super().wait_element(*self.popup)
        super().click_button(button)
    
    def sidenav_visible(self):
        return super().validate_is_exist(self.get_sideNav_content())
    
    def get_actual_language_in_page(self):
        return self.get_actual_language().text
    
    def click_sideNav(self):
        self.get_sideNav_content().click()
    
    def change_language(self):
        if len(self.get_language_list()) > 0:
            self.get_language_list()[0].click()

