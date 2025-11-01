# Составить программу, в которой функция генерирует четырехзначное число и
# определяет, есть ли в числе одинаковые цифры.

import random

def check_for_duplicate_numbers():
    number = random.randint(1000, 9999)

    print(f"Число: {number}")

    first = number // 1000
    second = (number % 1000) // 100
    third = (number % 100) // 10
    fourth = number % 10
    
    current = first
    if (current == second) or (current == third) or (current == fourth):
        print("В числе есть одинаковые цифры")
        return
    else:
        current = second

    if (current == first) or (current == third) or (current == fourth):
        print("В числе есть одинаковые цифры")
        return
    else: 
        current = third

    if (current == first) or (current == second) or (current == fourth):
        print("В числе есть одинаковые цифры")
        return
    else:
        print("В числе нет одинаковых цифр")
        return

check_for_duplicate_numbers()