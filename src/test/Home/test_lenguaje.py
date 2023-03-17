import sys
sys.path.append("src/pages/home")
sys.path.append("src/test/BaseElements")

from lenguaje import Lenguaje
from globalMethos import globalMethos

screen_module = 'home'

class TestLenguaje():

        def test_validate_changed_lenguaje(self,load_driver):
                drawerPage = Lenguaje(load_driver)
                assert drawerPage.test_lenguage_change() == True, "El lenguaje de la pagina sigue siendo el mismo"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_validate_changed_lenguaje")
