from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AuthPage:
    def __unit__(self, driver:WebDriver):
        self.__url= "URL страницы"
        self.__driver=driver
    
    def go(self):
        self.__driver.get(self.__url)