import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
class SearchProduct(unittest.TestCase): 

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://demo.owasp-juice.shop/")

    # def test_product_search_finded(self):
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
    #     validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
    #     if validatePoppup.is_displayed() == True:
    #         validatePoppup.click()
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')))
    #     self.driver.find_element(By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys("Banana Juice")
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(Keys.ENTER)
    #     value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-card")
    #     self.assertFalse(value,"Validate if product exist")

    # def test_product_search_finded_image(self):
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
    #     validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
    #     if validatePoppup.is_displayed() == True:
    #         validatePoppup.click()
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')))
    #     self.driver.find_element(By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys("Banana Juice")
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(Keys.ENTER)
    #     value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-card")
    #     image = False
    #     if value == False:
    #         time.sleep(1)
    #         self.driver.find_element(By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile/div/mat-card').click()
    #         time.sleep(1)
    #         image = self.driver.find_element(By.CLASS_NAME,'img-thumbnail').is_displayed()
    #     self.assertTrue(image,"Product image")
    
    # def test_product_search_finded_title(self):
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
    #     validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
    #     if validatePoppup.is_displayed() == True:
    #         validatePoppup.click()
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')))
    #     self.driver.find_element(By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]').click()
    #     time.sleep(1)
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys("Banana Juice")
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(Keys.ENTER)
    #     value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-card")
    #     image = False
    #     if value == False:
    #         time.sleep(1)
    #         self.driver.find_element(By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile/div/mat-card').click()
    #         time.sleep(1)
    #         image = self.driver.find_element(By.XPATH,'//*[@id="mat-dialog-1"]/app-product-details/mat-dialog-content/div/div[1]/div[2]/h1').is_displayed()
    #     self.assertTrue(image,"Product title")

    # def test_product_review(self):
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
    #     validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
    #     if validatePoppup.is_displayed() == True:
    #         validatePoppup.click()
    #     WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]')))
    #     self.driver.find_element(By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]').click()
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys("Banana Juice")
    #     self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(Keys.ENTER)
    #     value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-card")
    #     data = False
    #     if value == False:
    #         time.sleep(1)
    #         self.driver.find_element(By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile/div/mat-card').click()
    #         time.sleep(1)
    #         self.driver.find_element(By.TAG_NAME,'mat-expansion-panel-header').click()
    #         time.sleep(1)
    #         list = self.driver.find_elements(By.CLASS_NAME,'comment')
    #         if len(list) >= 1:
    #             data = True
    #         elif len(list) <= 0:
    #             data = False
    #     self.assertTrue(data,0)

    def test_product_review_empty(self):
        WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')))
        validatePoppup = self.driver.find_element(By.XPATH, '//*[@id="mat-dialog-0"]/app-welcome-banner/div/div[2]/button[2]')
        if validatePoppup.is_displayed() == True:
            validatePoppup.click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="searchQuery"]/span/mat-icon[2]').click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys("Fruit Press")
        self.driver.find_element(By.XPATH, '//*[@id="mat-input-0"]').send_keys(Keys.ENTER)
        time.sleep(2)
        value = self.validate_is_exist(By.XPATH,"/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/mat-card")
        list = 0
        emptyElement = False
        btn = False
        if value == False:
            self.driver.find_element(By.XPATH,'/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-search-result/div/div/div[2]/mat-grid-list/div/mat-grid-tile/div/mat-card').click()
            self.driver.find_element(By.TAG_NAME,'mat-expansion-panel-header').click()
            time.sleep(40)
            list = self.driver.find_elements(By.CLASS_NAME,'comment')
            if len(list) <= 0:
                time.sleep(1)
                text = self.driver.find_element(By.CLASS_NAME,'noResultText').text
                btn = self.driver.find_element(By.CLASS_NAME, 'close-dialog').is_displayed()
                if text == "There is no review for this product yet." and btn == True:
                    emptyElement = True
        self.assertTrue(emptyElement,0)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def validate_is_exist(self, how, what):
        try: displayed = self.driver.find_element(by=how, value=what).is_displayed()
        except NoSuchElementException: return False
        return displayed

if __name__ == '__main__':
    unittest.main()