import unittest
import HtmlTestRunner
from HomePage.HomeNavbar import HomeNavbar
from products.product import products
from FindProduct.find_product import SearchProduct
from drawerMenu.drawerMenu import DrawerMenu
from lenguage.lenguage import lenguage_test
from register.register import register_user
from login.login_incorrect import login_incorrect

home_navbar = unittest.TestLoader().loadTestsFromTestCase(HomeNavbar)
products_test = unittest.TestLoader().loadTestsFromTestCase(products)
search_product = unittest.TestLoader().loadTestsFromTestCase(SearchProduct)
drawer_menu = unittest.TestLoader().loadTestsFromTestCase(DrawerMenu)
lenguage_check = unittest.TestLoader().loadTestsFromTestCase(lenguage_test)
register_validation = unittest.TestLoader().loadTestsFromTestCase(register_user)
login_test = unittest.TestLoader().loadTestsFromTestCase(login_incorrect)
test_suite = unittest.TestSuite([home_navbar,products_test,search_product,drawer_menu,lenguage_check,register_validation,login_test])

runner = HtmlTestRunner.HTMLTestRunner(report_title='Home Page', report_name="Test Report", descriptions='Acceptance Tests')
unittest.TextTestRunner()
runner.run(test_suite)
# unittest.TextTestRunner(verbosity=2).run(test_suite)