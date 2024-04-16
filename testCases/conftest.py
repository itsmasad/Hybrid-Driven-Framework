import pytest
from selenium import webdriver

@pytest.fixture()
def setUp(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser.......")
        # pytest -v -s *filename* --browser chrome
    elif browser =='firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser.......")
        # pytest -v -s *filename* --browser firefox

    return driver

def pytest_addoption(parser): #This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): # This will return the browser value to the setup method
    return request.config.getoption("--browser")

## Pytest HTML Report #########

# def pytest_html_configure_metadata(config, metadata):
#     metadata['Project Name'] = 'nop Commerce'
#     metadata['Module Name'] = 'nop Commerce'
#     metadata['Tester'] = 'Muhammad Asad'


## It is hook for delete/modify environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
