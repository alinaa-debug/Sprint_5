import random



class Urls:
    BASE_URL = "https://stellarburgers.education-services.ru/"


class UserData:

    name = f"Alinarakhimiyanova42{random.randint(100, 999)}"

    email = f"{name}@example.com"

    password = f'a{random.randint(100000,999999)}'

    wrong_password = "12"



