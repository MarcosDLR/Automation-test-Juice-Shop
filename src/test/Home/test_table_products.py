import sys
sys.path.append("src/pages/home")

from table_products import Table_products

def test_all_images(load_driver):
        driver = load_driver
        drawerPage = Table_products(driver)
        assert drawerPage.validate_products_image() == True, "No todos los productos del home tienen imagen"

def test_all_titles(load_driver):
        driver = load_driver
        drawerPage = Table_products(driver)
        assert drawerPage.validate_products_title() == True, "No todos los productos del home tienen titulo"

def test_all_prices(load_driver):
        driver = load_driver
        drawerPage = Table_products(driver)
        assert drawerPage.validate_products_prices() == True, "No todos los productos del home tienen precio"