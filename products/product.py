import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class products(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")

    def test_validate_products_image(self):
        dropdowm = self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div")
        dropdowm.click()
        selected = self.driver.find_element(By.XPATH,'//*[@id="mat-option-2"]')
        selected.click()
        products_list = self.driver.find_elements(By.TAG_NAME,'mat-grid-tile')
        count = 0
        for e in products_list:
            if e.find_element(By.CLASS_NAME,"mat-card-image").is_displayed() == True:
                count += 1
        self.assertEqual(count,len(products_list),"All images")
    
    def test_validate_products_title(self):
        dropdowm = self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div")
        dropdowm.click()
        selected = self.driver.find_element(By.XPATH,'//*[@id="mat-option-2"]')
        selected.click()
        products_list = self.driver.find_elements(By.TAG_NAME,'mat-grid-tile')
        count = 0
        for e in products_list:
            if e.find_element(By.CLASS_NAME,"item-name").is_displayed() == True:
                count += 1
        self.assertEqual(count,len(products_list),"All titles")

    def test_validate_products_prices(self):
        dropdowm = self.driver.find_element(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-paginator/div/div/div[1]/mat-form-field/div/div[1]/div")
        dropdowm.click()
        selected = self.driver.find_element(By.XPATH,'//*[@id="mat-option-2"]')
        selected.click()
        products_list = self.driver.find_elements(By.TAG_NAME,'mat-grid-tile')
        count = 0
        for e in products_list:
            if e.find_element(By.CLASS_NAME,"ng-star-inserted").is_displayed() == True:
                count += 1
        self.assertEqual(count,len(products_list),"All prices")

    @classmethod
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()