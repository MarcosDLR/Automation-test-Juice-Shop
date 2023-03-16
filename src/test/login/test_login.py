import sys
sys.path.append("src/pages/login")
sys.path.append("src/test/BaseElements")

from login import Login
from screen_shot import Screen_shot

screen_module = 'login'

def test_login_is_incorrect(load_driver):
        drawerPage = Login(load_driver)
        assert drawerPage.test_login_incorrect() == True, "El login es correcto"
        Screen_shot.take_screenshot(load_driver,screen_module, f"{__name__}-test_login_is_incorrect")
