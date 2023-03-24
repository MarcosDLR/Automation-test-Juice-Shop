"""Test de la pantalla sing_up

Aquí esta localizado el test de crear una cuenta e iniciar sesión con la misma. 
"""

import sys
sys.path.append("src/pages/sing_up")
sys.path.append("src/BaseElements")
import random
from register import Register
from globalMethods import GlobalMethods

screen_module = 'sing_up'


class TestSingUp():


        def test_register(self, load_driver):
                sing_up_page = Register(load_driver)
                user = ("test"+ str(random.random()) +"@gmail.com")
                password = "Just a test"
                sing_up_page.remove_popup_init()
                sing_up_page.click_account_btn()
                sing_up_page.click_login_btn()
                sing_up_page.btn_customer()
                sing_up_page.set_user(user)
                sing_up_page.set_password_and_repeat(password)
                sing_up_page.click_register_form()
                sing_up_page.click_register_options()
                sing_up_page.set_security_answer(password)
                sing_up_page.wait_login_card()
                sing_up_page.set_email_input(user)
                sing_up_page.set_password_input(password)
                sing_up_page.click_login_btn_form()

                assert sing_up_page.test_register() == True, "El usuario creado no es valido"
                GlobalMethods.take_screenshot(load_driver, screen_module,
                                              f"{__name__}-test_register")
