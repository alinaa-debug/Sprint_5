
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (MY_ACCOUNT, 
LOGO_Stellar_Burgers, 
LOGOUT_BUTTON, 
MAIN_PAGE_TITLE,
EMAIL_BUTTON_LOGIN)

class TestNavigation:
    # Проверяем, что личный кабинет открылся..
    def test_go_to_personal_account(self, logged_in_user):
        wait = WebDriverWait(logged_in_user, 10)

        logged_in_user.find_element(*MY_ACCOUNT).click()
        assert wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))
        

    # Проверяем, что конструктор открыт
    def test_go_to_constructor(self, logged_in_user):
        wait = WebDriverWait(logged_in_user, 10)

        logged_in_user.find_element(*MY_ACCOUNT).click()
        logged_in_user.find_element(*LOGO_Stellar_Burgers).click()
        assert wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE))
        

    
    # Проверяем, что пользователь вышел
    def test_logout_from_account(self, logged_in_user):
        wait = WebDriverWait(logged_in_user, 10)

        logged_in_user.find_element(*MY_ACCOUNT).click()
        logged_in_user.find_element(*LOGOUT_BUTTON).click()
        assert wait.until(EC.visibility_of_element_located(EMAIL_BUTTON_LOGIN))
        















