from selenium.webdriver.common.by import By
import random

#Ссылка URL
BASE_URL = "https://stellarburgers.education-services.ru/"

# Поле ввода имени при регистрации
NAME_BUTTON = (By.XPATH, "(//input[@type='text'])[1]") # Ввод имени пользователя

# Поле ввода email при регистрации или входе
EMAIL_BUTTON = (By.XPATH, "(//input[@type='text'])[2]")  # Ввод Email

# Поле ввода email при входе
EMAIL_BUTTON_LOGIN = (By.NAME, "name") 

# Поле ввода пароля при регистрации
PASSWORD_BUTTON = (By.XPATH, "//input[@type='password']")

# Поле ввода пароля при входе
PASSWORD_BUTTON_LOGIN = (By.XPATH, "//input[@type='password']")  # Ввод пароля

# Кнопка входа в систему
LOGIN_BUTTON = (By.XPATH, ".//form//button[text()='Войти']")# Нажатие кнопки "Войти"

# Кнопка регистрации нового пользователя
REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Нажатие кнопки "Зарегистрироваться"

# главная страница
MAIN_PAGE_TITLE = (By.XPATH, "//span[text()='Булки']")

# Кнопка выхода из аккаунта
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Нажатие кнопки "Выход"

# Ссылка на личный кабинет пользователя
MY_ACCOUNT = (By.XPATH, "//p[text()='Личный Кабинет']")  # Переход в раздел "Личный Кабинет"

LOGO_Stellar_Burgers = (By.XPATH, "//a[@class='active']")

LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")