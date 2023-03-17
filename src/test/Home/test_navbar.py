import sys
sys.path.append("src/pages/home")
sys.path.append("src")

from navbar import Navbar
from globalMethos import globalMethos

screen_module = 'home'

class TestNavBar():

        def test_logo(self,load_driver):
                drawerPage = Navbar(load_driver)
                assert drawerPage.validate_logo() == True, "El logo no existe"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_logo")

        def test_name(self,load_driver):
                drawerPage = Navbar(load_driver)
                assert drawerPage.validate_name() == True, "El nombre no existe"
                Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_name")

        def test_btn_search(self,load_driver):
                drawerPage = Navbar(load_driver)
                assert drawerPage.validate_name() == True, "El boton de busqueda no existe"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_btn_search")

        def test_btn_lenguaje(self,load_driver):
                drawerPage = Navbar(load_driver)
                assert drawerPage.validate_name() == True, "El boton de lenguaje no existe"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_btn_lenguaje")

        def test_btn_change_account(self,load_driver):
                drawerPage = Navbar(load_driver)
                assert drawerPage.validate_name() == True, "El boton de cambiar cuenta no existe"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_btn_change_account")
