from selenium.webdriver.common.by import By



# Поле ввода имени при регистрации
NAME_BUTTON = (By.XPATH, "(//input[@type='text'])[1]") # Ввод имени пользователя

# Поле ввода email при регистрации 
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

# Логотип Stellar Burgers
LOGO_Stellar_Burgers = (By.XPATH, "//a[@class='active']")  # Переход на главную страницу по клику на логотип

# Кнопка "Войти в аккаунт" на главной странице
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Открытие формы входа

# Категории ингредиентов на странице конструктора
IMG_SAUCE_SPICY_X = (By.XPATH, "//span[text()='Соусы']/..")  # Выбор раздела "Соусы"
IMG_FILLING = (By.XPATH, "//span[text()='Начинки']/..")      # Выбор раздела "Начинки"
IMG_BULKI = (By.XPATH, "//span[text()='Булки']/..")          # Выбор раздела "Булки"

# Ссылка для восстановления пароля
RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")  # Переход в форму восстановления пароля

# Кнопка "Войти" в форме восстановления пароля
LODIN_IN_RECOVERY = (By.XPATH,"//a[text()='Войти']")  # Вход через форму восстановления пароля

# Ссылка "Зарегистрироваться" в форме входа
REGISTRATION = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Переход в форму регистрации

# Кнопка "Войти" в форме регистрации
LOD_IN = (By.XPATH, "//a[text()= 'Войти']")  # Переход из формы регистрации обратно в форму входа

LINK_REGISTRATION = (By.LINK_TEXT, "Зарегистрироваться")

#Некорректный пароль
INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")