from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import my_name, name, password, wrong_password, BASE_URL
from locators import (
    EMAIL_BUTTON, 
    REGISTRATION_BUTTON, 
    PASSWORD_BUTTON, 
    MY_ACCOUNT, 
    NAME_BUTTON, 
    EMAIL_BUTTON_LOGIN
)
import random

class TestRegistration:

    def test_valid_registration(self, driver):

        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)

        # переход в личный кабинет
        wait.until(
            EC.element_to_be_clickable(MY_ACCOUNT)
        ).click()

        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()

        wait.until(
            EC.visibility_of_element_located(NAME_BUTTON)
        )

        # ошибка для некорректного пароля
        driver.find_element(*NAME_BUTTON).send_keys(my_name)
        driver.find_element(*EMAIL_BUTTON).send_keys(name)
        driver.find_element(*PASSWORD_BUTTON).send_keys(password)
        driver.find_element(*REGISTRATION_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(EMAIL_BUTTON_LOGIN))
        

    def test_registration_with_wrong_password(self, driver):

        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.element_to_be_clickable(MY_ACCOUNT)
        ).click()

        wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()

        wait.until(
            EC.visibility_of_element_located(NAME_BUTTON))
        

        driver.find_element(*NAME_BUTTON).clear()
        driver.find_element(*NAME_BUTTON).send_keys(my_name)

        driver.find_element(*EMAIL_BUTTON).clear()
        driver.find_element(*EMAIL_BUTTON).send_keys(name)

        driver.find_element(*PASSWORD_BUTTON).clear()
        driver.find_element(*PASSWORD_BUTTON).send_keys(wrong_password)

        driver.find_element(*REGISTRATION_BUTTON).click()
        
        assert wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']"))
        )
        
        