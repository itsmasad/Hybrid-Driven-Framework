import pytest
from selenium import webdriver

@pytest.fixture()
def setUp(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
    elif browser =='firefox':
        driver = webdriver.Firefox()
        
    return driver

def pytest_addoption(parser): #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to the setup method
    return request.config.getoption("--browser")