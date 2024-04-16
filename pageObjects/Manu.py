from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.wait import reusableFunction


class Manu:
    tab_Catalog_xpath = "//p[normalize-space()='Catalog']"
    tab_products_xpath = "/html[1]/body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]/p[1]"
    textbox_productName_id = "SearchProductName"
    button_search_id = "search-products"

    def __init__(self, driver):
        self.driver = driver

    def Click_manue_catalog(self):
        self.uti = reusableFunction(self.driver)
        self.uti.wait(self.driver,By.XPATH,self.tab_Catalog_xpath)
        self.driver.find_element(By.XPATH,self.tab_Catalog_xpath).click()
    
    def Click_manue_products(self):
        self.uti = reusableFunction(self.driver)
        self.uti.wait(self.driver,By.XPATH,self.tab_products_xpath)
        self.driver.find_element(By.XPATH,self.tab_products_xpath).click()
    
    def setProductName(self,productName):
        self.uti = reusableFunction(self.driver)
        self.uti.wait(self.driver,By.ID,self.textbox_productName_id)
        self.driver.find_element(By.ID,self.textbox_productName_id).clear()
        self.driver.find_element(By.ID,self.textbox_productName_id).send_keys(productName)
    
    def Click_searchButton(self):
        self.driver.find_element(By.ID,self.button_search_id).click()