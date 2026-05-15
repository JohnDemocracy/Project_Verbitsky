# В матрице найти среднее арифметическое положительных элементов, кратных 3 

import random

def generate():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = [[random.randint(-30, 30) for _ in range(cols)] for _ in range(rows)]
    return matrix

def printmatrix(a):
    print(f"Матрица: {matrix}")

def findelement(a):
    filtered = [num for row in matrix for num in row if num > 0 and num % 3 == 0]
    if filtered:
        print(f"Элементы, кратные 3: {filtered}")
        avg = sum(filtered) / len(filtered)
        print(f"Среднее арифметическое: {avg:.2f}")
    else:
        print(f"Нет положительных элементов, кратных 3")

matrix = generate()
printmatrix(matrix)
findelement(matrix)