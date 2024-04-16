from selenium import webdriver
from selenium.webdriver.common.by import By


class Manu:
    tab_Catalog_xpath = "//p[normalize-space()='Catalog']"
    tab_products_xpath = "//p[normalize-space()='Products']"
    textbox_productName_id = "SearchProductName"
    button_search_id = "search-products"

    def __init__(self, driver):
        self.driver = driver

    def Click_manue_catalog(self):
        self.driver.find_element(By.XPATH,self.tab_Catalog_xpath).click()
    
    def Click_manue_products(self):
        self.driver.find_element(By.XPATH,self.tab_products_xpath).click()
    
    def setProductName(self,productName):
        self.driver.find_element(By.ID,self.textbox_productName_id).clear()
        self.driver.find_element(By.ID,self.textbox_productName_id).send_keys(productName)
    
    def Click_searchButton(self):
        self.driver.find_element(By.XPATH,self.button_search_id).click()