import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Manu import Manu
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig


class TestCase_002_Products:
    baseURL = ReadConfig.getApplicationURL()
    productName = ReadConfig.getProductFilterData()
    userName = ReadConfig.getUseremail()
    password = ReadConfig.getUserpassword()

    def test_Product_filter(self,setUp):

        self.driver = setUp
        self.driver.get(self.baseURL)
        self.Manu = Manu(self.driver)
        self.lp = LoginPage(self.driver)

        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()

        self.Manu.Click_manue_catalog()
        self.Manu.Click_manue_products()
        self.Manu.setProductName(self.productName)
        self.Manu.Click_searchButton()
        self.driver.close()
    
    def addNewProduct(self,setUp):
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.userName)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin

        self.Manu = Manu(self.driver)
        self.Manu.Click_addNewProduct()
        self.Manu.set_newProductName()
        self.Manu.set_shortDescription()
        self.Manu.Click_Save_Button()


