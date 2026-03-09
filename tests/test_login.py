
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import (
    EMAIL_BUTTON, 
    REGISTRATION_BUTTON, 
    LOGOUT_BUTTON, 
    MAIN_PAGE_TITLE, 
    LOGIN_BUTTON, 
    PASSWORD_BUTTON, 
    MY_ACCOUNT, 
    NAME_BUTTON, 
    LOGO_Stellar_Burgers, 
    LOGIN_ACCOUNT_BUTTON,
    BASE_URL,
    EMAIL_BUTTON_LOGIN,
    PASSWORD_BUTTON_LOGIN
)

class TestLogin:

    def test_registration_and_login(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
    
        my_name = "Alina42"
        name = f"{my_name}@gmail.com"
        password = "abcabcabc2000"

        wait.until(
         EC.element_to_be_clickable(MY_ACCOUNT)
        ).click()

        wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()

        driver.find_element(*NAME_BUTTON).send_keys(my_name)
        driver.find_element(*EMAIL_BUTTON).send_keys(name)
        driver.find_element(*PASSWORD_BUTTON).send_keys(password)

        wait.until(
        EC.element_to_be_clickable(REGISTRATION_BUTTON)
        ).click()

#вход через кнопку в форме регистрации
        wait.until(
        EC.element_to_be_clickable(EMAIL_BUTTON_LOGIN)
)
        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(name)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear()
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)

        wait.until(
    EC.element_to_be_clickable(LOGIN_BUTTON)
        ).click()
        wait.until(
    EC.visibility_of_element_located(MAIN_PAGE_TITLE)
    )

        driver.find_element(*MY_ACCOUNT).click()
        wait.until(
    EC.visibility_of_element_located(NAME_BUTTON)
        )

#Выход из аккаунта
        driver.find_element(*LOGOUT_BUTTON).click()

#переход по клику на логотип Stellar Burgers
        driver.find_element(*LOGO_Stellar_Burgers).click()
        wait.until(
    EC.visibility_of_element_located(MAIN_PAGE_TITLE)
        )

        driver.find_element(*MY_ACCOUNT).click()

#вход через кнопку «Личный кабинет»
        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(name)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear()
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(
    EC.visibility_of_element_located(MAIN_PAGE_TITLE)
        )

#вход по кнопке «Войти в аккаунт» на главной
        driver.find_element(*MY_ACCOUNT).click()
        driver.find_element(*LOGOUT_BUTTON).click()
        driver.find_element(*LOGO_Stellar_Burgers).click()
        wait.until(
    EC.visibility_of_element_located(MAIN_PAGE_TITLE)
        )

        driver.find_element(*LOGIN_ACCOUNT_BUTTON).click()
        
        driver.find_element(*EMAIL_BUTTON_LOGIN).clear()
        driver.find_element(*EMAIL_BUTTON_LOGIN).send_keys(name)
        driver.find_element(*PASSWORD_BUTTON_LOGIN).clear
        driver.find_element(*PASSWORD_BUTTON_LOGIN).send_keys(password)
        driver.find_element(*LOGIN_BUTTON).click()
        wait.until(
    EC.visibility_of_element_located(MAIN_PAGE_TITLE)
        )
        assert driver.find_element(*MAIN_PAGE_TITLE).is_displayed()