import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()

    def test_homePageTitle(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # Assertion for the Title
        if act_title == "Your store. Login":
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
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
            # Assertion for the Title
            if act_title == "Dashboard / nopCommerce administration":
                 self.driver.close()
                 assert True
            else:
                 self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
                 self.driver.close()
                 assert False