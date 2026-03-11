import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from data import Urls,UserData
from locators import (MY_ACCOUNT,
NAME_BUTTON,
EMAIL_BUTTON,
PASSWORD_BUTTON,
REGISTRATION_BUTTON,
MAIN_PAGE_TITLE,
EMAIL_BUTTON_LOGIN,
PASSWORD_BUTTON_LOGIN,
LOGIN_BUTTON,
LINK_REGISTRATION)

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture
def registered_user(driver):
    
    wait = WebDriverWait(driver, 10)

    driver.get(Urls.BASE_URL)


    wait.until(EC.element_to_be_clickable(MY_ACCOUNT)).click()

    wait.until(
        EC.element_to_be_clickable(LINK_REGISTRATION)
    ).click()

    driver.find_element(*NAME_BUTTON).send_keys(UserData.name)
    driver.find_element(*EMAIL_BUTTON).send_keys(UserData.email)
    driver.find_element(*PASSWORD_BUTTON).send_keys(UserData.password)

    driver.find_element(*REGISTRATION_BUTTON).click()
    wait.until(
        EC.visibility_of_element_located(EMAIL_BUTTON_LOGIN))
    
    return UserData.email, UserData.password


@pytest.fixture
def logged_in_user(driver, registered_user):
    
    my_email, my_password = registered_user
    driver.get(Urls.BASE_URL)
    wait = WebDriverWait(driver, 10)

    driver.find_element(*MY_ACCOUNT).click()
    driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(my_email)
    driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(my_password)
    driver.find_element(*LOGIN_BUTTON).click()
    wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))
    return driver