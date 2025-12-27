import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AuthPage:
    def __init__(self, driver:WebDriver):
        self.__url= "URL страницы"
        self.__driver=driver
    
    def go(self):
        self.__driver.get(self.__url)

    def auth_token():
        headers={
            'Autorization':f"Bearer{token}",
            'Content-Type': "aplication/json"
        }
        resp=requests.post(base_url)
        response_data=resp.json()