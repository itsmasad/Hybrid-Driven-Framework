from selenium import webdriver
from selenium.webdriver.common.by import By


class Manu:
    tab_Catalog_xpath = "//p[normalize-space()='Catalog']"
    tab_products_xpath = "//p[normalize-space()='Products']"
    textbox_productName_id = "SearchProductName"

    def __init__(self, driver):
        self.driver = driver

    def Click_manue_catalog(self):
        self.driver.find_element(By.XPATH,self.tab_Catalog_xpath).click()