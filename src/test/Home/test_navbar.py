import sys
sys.path.append("src/pages/home")
sys.path.append("src/test/BaseElements")

from navbar import Navbar
from screen_shot import Screen_shot

screen_module = 'home'

def test_logo(load_driver):
        drawerPage = Navbar(load_driver)
        assert drawerPage.validate_logo() == True, "El logo no existe"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_logo")

def test_name(load_driver):
        drawerPage = Navbar(load_driver)
        assert drawerPage.validate_name() == True, "El nombre no existe"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_name")

def test_btn_search(load_driver):
        drawerPage = Navbar(load_driver)
        assert drawerPage.validate_name() == True, "El boton de busqueda no existe"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_btn_search")

def test_btn_lenguaje(load_driver):
        drawerPage = Navbar(load_driver)
        assert drawerPage.validate_name() == True, "El boton de lenguaje no existe"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_btn_lenguaje")

def test_btn_change_account(load_driver):
        drawerPage = Navbar(load_driver)
        assert drawerPage.validate_name() == True, "El boton de cambiar cuenta no existe"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_btn_change_account")
