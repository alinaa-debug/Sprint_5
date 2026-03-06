from selenium.webdriver.common.by import By
import random

# Поле ввода имени при регистрации
NAME_BUTTON = (By.XPATH, "(//div[.//h2[text()='Регистрация']]//input[@name='name'])[1]")  # Ввод имени пользователя

# Поле ввода email при регистрации или входе
EMAIL_BUTTON = (By.XPATH, "(//div[.//h2[text()='Регистрация']]//input[@name='name'])[2]")  # Ввод Email

# Поле ввода пароля при регистрации или входе
PASSWORD_BUTTON = (By.XPATH, "//input[@type='password']")  # Ввод пароля

# Кнопка входа в систему
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Нажатие кнопки "Войти"

# Кнопка регистрации нового пользователя
REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Нажатие кнопки "Зарегистрироваться"

# главная страница
MAIN_PAGE_TITLE = (By.XPATH, "//span[text()='Булки']")

# Кнопка выхода из аккаунта
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Нажатие кнопки "Выход"

# Ссылка на личный кабинет пользователя
MY_ACCOUNT = (By.LINK_TEXT, 'Личный Кабинет')  # Переход в раздел "Личный Кабинет"

LOGO_Stellar_Burgers = (By.XPATH, "//a[@class='active']")

LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")