import sys
sys.path.append("src/pages/home")
sys.path.append("src/test/BaseElements")

from table_products import Table_products
from screen_shot import Screen_shot

screen_module = 'home'

def test_all_images(load_driver):
        drawerPage = Table_products(load_driver)
        assert drawerPage.validate_products_image() == True, "No todos los productos del home tienen imagen"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_all_images")

def test_all_titles(load_driver):
        drawerPage = Table_products(load_driver)
        assert drawerPage.validate_products_title() == True, "No todos los productos del home tienen titulo"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_all_titles")

def test_all_prices(load_driver):
        drawerPage = Table_products(load_driver)
        assert drawerPage.validate_products_prices() == True, "No todos los productos del home tienen precio"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_all_prices")