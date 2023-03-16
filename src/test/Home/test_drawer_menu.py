import sys
sys.path.append("src/pages/home")
sys.path.append("src/test/BaseElements")

from drawerMenu import DrawerMenu
from screen_shot import Screen_shot

screen_module = 'home'

def test_validate_btn_exist(load_driver):
        drawerPage = DrawerMenu(load_driver)
        assert drawerPage.validate_btn_drawer_exist() == True, "El boton del drawer no existe en la barra"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_validate_btn_exist")

def test_validate_drawer_content(load_driver):
        drawerPage = DrawerMenu(load_driver)
        assert drawerPage.test_btn_drawer_exist_content() == True, "El drawer no tiene contenido"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_validate_drawer_content")