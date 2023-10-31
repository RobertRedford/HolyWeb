from typing import Union
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_field(browser) -> Union[WebElement, None]:
    login_field = browser.find_element(By.XPATH, "//input[@id='login']")
    return login_field

def password_field(browser) -> Union[WebElement, None]:
    password_field = browser.find_element(By.XPATH, "//div[@id='password']//input[@type='password']")
    return password_field

def password_confirmation_field(browser) -> Union[WebElement, None]:
    password_confirmation_field = browser.find_element(By.XPATH, "//div[@id='confirm_password']//input[@type='password']")
    return password_confirmation_field

def submit_button(browser) -> Union[WebElement, None]:
    submit_button = browser.find_element(By.XPATH, "//span[@class='p-button-label']")
    return submit_button

def adding_descriptions_block(browser) -> Union[WebElement, None]:
    adding_descriptions_block = browser.find_element(By.XPATH, "//div[@class='p-dataview-header']")
    return adding_descriptions_block

def profile_menu_icon(browser) -> Union[WebElement, None]:
    profile_menu_icon = browser.find_element(By.XPATH, "//span[normalize-space()='Profile']")
    return profile_menu_icon

def quit_menu_icon(browser) -> Union[WebElement, None]:
    quit_menu_icon = browser.find_element(By.XPATH, "//span[normalize-space()='Quit']")
    return quit_menu_icon

def no_records_found_msg(browser) -> Union[WebElement, None]:
    no_records_found_msg = browser.find_element(By.XPATH, "//div[@class='p-dataview-emptymessage']")
    return no_records_found_msg

def something_went_wrong_msg(browser):
    wait = WebDriverWait(browser, 10)
    something_went_wrong_msg = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='p-message-text']")))
    return something_went_wrong_msg
