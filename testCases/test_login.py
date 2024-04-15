import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
        else:
            assert False
    
    def test_login(self,setUp):
            self.driver = setUp
            self.driver.get(self.baseURL)
            # Creating an object of loginpage to access class method
            # When this class will be created or called the constructor (__init__) which have the driver will automatically invoke in the pagelogin class
            self.lp = LoginPage(self.driver)
            # Calling Loginpage objects using self.lp
            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            act_title = self.driver.title
            self.driver.close()
            if act_title == "Dashboard / nopCommerce administration":
                 assert True
            else:
                 assert False