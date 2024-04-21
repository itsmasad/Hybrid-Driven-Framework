# This file will read the data from ini (config.ini) file
# configparser module provides functionality to work with configuration files.
import configparser

# Creating an instance of RawConfigParser class called config
config = configparser.RawConfigParser()
# Reading the contents of the configuration file named config.ini
config.read(".\\Configurations\\config.ini")

class ReadConfig():
    #Creating staticmethod so we can directly acces using class name without creating any object
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info','username')
        return username
        
    @staticmethod
    def getUserpassword():
        password = config.get('common info','password')
        return password
    
    @staticmethod
    def getProductFilterData():
        productName = config.get('product filter','productName')
        return productName