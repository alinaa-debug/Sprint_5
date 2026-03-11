from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import BASE_URL
from locators import (
    MAIN_PAGE_TITLE, 
    LOGIN_BUTTON, 
    MY_ACCOUNT, 
    LOGIN_ACCOUNT_BUTTON,
    BASE_URL,
    EMAIL_BUTTON_LOGIN,
    PASSWORD_BUTTON_LOGIN,
    RECOVER_PASSWORD,
    LODIN_IN_RECOVERY,
    REGISTRATION,
    LOD_IN
)
import pytest


class TestLogin:
    # вход через кнопку «Личный кабинет»
    def test_login_personal_account(self, driver,registered_user):
        email, password = registered_user
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)

        driver.find_element(*MY_ACCOUNT).click()
       
        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(email)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear()
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))
       
        assert driver.find_element(*MAIN_PAGE_TITLE).is_displayed()


    # вход через кнопку в форме регистрации
    def test_login_via_registration_form(self,driver,registered_user):
        email, password = registered_user
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        driver.find_element(*MY_ACCOUNT).click()
        driver.find_element(*REGISTRATION).click()
        driver.find_element(*LOD_IN).click()

        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(email)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear()
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))
        assert driver.find_element(*MAIN_PAGE_TITLE).is_displayed()


       
    # вход по кнопке «Войти в аккаунт» на главной
    def test_by_clicking_the_login_button(self,driver,registered_user):
        email, password = registered_user
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        
        driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()

        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(email)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear()
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))

        assert driver.find_element(*MAIN_PAGE_TITLE).is_displayed()


        #ход через кнопку в форме восстановления пароля
    def test_login_in_the_password_recovery_form(self,driver,registered_user):
        email, password = registered_user
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        driver.find_element(*MY_ACCOUNT).click()
        driver.find_element(*RECOVER_PASSWORD).click()
        driver.find_element(*LODIN_IN_RECOVERY).click()


        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(email)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear()
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()

        wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))

        assert driver.find_element(*MAIN_PAGE_TITLE).is_displayed()



        