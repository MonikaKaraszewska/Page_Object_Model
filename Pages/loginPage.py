from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.base_pages import BasePage

class LoginPage(BasePage):
    '''By locators'''
    EMAIL = (By.ID,"username" )
    PASSWORD = (By.ID, "password")
    LOG_IN_BUTTON = (By.ID,"loginBtn")
    SIGNUP_LINK = (By.LINK_TEXT, "Sign up")

    '''constructor of the page class'''

    def __init__(self, driver):
        super().__init__(driver)

    '''page actions'''

    def get_login_page_title(self, title):
        return self.get_title(title)


    def is_signup_link_exist(self):
        return self.is_visible(self.SIGNUP_LINK)

    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOG_IN_BUTTON)