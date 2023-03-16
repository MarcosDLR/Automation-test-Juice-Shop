import sys
sys.path.append("src/pages/home")

from drawerMenu import DrawerMenu

def test_validate_btn_exist(load_driver):
        driver = load_driver
        drawerPage = DrawerMenu(driver)
        assert drawerPage.validate_btn_drawer_exist() == True, "El boton del drawer no existe en la barra"

def test_validate_drawer_content(load_driver):
        driver = load_driver
        drawerPage = DrawerMenu(driver)
        assert drawerPage.test_btn_drawer_exist_content() == True, "El drawer no tiene contenido"