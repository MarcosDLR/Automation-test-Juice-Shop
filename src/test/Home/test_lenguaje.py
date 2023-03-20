import sys
sys.path.append("src/pages/home")
sys.path.append("src/test/BaseElements")

from lenguaje import Lenguaje
from globalMethos import globalMethos

screen_module = 'home'

class TestLenguaje():

        def test_validate_changed_lenguaje(self,load_driver):
                lenguaje = Lenguaje(load_driver)
                lenguaje.close_popup_init()
                if lenguaje.sidenav_visible():
                        before = lenguaje.get_actual_lenguaje_in_page()
                        lenguaje.click_sidenav()
                        lenguaje.change_lenguaje()
                        after = lenguaje.get_actual_lenguaje_in_page()
                        assert before != after, "El lenguaje de la pagina sigue siendo el mismo"
                else:
                     assert False, "No existe el sidenav"   
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_validate_changed_lenguaje")
