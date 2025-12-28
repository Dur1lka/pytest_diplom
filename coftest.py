import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import base_url


@pytest.fixture
def browser():
    browser=webdriver.Chrome()
    browser.implicitly_wait(4)
    browser.maximize_window()
    browser.get(base_url)
    yield browser

    browser.quit()