import sys
sys.path.append("src/pages/home")
sys.path.append("src")

from drawerMenu import DrawerMenu
from globalMethos import globalMethos

screen_module = 'home'

class TestDrawerMenu():

        def test_validate_btn_exist(self,load_driver):
                drawerPage = DrawerMenu(load_driver)
                drawerPage.close_popup_init()
                assert drawerPage.validate_btn_drawer_exist() == True, "El boton del drawer no existe en la barra"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_validate_btn_exist")

        def test_validate_drawer_content(self,load_driver):
                drawerPage = DrawerMenu(load_driver)
                drawerPage.close_popup_init()
                if drawerPage.validate_drawer_displed():
                        drawerPage.click_drawer()
                        drawerPage.wait_header()
                        assert drawerPage.validate_btn_drawer_exist() == True, "El drawer no tiene contenido"
                else:
                        assert False, "El drawer no esta desplegado"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_validate_drawer_content")