import sys
sys.path.append("src/pages/product")
sys.path.append("src/test/BaseElements")

from product import Product
from screen_shot import Screen_shot

screen_module = 'product'

def test_product_search_finded(load_driver):
        drawerPage = Product(load_driver)
        assert drawerPage.product_search_finded() == True, "No se encontro el producto"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded")

def test_product_search_image(load_driver):
        drawerPage = Product(load_driver)
        assert drawerPage.product_search_finded_image() == True, "No se encontro la imagen del producto"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_image")

def test_product_search_title(load_driver):
        drawerPage = Product(load_driver)
        assert drawerPage.product_search_finded_title() == True, "No se encontro la titulo del producto"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_title")

def test_product_search_finded_review(load_driver):
        drawerPage = Product(load_driver)
        assert drawerPage.product_search_finded_review() == True, "No se encontraron reviews"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded_review")

def test_product_search_finded_review_empty(load_driver):
        drawerPage = Product(load_driver)
        assert drawerPage.product_search_finded_review_empty() == True, "Se encontraron reviews"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_product_search_finded_review_empty")
        
