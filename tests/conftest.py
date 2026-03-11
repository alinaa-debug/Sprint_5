import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from data import BASE_URL
from locators import (MY_ACCOUNT,
NAME_BUTTON,
EMAIL_BUTTON,
PASSWORD_BUTTON,
REGISTRATION_BUTTON,
EMAIL_BUTTON_LOGIN,
MAIN_PAGE_TITLE,
EMAIL_BUTTON_LOGIN,
PASSWORD_BUTTON_LOGIN,
LOGIN_BUTTON)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture
def registered_user(driver):
    
    wait = WebDriverWait(driver, 10)

    driver.get(BASE_URL)
    my_name_test_lodin = "Alina42"

    name_for_test_lodin = f"{my_name_test_lodin}@gmail.com"

    password_for_test_login = "abcabcabc2000"

    wait.until(EC.element_to_be_clickable(MY_ACCOUNT)).click()

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
    ).click()

    driver.find_element(*NAME_BUTTON).send_keys(my_name_test_lodin)
    driver.find_element(*EMAIL_BUTTON).send_keys(name_for_test_lodin)
    driver.find_element(*PASSWORD_BUTTON).send_keys(password_for_test_login)

    driver.find_element(*REGISTRATION_BUTTON).click()
    wait.until(
        EC.visibility_of_element_located(*EMAIL_BUTTON_LOGIN))
    
    return name_for_test_lodin, password_for_test_login


@pytest.fixture
def logged_in_user(driver, registered_user):
    
    email, password = registered_user
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 10)

    driver.find_element(*MY_ACCOUNT).click()
    driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(email)
    driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
    driver.find_element(*LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))
    return driver