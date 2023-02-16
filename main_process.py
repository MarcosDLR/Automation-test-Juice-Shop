import unittest
import HtmlTestRunner
from HomePage.HomeNavbar import HomeNavbar
from products.product import products
from FindProduct.find_product import SearchProduct
from drawerMenu.drawerMenu import DrawerMenu
from lenguage.lenguage import lenguage_test
from register.register import register_user
from login.login_incorrect import login_incorrect

suite_1 = unittest.TestLoader().loadTestsFromTestCase(HomeNavbar)

suite_2 = unittest.TestLoader().loadTestsFromTestCase(products)

suite_3 = unittest.TestLoader().loadTestsFromTestCase(SearchProduct)

suite_4 = unittest.TestLoader().loadTestsFromTestCase(DrawerMenu)

suite_5 = unittest.TestLoader().loadTestsFromTestCase(lenguage_test)

suite_6 = unittest.TestLoader().loadTestsFromTestCase(register_user)

suite_7 = unittest.TestLoader().loadTestsFromTestCase(login_incorrect)

runner_1 = HtmlTestRunner.HTMLTestRunner(output='reports/HomeNavbar',report_name='Home NavBar', report_title="Home NavBar")
runner_1.run(suite_1)
runner_2 = HtmlTestRunner.HTMLTestRunner(output='reports/Products',report_name='Products', report_title="Products")
runner_2.run(suite_2)
runner_3 = HtmlTestRunner.HTMLTestRunner(output='reports/SearchProduct',report_name='Search Product', report_title="Search Product")
runner_3.run(suite_3)
runner_4 = HtmlTestRunner.HTMLTestRunner(output='reports/DrawerMenu',report_name='Drawer Menu', report_title="Drawer Menu")
runner_4.run(suite_4)
runner_5 = HtmlTestRunner.HTMLTestRunner(output='reports/lenguage',report_name='Lenguage', report_title="Lenguage")
runner_5.run(suite_5)
runner_6 = HtmlTestRunner.HTMLTestRunner(output='reports/register',report_name='Register', report_title="Register")
runner_6.run(suite_6)
runner_7 = HtmlTestRunner.HTMLTestRunner(output='reports/login',report_name='Incorrect Login', report_title="Incorrect Login")
runner_7.run(suite_7)
