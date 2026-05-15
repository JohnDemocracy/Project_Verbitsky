# В матрице элементы второго столбца заменить элементами из одномерного
# динамического массива соответствующей размерности.

import random

def generate():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = [[random.randint(1, 9) for _ in range(cols)] for _ in range(rows)]
    dynamic_array = [random.randint(0, 10) for _ in range(rows)]
    return matrix, dynamic_array

def printset(matrix, array):
    print(f"Начальная матрица: {matrix}")
    print(f"Одномерный массив: {array}")

def replacecolumn(matrix, array):
    for i in range(len(matrix)):
        matrix[i][1] = array[i]
    print(f"Новая матрица: {matrix}")

matrix, array = generate()
printset(matrix, array)
replacecolumn(matrix, array)