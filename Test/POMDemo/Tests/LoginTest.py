from selenium import webdriver
import time
import unittest
# To run the POM in command
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
#.........

from Test.POMDemo.Pages.LoginPage import LoginPage
from Test.POMDemo.Pages.HomePage import HomePage
import HTMLTestRunner

class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path="C:\\Users\\ealaayy\\PycharmProjects\\Selenium\\drivers\\geckodriver.exe")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")


        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()


        #self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        #self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        #self.driver.find_element_by_id("btnLogin").click()
        #self.driver.find_element_by_id("welcome").click()
        #self.driver.find_element_by_link_text("Logout").click()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")




if __name__ == '__main__':
 unittest.main(testRunner=HTMLTestRunner.HTMLTestRunner(output="C:\\Users\\ealaayy\\PycharmProjects\\Selenium\\reports"))



