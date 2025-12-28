import pytest
import allure
from API.api_req import API_profile
from config import base_url,api_url,token

@pytest.fixture
def auth_test():
    api=API_profile()


@allure.feature("Поиск товаров")
@allure.story("API")
@allure.title("Поиск товара на кириллице по названию")
@pytest.mark.api
@pytest.mark.positive
@pytest.mark.parametrize("title", [
    "Граф Аверин"
])
def test_search_api(api_req,title):
    with allure.step("Отправляем запрос на поиск на кириллице по названию"):
        response= api_req.search_books(title)
    with allure.step("Проверяем статус-код"):
        assert response.status_code == 200, "Ожидается статус код 200"

#Проверки:
#1.Поиск товара на кириллице по названию

#2.Поиск товара на латинице по автору
#3.открытие страницы товара при поиске
#4.Добавление товара в корзину
#5.Удаление из корзины
#6.пустой поиск