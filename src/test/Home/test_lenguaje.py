import sys
sys.path.append("src/pages/home")

from lenguaje import Lenguaje

def test_validate_changed_lenguaje(load_driver):
        driver = load_driver
        drawerPage = Lenguaje(driver)
        assert drawerPage.test_lenguage_change() == True, "El lenguaje de la pagina sigue siendo el mismo"
