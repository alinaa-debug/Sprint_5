import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    EMAIL_BUTTON,
    PASSWORD_BUTTON,
    REGISTRATION_BUTTON,
    MY_ACCOUNT,
    NAME_BUTTON,
    BASE_URL,
    EMAIL_BUTTON_LOGIN
)


class TestRegistration:

    def test_registration(self, driver):

        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)

        my_name = f"Alinarakhimiyanova42{random.randint(100, 999)}"
        name = f"{my_name}@example.com"

        password = f'a{random.randint(100000,999999)}'
        wrong_password = "12"

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
        driver.find_element(*PASSWORD_BUTTON).send_keys(wrong_password)
        driver.find_element(*REGISTRATION_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//p[text()='Некорректный пароль']"))
        )

        # успешная регистрация
        driver.find_element(*NAME_BUTTON).clear()
        driver.find_element(*NAME_BUTTON).send_keys(my_name)

        driver.find_element(*EMAIL_BUTTON).clear()
        driver.find_element(*EMAIL_BUTTON).send_keys(name)

        driver.find_element(*PASSWORD_BUTTON).clear()
        driver.find_element(*PASSWORD_BUTTON).send_keys(password)

        driver.find_element(*REGISTRATION_BUTTON).click()

        wait.until(
            EC.visibility_of_element_located(EMAIL_BUTTON_LOGIN)
        )