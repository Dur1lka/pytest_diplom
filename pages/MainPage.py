from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self,driver:WebDriver):
        self.__driver=driver
    # Получаем текущий URL
    def get_current_url(self,param:str):
        return self.__driver.current_url
    # Нажимаем на иконку с именем в верхней части экрана
    def open_menu(self):
        self.__driver.find_element(By.CSS_SELECTOR,"button[aria-label='меню профиля']").click()
    # Получаем информацию о пользователе:
    def get_account_info(self,param:list[str]):
        # Ищем имя пользователя:
        container=self.__driver.find_element(By.CSS_SELECTOR,"div[profile-page_user-name]")
        fields=container.find_element(By.CSS_SELECTOR,"div")
        name=fields[0].text
    # Возвращаем имя пользователя:
    return [name]