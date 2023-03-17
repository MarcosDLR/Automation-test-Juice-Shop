import sys
sys.path.append("src/pages/product")
sys.path.append("src")

from product import Product
from globalMethos import globalMethos

screen_module = 'product'

class TestProduct():

        def test_product_search_finded(self,load_driver):
                drawerPage = Product(load_driver)
                assert drawerPage.product_search_finded() == True, "No se encontro el producto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded")

        def test_product_search_image(self,load_driver):
                drawerPage = Product(load_driver)
                assert drawerPage.product_search_finded_image() == True, "No se encontro la imagen del producto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_image")

        def test_product_search_title(self,load_driver):
                drawerPage = Product(load_driver)
                assert drawerPage.product_search_finded_title() == True, "No se encontro la titulo del producto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_title")

        def test_product_search_finded_review(self,load_driver):
                drawerPage = Product(load_driver)
                assert drawerPage.product_search_finded_review() == True, "No se encontraron reviews"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded_review")

        def test_product_search_finded_review_empty(self,load_driver):
                drawerPage = Product(load_driver)
                assert drawerPage.product_search_finded_review_empty() == True, "Se encontraron reviews"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded_review_empty")
        
