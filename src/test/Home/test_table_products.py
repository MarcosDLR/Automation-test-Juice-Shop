import sys
sys.path.append("src/pages/home")
sys.path.append("src")

from table_products import Table_products
from globalMethos import globalMethos

screen_module = 'home'

class TestTableProduct():

        def test_all_images(self,load_driver):
                products = Table_products(load_driver)
                products.click_pagination()
                products.pagination_last_option()
                assert products.validate_products_image(products.get_products()) == True, "No todos los productos del home tienen imagen"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_all_images")

        def test_all_titles(self,load_driver):
                products = Table_products(load_driver)
                products.click_pagination()
                products.pagination_last_option()
                assert products.validate_products_title(products.get_products()) == True, "No todos los productos del home tienen titulo"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_all_titles")

        def test_all_prices(self,load_driver):
                products = Table_products(load_driver)
                products.click_pagination()
                products.pagination_last_option()
                assert products.validate_products_prices(products.get_products()) == True, "No todos los productos del home tienen precio"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_all_prices")