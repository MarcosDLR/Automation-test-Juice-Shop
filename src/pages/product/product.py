import sys
sys.path.append("src/BaseElements")

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from globalMethos import globalMethos
import time
class Product(globalMethos): 

    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.popup = (By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        self.search_bar = (By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')
        self.search_bar_input = (By.XPATH, '//*[@id="mat-input-0"]')
        self.search_result = (By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-card")
        self.product_list = (By.TAG_NAME,'mat-grid-tile')
        self.product_image = (By.CLASS_NAME,'img-container')
        self.product_title = (By.CLASS_NAME,'item-name')
        self.product_expantion_panel = (By.TAG_NAME,'mat-expansion-panel-header')

    def get_popup_init(self):
        return self.driver.find_element(*self.popup)
    
    def get_search_bar_input(self):
        return self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')
    
    def get_search_result(self):
        return self.driver.find_element(*self.search_result)
    
    def get_products_list(self):
        return self.driver.find_elements(*self.product_list)
    
    def get_result(self):
        return self.driver.find_elemet(By.XPATH, '/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]')
    
    def get_product_image(self):
        return self.driver.find_elemet(*self.product_image)
    
    def get_expantion_panel(self):
        return self.driver.find_element(*self.product_expantion_panel)

    def product_search_finded(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        search_bar_btn = super().wait_element(*self.search_bar)
        super().click_button(search_bar_btn)
        super().wait_element(*self.search_bar_input)

        self.get_search_bar_input().click()
        self.get_search_bar_input().send_keys("Banana Juice")
        self.get_search_bar_input().send_keys(Keys.ENTER)
        time.sleep(2)
        if(len(self.get_products_list()) > 0):    
            return True
        else:
            return False
        
    def product_search_finded_image(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        search_bar_btn = super().wait_element(*self.search_bar)
        super().click_button(search_bar_btn)
        super().wait_element(*self.search_bar_input)

        self.get_search_bar_input().click()
        self.get_search_bar_input().send_keys("Banana Juice")
        self.get_search_bar_input().send_keys(Keys.ENTER)
        time.sleep(2)
        if(len(self.get_products_list()) > 0):
            return self.get_products_list()[0].find_element(*self.product_image).is_displayed()
        else:
            return False
    
    def product_search_finded_title(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        search_bar_btn = super().wait_element(*self.search_bar)
        super().click_button(search_bar_btn)
        super().wait_element(*self.search_bar_input)

        self.get_search_bar_input().click()
        self.get_search_bar_input().send_keys("Banana Juice")
        self.get_search_bar_input().send_keys(Keys.ENTER)
        time.sleep(2)
        if(len(self.get_products_list()) > 0):
            return self.get_products_list()[0].find_element(*self.product_title).is_displayed()
        else:
            return False

    def product_search_finded_review(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        search_bar_btn = super().wait_element(*self.search_bar)
        super().click_button(search_bar_btn)
        super().wait_element(*self.search_bar_input)

        self.get_search_bar_input().click()
        self.get_search_bar_input().send_keys("Banana Juice")
        self.get_search_bar_input().send_keys(Keys.ENTER)
        time.sleep(2)
        if(len(self.get_products_list()) > 0):
             self.get_products_list()[0].find_element(*self.product_title).is_displayed()
             self.get_products_list()[0].find_element(*self.product_title).click()
             super().wait_element(*self.product_expantion_panel)
             time.sleep(1)
             super().click_button(self.get_expantion_panel())
             list = self.driver.find_elements(By.CLASS_NAME,'comment')
             if len(list) >= 1:
                return True
             else:
                return False
    
    def product_search_finded_review_empty(self):
        boton = super().wait_element(*self.popup)
        super().click_button(boton)
        search_bar_btn = super().wait_element(*self.search_bar)
        super().click_button(search_bar_btn)
        super().wait_element(*self.search_bar_input)

        self.get_search_bar_input().click()
        self.get_search_bar_input().send_keys("Banana Juice")
        self.get_search_bar_input().send_keys(Keys.ENTER)
        time.sleep(2)
        if(len(self.get_products_list()) > 0):
             self.get_products_list()[0].find_element(*self.product_title).is_displayed()
             self.get_products_list()[0].find_element(*self.product_title).click()
             super().wait_element(*self.product_expantion_panel)
             time.sleep(1)
             super().click_button(self.get_expantion_panel())
             list = self.driver.find_elements(By.CLASS_NAME,'comment')
             if len(list) <= 0:
                return True
             else:
                return False
        
        