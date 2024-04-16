import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.Manu import Manu
from utilities.readProperties import ReadConfig


class TestCase_002_Products:
    baseURL = ReadConfig.getApplicationURL
    productName = ReadConfig.getProductFilterData

    def test_Product_filter(self,setUp):

        self.driver = setUp
        self.driver.get(self.baseURL)
        self.Manu = Manu(self.driver)
        self.Manu.Click_manue_catalog()
        self.Manu.Click_manue_products()
        self.Manu.setProductName(self.productName)
        self.Manu.Click_searchButton()
