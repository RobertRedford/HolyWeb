import pytest
from ui.pages import *
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config.constants import REGISTER_URL, PROFILE_URL
from api.data import login_data, password_data, old_user_login, old_user_password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def browser():
    options = Options()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

'''
Негативный тест проверяет регистрацию уже созданного пользователя.
Данные логина и пароля хранятся в файле data
'''
def test_negative_register(browser):
    browser.get(f"{REGISTER_URL}")
    login_field(browser).send_keys(f"{old_user_login}")
    password_field(browser).send_keys(f"{old_user_password}")
    password_confirmation_field(browser).send_keys(f"{old_user_password}")
    login_field(browser).click()
    submit_button(browser).click()
    wait = WebDriverWait(browser, 5)
    assert wait.until(EC.url_to_be(f"{REGISTER_URL}"))
    assert something_went_wrong_msg(browser).text == "Something went wrong"


'''
Позитивный тест проверяет регистрацию нового пользователя.
Данные логина и пароля генерятся в файле data с помощью библиотеки Faker
'''
def test_positive_register(browser):
    browser.get(f"{REGISTER_URL}")
    login_field(browser).send_keys(f"{login_data}")
    password_field(browser).send_keys(f"{password_data}")
    password_confirmation_field(browser).send_keys(f"{password_data}")
    login_field(browser).click()
    submit_button(browser).click()
    wait = WebDriverWait(browser, 5)
    wait.until(EC.url_to_be(f"{PROFILE_URL}"))
    assert no_records_found_msg(browser).is_displayed()
    assert adding_descriptions_block(browser).is_displayed()
    assert profile_menu_icon(browser).is_displayed()

