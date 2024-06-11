import time
from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from Pages import pages, text, elements

@pytest.fixture()
def home_Page():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(pages.homePage_Url)

@pytest.fixture()
def login_page(home_Page):
    driver.find_element(By.LINK_TEXT, elements.logIn_button).click()
    driver.find_element(By.TAG_NAME, 'h1').click()

def test_page(home_Page):
    assert driver.title == text.home_page_title

def test_logIn_button(home_Page,login_page):
    assert driver.title == 'Log in'

def test_logIn_input(home_Page,login_page):
    assert driver.title == 'Log in'
    username = driver.find_element(By.ID, "username")
    username.send_keys("monikakaraszewska@gmail.com", Keys.TAB)
    paswrd = driver.find_element(By.ID, "password")
    paswrd.send_keys("Oxford58", Keys.TAB)
    # driver.find_element(By.XPATH, "//button[@type='submit']").submit()
    time.sleep(10)

@pytest.mark.usefixtures(home_Page,login_page)
def test_logIn_button2():
    assert driver.title == 'Log in'