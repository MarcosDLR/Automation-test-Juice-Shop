import sys
from selenium.webdriver.common.by import By

sys.path.append("src/BaseElements")

class TableProducts():
 

    def __init__(self, driver):
        self.driver = driver
    
    def get_btn_pagination(self):
        return self.driver.find_element(By.XPATH, "/html/body/app-root/div/ \
                                        mat-sidenav-container/mat-sidenav-content/app-search-result/ \
                                        div/div/mat-paginator/div/div/div[1]/mat-form-field/div/ \
                                        div[1]/div")
    
    def get_pagination_last_option(self):
        return self.driver.find_element(By.XPATH, '//*[@id="mat-option-2"]')
    
    def get_products_list(self):
        return self.driver.find_elements(By.TAG_NAME, 'mat-grid-tile')
    
    def get_card_image(self,element):
        return element.find_element(By.CLASS_NAME, "mat-card-image")
    
    def get_card_title(self,element):
        return element.find_element(By.CLASS_NAME, "item-name")
    
    def get_card_price(self,element):
        return element.find_element(By.CLASS_NAME, "ng-star-inserted")
    
    def click_pagination(self):
        self.get_btn_pagination().click()
    
    def pagination_last_option(self):
        self.get_pagination_last_option().click()
    
    def get_products(self):
        return self.get_products_list()


    def validate_products_image(self,products_list):
        """Validar que todos los productos que estan en el home tengan imagenes"""
        count = 0
        for e in products_list:
            if self.get_card_image(e).is_displayed() == True:
                count += 1
        if count == len(products_list):
            return True
        else:
            return False
    
    def validate_products_title(self,products_list):
        """Validar que todos los productos que estan en el home tengan título"""
        count = 0
        for e in products_list:
            if self.get_card_image(e).is_displayed() == True:
                count += 1
        if count == len(products_list):
            return True
        else:
            return False

    def validate_products_prices(self,products_list):
        """Validar que todos los productos que estan en el home tengan precio"""
        count = 0
        for e in products_list:
            if self.get_card_image(e).is_displayed() == True:
                count += 1
        if count == len(products_list):
            return True
        else:
            return False