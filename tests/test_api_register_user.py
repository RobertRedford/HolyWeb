import pytest
from api.api_client import ApiClient
from config.constants import BASE_URL, HEADERS
from api.data import data, old_user_login, old_user_password


'''
Негативный тест проверяет регистрацию уже созданного пользователя.
Данные логина и пароля хранятся в файле data
'''
@pytest.mark.parametrize("email, password", [(f"{old_user_login}", f"{old_user_password}")])
def test_negative_register_user(email, password):
    api_client = ApiClient(BASE_URL, HEADERS)
    response = api_client.register_user(email, password)
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    response_data = response.json()
    assert response_data["detail"] == "Username is taken or pass issue"

'''
Позитивный тест проверяет регистрацию нового пользователя.
Данные логина и пароля генерятся в файле data с помощью библиотеки Faker
'''
@pytest.mark.parametrize("email, password", data)
def test_positive_register_new_user(email, password):
    api_client = ApiClient(BASE_URL, HEADERS)
    response = api_client.register_user(email, password)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    response_data = response.json()
    assert "token" in response_data
    assert "email" in response_data
    assert "id" in response_data
