import pytest
from selenium import webdriver
from Config.config import TestData


@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    driver = webdriver.Chrome()
    request.driver = driver
    yield
    driver.close()