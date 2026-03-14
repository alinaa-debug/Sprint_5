
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls,UserData, Password
from locators import (
    EMAIL_BUTTON, 
    REGISTRATION_BUTTON, 
    PASSWORD_BUTTON, 
    MY_ACCOUNT, 
    NAME_BUTTON, 
    EMAIL_BUTTON_LOGIN,
    LINK_REGISTRATION,
    ERROR_MESSAGE
)

class TestRegistration:

    def test_valid_registration(self, driver):
        driver.get(Urls.BASE_URL)

        wait = WebDriverWait(driver, 10)

        # переход в личный кабинет
        wait.until(
            EC.element_to_be_clickable(MY_ACCOUNT)
        ).click()

        wait.until(
            EC.element_to_be_clickable(LINK_REGISTRATION)
        ).click()

        wait.until(
            EC.visibility_of_element_located(NAME_BUTTON)
        )

        
        driver.find_element(*NAME_BUTTON).send_keys(UserData.name)
        driver.find_element(*EMAIL_BUTTON).send_keys(UserData.email)
        driver.find_element(*PASSWORD_BUTTON).send_keys(UserData.password)
        driver.find_element(*REGISTRATION_BUTTON).click()

        assert wait.until(
            EC.visibility_of_element_located(EMAIL_BUTTON_LOGIN))
        

    def test_registration_with_wrong_password(self, driver):

        driver.get(Urls.BASE_URL)

        wait = WebDriverWait(driver, 10)

        wait.until(
            EC.element_to_be_clickable(MY_ACCOUNT)
        ).click()

        wait.until(
            EC.element_to_be_clickable(LINK_REGISTRATION)
        ).click()

        wait.until(
            EC.visibility_of_element_located(NAME_BUTTON))
        

        driver.find_element(*NAME_BUTTON).send_keys(UserData.name)
        driver.find_element(*EMAIL_BUTTON).send_keys(UserData.email)
        driver.find_element(*PASSWORD_BUTTON).send_keys(UserData.wrong_password)

        driver.find_element(*REGISTRATION_BUTTON).click()
        error = wait.until(
            EC.visibility_of_element_located(ERROR_MESSAGE)
        )
        assert Password.INCORRECT_PASSWORD in error.text
        
        