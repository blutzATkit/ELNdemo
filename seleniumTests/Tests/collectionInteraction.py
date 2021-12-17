from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import unittest
import time
import os
import sys
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../..'))
sys.path.append(file_path)

from seleniumTests.POM.homePage import HomePage
from seleniumTests.POM.topFrame import TopFrame

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("http://localhost:4000/home")
        cls.driver.implicitly_wait(10)
        home_page = HomePage(cls.driver)
        home_page.enter_username("test.user@provider.edu")
        home_page.enter_password("asdasdasd")
        home_page = HomePage(cls.driver)
        home_page.click_login()

    def test_00_import_click(self):
        home_page = HomePage(self.driver)
        home_page.click_import()
        home_page.click_import_close()

    def test_00_import_file_select_click(self):
        home_page = HomePage(self.driver)
        home_page.click_import()
        home_page.enter_path_import_file_select("/home/benjamin/Downloads/demo.zip")
        home_page.click_import_import()
        time.sleep(15)

    def test_export_click(self):
        home_page = HomePage(self.driver)
        home_page.click_export()
        home_page.click_export_close()       

    def test_export_collection_select_click(self):
        home_page = HomePage(self.driver)
        home_page.click_export()
        try:
            home_page.click_export_checkbox()
        except NoSuchElementException:
            home_page.click_export_close()
            time.sleep(20)
            self.driver.refresh()
            home_page.click_export()
            home_page.click_export_checkbox()
        home_page.click_export_export()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(15)
        top_frame = TopFrame(cls.driver)
        top_frame.click_logout()
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()