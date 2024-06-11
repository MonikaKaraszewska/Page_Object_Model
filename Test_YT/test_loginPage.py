import pytest
from selenium import webdriver
from Test_YT.test_base import BaseTest
from Pages.loginPage import LoginPage
from Config.config import TestData

class Test_login("init_driver"):
    driver = webdriver.Chrome
    def test_singup_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        flag = self.loginPage.is_signup_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.LOGIN_Page_Title)
        assert title == TestData.LOGIN_Page_Title



