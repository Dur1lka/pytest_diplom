from re import search

import requests
from config import api_url,token

class API_profile

    def __init__(self):
        self.url=api_url
        self.headers = {
            'Autorization':f"Bearer {token}",
            'Content-Type': "application/json"
        }

    def search_books(self,phrase:str):
        search_params = {
            "phrase":phrase
        }
        response = requests.get(self.url + "search/search-phrase-suggests",headers=self.headers,params=search_params)