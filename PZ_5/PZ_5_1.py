# Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры.

import random

def check_for_duplicate_numbers():
    number = random.randint(1000, 9999)

    print(f"Число: {number}")

    number_str = str(number)
    if len(set(number_str)) < 4:
        print("В числе есть одинаковые цифры")
    else:
        print("В числе нет одинаковых цифр")

check_for_duplicate_numbers()