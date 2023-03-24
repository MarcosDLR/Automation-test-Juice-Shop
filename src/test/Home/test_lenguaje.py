"""Test de la pantalla de inicio(lenguaje)

Cambiaremos el lenguaje de la página y 
verificaremos si este se cambió correctamente
"""

import sys
sys.path.append("src/pages/home")
sys.path.append("src/test/BaseElements")
from language import Language
from globalMethods import GlobalMethods


screen_module = 'home'


class TestLanguage():


        def test_validate_changed_language(self, load_driver):
                language = Language(load_driver)
                language.close_popup_init()
                if language.sidenav_visible():
                        before = language.get_actual_language_in_page()
                        language.click_sideNav()
                        language.change_language()
                        after = language.get_actual_language_in_page()
                        assert before != after, "El lenguaje de la pagina sigue siendo el mismo"
                else:
                     assert False, "No existe el sidenav"
                     
                GlobalMethods.take_screenshot(load_driver,screen_module, 
                                             f"{__name__}-test_validate_changed_language")
