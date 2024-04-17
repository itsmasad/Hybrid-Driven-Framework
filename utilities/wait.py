from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class reusableFunction:

    def __init__(self,driver):
        self.driver = driver

    def wait(self, by, locator): 
        return WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((by, locator))
        )