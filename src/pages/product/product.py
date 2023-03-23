import sys
import time
sys.path.append("src/BaseElements")
from globalMethos import GlobalMethos
from singletonMeta import SingletonMeta
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Product(GlobalMethos,metaclass=SingletonMeta): 


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/ \
                      app-welcome-banner/div/div[2]/button[2]')
        self.search_bar = (By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')
        self.search_bar_input = (By.XPATH, '//*[@id="mat-input-0"]')
        self.search_result = (By.XPATH, "/html/body/app-root/ \
                              div/mat-sidenav-container \
                              /mat-sidenav-content/app- \
                              search-result/div/div/mat-card")
        self.product_list = (By.TAG_NAME, 'mat-grid-tile')
        self.product_image = (By.CLASS_NAME, 'img-container')
        self.product_title = (By.CLASS_NAME, 'item-name')
        self.product_expantion_panel = (By.TAG_NAME, 'mat-expansion-panel-header')

    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_search_bar_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
    
    def get_search_result(self):
        return self.driver.find_element(*self.search_result)
    
    def get_products_list(self):
        return self.driver.find_elements(*self.product_list)
    
    def get_result(self):
        return self.driver.find_elemet(By.XPATH, '/html/body/app-root/div/mat-sidenav-container/ \
                                       mat-sidenav-content/app-search-result/div/div/div[2]')
    
    def get_product_image(self):
        return self.driver.find_elemet(*self.product_image)
    
    def get_expantion_panel(self):
        return self.driver.find_element(*self.product_expantion_panel)
    
    def remove_popup_init(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
    
    def click_search_bar(self):
        search_bar_btn = super().wait_element(*self.search_bar)
        super().click_button(search_bar_btn)

    def wait_search_bar(self):
        super().wait_element(*self.search_bar_input)
    
    def click_search_bar_input(self):
        self.get_search_bar_input().click()
    
    def set_text_in_search_bar(self, value):
        self.get_search_bar_input().send_keys(value)
    
    def press_enter_in_serach_bar(self):
        self.get_search_bar_input().send_keys(Keys.ENTER)
        time.sleep(3)
    
    def validate_products(self):
        if(len(self.get_products_list()) > 0):    
            return True
        else:
            return False

    def validate_products_image(self):
        if(len(self.get_products_list()) > 0):
            return self.get_products_list()[0] \
            .find_element(*self.product_image).is_displayed()
        else:
            return False
    
    def validate_products_title(self):
        if(len(self.get_products_list()) > 0):
            return self.get_products_list()[0]\
            .find_element(*self.product_title).is_displayed()
        else:
            return False

    def click_product_title(self):
        self.get_products_list()[0]\
        .find_element(*self.product_title).click()

    def wait_expanded_products(self):
        super().wait_element(*self.product_expantion_panel)
        time.sleep(2)
    
    def click_btn_expanded(self):
        super().click_button(self.get_expantion_panel())
    
    def find_reviews(self):
        list = self.driver.find_elements(By.CLASS_NAME, 'comment')
        if len(list) >= 1:
            return True
        else:
            return False
        
    def find_empty_reviews(self):
        if len(list) <= 0:
            return True
        else:
            return False
        