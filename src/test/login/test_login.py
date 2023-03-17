import sys
sys.path.append("src/pages/login")
sys.path.append("src")

from login import Login
from globalMethos import globalMethos

screen_module = 'login'

class TestLogin():

        def test_login_is_incorrect(self,load_driver):
                drawerPage = Login(load_driver)
                assert drawerPage.test_login_incorrect() == True, "El login es correcto"
                globalMethos.take_screenshot(load_driver,screen_module, f"{__name__}-test_login_is_incorrect")
