import sys
sys.path.append("src/pages/product")
sys.path.append("src")

from product import Product
from globalMethos import globalMethos

screen_module = 'product'

class TestProduct():

        def repetitive_steps(self,product_page,product_name):
                product_page.remove_popup_init()
                product_page.click_search_bar()
                product_page.wait_search_bar()
                product_page.click_search_bar_input()
                product_page.set_text_in_search_bar(product_name)
                product_page.press_enter_in_serach_bar()
        
        def repetitive_steps_with_reviews(self,product_page):
                product_page.click_product_title()
                product_page.wait_expanded_products()
                product_page.click_btn_expanded()

        def test_product_search_finded(self,load_driver):
                product_page = Product(load_driver)
                self.repetitive_steps(product_page,"Banana Juice")
                assert product_page.validate_products() == True, "No se encontro el producto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded")

        def test_product_search_image(self,load_driver):
                product_page = Product(load_driver)
                self.repetitive_steps(product_page,"Banana Juice")
                assert product_page.validate_products_image() == True, "No se encontro la imagen del producto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_image")

        def test_product_search_title(self,load_driver):
                product_page = Product(load_driver)
                self.repetitive_steps(product_page,"Banana Juice")
                assert product_page.validate_products_title() == True, "No se encontro la titulo del producto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_title")

        def test_product_search_finded_review(self,load_driver):
                product_page = Product(load_driver)
                self.repetitive_steps(product_page,"Banana Juice")
                self.repetitive_steps_with_reviews(product_page)
                assert product_page.find_reviews() == True, "No se encontraron reviews"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded_review")

        def test_product_search_finded_review_empty(self,load_driver):
                product_page = Product(load_driver)
                self.repetitive_steps(product_page,"Banana Juice")
                self.repetitive_steps_with_reviews(product_page)
                assert product_page.find_empty_reviews() == True, "Se encontraron reviews"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded_review_empty")
        
