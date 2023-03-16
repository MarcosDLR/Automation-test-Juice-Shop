import sys
sys.path.append("src/pages/sing_up")
sys.path.append("src/test/BaseElements")

from register import Register
from screen_shot import Screen_shot

screen_module = 'sing_up'

def test_register(load_driver):
        driver = load_driver
        drawerPage = Register(driver)
        assert drawerPage.test_register() == True, "El usuario creado no es valido"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_register")
