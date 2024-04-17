import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.wait import reusableFunction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Manu:
    tab_Catalog_xpath = "//p[normalize-space()='Catalog']"
    tab_products_xpath = "/html[1]/body[1]/div[3]/aside[1]/div[1]/div[4]/div[1]/div[1]/nav[1]/ul[1]/li[2]/ul[1]/li[1]/a[1]/p[1]"
    textbox_productName_id = "SearchProductName"
    button_search_id = "search-products"
    button_addNewProduct_xpath = "//a[@class='btn btn-primary']"
    textbox_newProductName_id = "Name"
    textarea_shortDescription_id = "ShortDescription"
    button_save_id = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def Click_manue_catalog(self):
        # Issue was here
        
        self.uti = reusableFunction(self.driver)
        self.uti.wait(By.XPATH, self.tab_Catalog_xpath)

        self.driver.find_element(By.XPATH,self.tab_Catalog_xpath).click()
    
    def Click_manue_products(self):
        self.uti = reusableFunction(self.driver)
        self.uti.wait(By.XPATH,self.tab_products_xpath)
        self.driver.find_element(By.XPATH,self.tab_products_xpath).click()
    
    def setProductName(self,productName):
        self.uti = reusableFunction(self.driver)
        self.uti.wait(By.ID,self.textbox_productName_id)
        self.driver.find_element(By.ID,self.textbox_productName_id).clear()
        self.driver.find_element(By.ID,self.textbox_productName_id).send_keys(productName)
    
    def Click_searchButton(self):
        self.driver.find_element(By.ID,self.button_search_id).click()


    def Click_addNewProduct(self):
        self.uti = reusableFunction(self.driver)
        time.sleep(3)
        self.uti.wait(By.XPATH,self.button_addNewProduct_xpath)
        self.driver.find_element(By.XPATH,self.button_addNewProduct_xpath).click()
        
    def set_newProductName(self):
        self.uti = reusableFunction(self.driver)
        new_product_name = string.ascii_letters + string.digits + string.punctuation
        self.uti.wait(By.ID,self.textbox_newProductName_id).send_keys(new_product_name)
    
    def set_shortDescription(self):
        self.uti = reusableFunction(self.driver)
        new_shortDescription_name = string.ascii_letters + string.digits + string.punctuation
        self.uti.wait(By.ID,self.textarea_shortDescription_id).send_keys(new_shortDescription_name)

    def Click_Save_Button(self):
        self.uti = reusableFunction(self.driver)
        self.uti.wait(By.ID,self.button_save_id).click()