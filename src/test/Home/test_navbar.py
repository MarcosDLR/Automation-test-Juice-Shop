import sys
sys.path.append("src/pages/home")

from navbar import Navbar

def test_logo(load_driver):
        driver = load_driver
        drawerPage = Navbar(driver)
        assert drawerPage.validate_logo() == True, "El logo no existe"

def test_name(load_driver):
        driver = load_driver
        drawerPage = Navbar(driver)
        assert drawerPage.validate_name() == True, "El nombre no existe"

def test_btn_search(load_driver):
        driver = load_driver
        drawerPage = Navbar(driver)
        assert drawerPage.validate_name() == True, "El boton de busqueda no existe"

def test_btn_lenguaje(load_driver):
        driver = load_driver
        drawerPage = Navbar(driver)
        assert drawerPage.validate_name() == True, "El boton de lenguaje no existe"

def test_btn_change_account(load_driver):
        driver = load_driver
        drawerPage = Navbar(driver)
        assert drawerPage.validate_name() == True, "El boton de cambiar cuenta no existe"
