"""Test de la pantalla login

Iniciamos sesión con un usuario y contraseña
 y verificamos si este es válido.
"""

import sys
sys.path.append("src/pages/login")
sys.path.append("src/BaseElements")
from login import Login
from globalMethos import GlobalMethos

screen_module = 'login'


class TestLogin():


        def test_login_is_incorrect(self, load_driver):
                login_page = Login(load_driver)
                login_page.remove_init_popup()
                login_page.click_account_btn()
                login_page.click_login_btn()
                login_page.wait_login_card()
                login_page.set_user_in_input()
                login_page.set_password_in_input("Just a test")
                login_page.click_login_summit()
                login_page.wait_login_error()

                assert login_page.validate_error_login() == True, "El login es correcto"
                GlobalMethos.take_screenshot(load_driver, screen_module,
                                              f"{__name__}-test_login_is_incorrect")
