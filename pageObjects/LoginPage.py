from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    button_logout_linktext = "Logout"

    # We need to implement the action method for every locator
    # And before we need to initialize the driver using python cunstructor
    def __init__(self,driver):
        self.driver = driver

    def __init__(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)


    def __init__(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def __init__(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()

    def __init__(self):
        self.driver.find_element(By.LINK_TEXT,self.button_logout_linktext).click()