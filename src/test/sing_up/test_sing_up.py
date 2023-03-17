import sys
sys.path.append("src/pages/sing_up")
sys.path.append("src")

from register import Register
from globalMethos import globalMethos

screen_module = 'sing_up'

class TestSingUp():

        def test_register(self,load_driver):
                driver = load_driver
                drawerPage = Register(driver)
                assert drawerPage.test_register() == True, "El usuario creado no es valido"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_register")
