import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from Pages import pages

@pytest.fixture(scope='module')

def Home_Page():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(pages.homePage_Url)

    yield
    time.sleep(5)
    driver.quit()

def test_oup_title(Home_Page):
    assert driver.title == "English Language Teaching Home Page | Oxford University Press"

def test_oup_url(Home_Page):
    assert driver.current_url == "https://elt.oup.com/?cc=ch&selLanguage=en"

def test_click_on_logo(Home_Page):
    driver.find_element(By.CLASS_NAME, "siteTitle_logoImg").click()
    assert driver.current_url == "https://elt.oup.com/?cc=ch&selLanguage=en"

