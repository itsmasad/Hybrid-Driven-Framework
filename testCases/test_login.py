import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"