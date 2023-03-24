"""Test de la pantalla de inicio(tabla de productos)

Aquí verificaremos que los productos que se encuentren 
en el login tengan todos imagen, precio y título.
"""

import sys
sys.path.append("src/pages/home")
sys.path.append("src/BaseElements")
from table_products import TableProducts
from globalMethods import GlobalMethods

screen_module = 'home'


class TestTableProduct():


        def test_all_images(self, load_driver):
                products = TableProducts(load_driver)
                products.click_pagination()
                products.pagination_last_option()
                assert products.validate_products_image(products.get_products()) == True,"No todos los productos del home tienen imagen"
                self.take_screen(load_driver,'test_all_images')

        def test_all_titles(self, load_driver):
                products = TableProducts(load_driver)
                products.click_pagination()
                products.pagination_last_option()
                assert products.validate_products_title(products.get_products()) == True,"No todos los productos del home tienen titulo"
                self.take_screen(load_driver,'test_all_titles')

        def test_all_prices(self, load_driver):
                products = TableProducts(load_driver)
                products.click_pagination()
                products.pagination_last_option()
                assert products.validate_products_prices(products.get_products()) == True,"No todos los productos del home tienen precio"
                self.take_screen(load_driver,'test_all_prices')
        
        def take_screen(self,load_driver, method):
                GlobalMethods.take_screenshot(load_driver, screen_module,f"{__name__}-{method}")