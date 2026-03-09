
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import BASE_URL

class TestConstructor:
    # Соусы
    def test_open_sauces(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
   
        sauce_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Соусы']"))
        )
        sauce_button.click()

        sauce_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='Соус Spicy-X']"))
)
        assert sauce_title.is_displayed()

# Начинки
    def text_open_filling(self,driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver,3)

        filling_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Начинки']"))
        )
        filling_button.click()

        filling_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='Мясо бессмертных моллюсков Protostomia']"))
        )
        assert filling_title.is_displayed()

# Булки
    def text_open_bulki(self,driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver,3)
        bulki_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Булки']"))
        )
        bulki_button.click()

        bulki_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']"))
        )
        assert bulki_title.is_displayed()

        