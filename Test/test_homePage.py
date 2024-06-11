import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

from Pages import pages
import pytest_html

driver = webdriver.Chrome()
def setup_module():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(pages.homePage_Url)


def teardown_module():
    time.sleep(5)
    driver.quit()

def test_oup_title():
    assert driver.title == "English Language Teaching Home Page | Oxford University Press"

def test_oup_url():
    assert driver.current_url == "https://elt.oup.com/?cc=ch&selLanguage=en"

def test_click_on_logo():
    driver.find_element(By.CLASS_NAME, "siteTitle_logoImg").click()
    assert driver.current_url == "https://elt.oup.com/?cc=ch&selLanguage=en"

