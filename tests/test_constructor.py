
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from data import Urls
from locators import (
    IMG_SAUCE_SPICY_X,
    IMG_FILLING,
    IMG_BULKI)

class TestConstructor:
    # Соусы.
    def test_open_sauces(self, driver):
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver, 3)
   
        sauce_button = wait.until(
        EC.element_to_be_clickable(IMG_SAUCE_SPICY_X)
        )
        sauce_button.click()
        assert "tab_tab_type_current" in sauce_button.get_attribute("class")

# Начинки
    def test_open_filling(self,driver):
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver,3)

        filling_button = wait.until(
        EC.element_to_be_clickable(IMG_FILLING)
        )
        filling_button.click()

        assert "tab_tab_type_current" in filling_button.get_attribute('class')

# Булки
    def test_open_bulki(self,driver):
        driver.get(Urls.BASE_URL)
        wait = WebDriverWait(driver,3)
        driver.find_element(*IMG_SAUCE_SPICY_X).click()
        
        bulki_button = wait.until(
        EC.element_to_be_clickable(IMG_BULKI)
        )
        bulki_button.click()

        assert "tab_tab_type_current" in bulki_button.get_attribute('class')

        