"""Test de la pantalla de inicio(Nav Bar)

Verificaremos si el navegador contiene el logo y 
el nombre de la organización,
tambien verificaremos si contiene la barra de búsqueda,
lenguaje y el botón para registrarse.
"""

import sys
sys.path.append("src/pages/home")
sys.path.append("src/BaseElements")
from navbar import Navbar
from globalMethods import GlobalMethods


screen_module = 'home'


class TestNavBar():


        def test_logo(self, load_driver):
                nav_bar = Navbar(load_driver)
                assert nav_bar.validate_logo() == True, "El logo no existe"
                self.take_screen(load_driver,'test_logo')

        def test_name(self, load_driver):
                nav_bar = Navbar(load_driver)
                assert nav_bar.validate_name() == True, "El nombre no existe"
                self.take_screen(load_driver,'test_name')

        def test_btn_search(self, load_driver):
                nav_bar = Navbar(load_driver)
                assert nav_bar.validate_name() == True, "El boton de busqueda no existe"
                self.take_screen(load_driver,'test_btn_search')

        def test_btn_language(self, load_driver):
                nav_bar = Navbar(load_driver)
                assert nav_bar.validate_name() == True, "El boton de lenguaje no existe"
                self.take_screen(load_driver,'test_btn_language')

        def test_btn_change_account(self, load_driver):
                nav_bar = Navbar(load_driver)
                assert nav_bar.validate_name() == True, "El boton de cambiar cuenta no existe"
                self.take_screen(load_driver,'test_btn_change_account')

        def take_screen(self,load_driver, method):
                GlobalMethods.take_screenshot(load_driver, screen_module,f"{__name__}-{method}")