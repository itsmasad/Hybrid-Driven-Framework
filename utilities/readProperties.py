# This file will read the data from ini (config.ini) file
import configparser

config = configparser.RawConfigParser()
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