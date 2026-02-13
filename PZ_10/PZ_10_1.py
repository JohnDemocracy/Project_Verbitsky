# Средствами языка Python сформировать текстовый файл (.txt), содержащий
# последовательность из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:
# Исходные данные:
# Количество элементов:
# Индекс последнего максимального элемента:
# Меняем местами первую и последнюю трети:

import random

# Создание первого файла

numbers = [str(random.randint(-100, 100)) for i in range(12)]
textfile1 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text1.txt', 'w', encoding='utf-8')
textfile1.write(" ".join(numbers))
textfile1.close

# Исходные данные

textfile1 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text1.txt', encoding='utf-8')
textfile2 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text2.txt', 'w', encoding='utf-8')
textfile2.write(f"Исходные данные: {textfile1.read()}")
textfile2.close

# Количество элементов

textfile1 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text1.txt', encoding='utf-8')
length = len((textfile1.read()).split())

# Последний максимальный элемент

textfile1 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text1.txt', encoding='utf-8')
intlist = [int(i) for i in (textfile1.read()).split()]
maxnum = max(intlist)
maxnumint = length - 1 - intlist[::-1].index(maxnum)

# Меняем местами первую и последнюю трети

textfile1 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text1.txt', encoding='utf-8')
tf1contents = textfile1.read().split()
ft = tf1contents[:(length//3)]
st = tf1contents[(length//3*2):]
tf1contents[:(length//3)] = st
tf1contents[(length//3*2):] = ft
thirdslist = " ".join(tf1contents)

# Запись в файл

textfile2 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text2.txt', 'a', encoding='utf-8')
textfile2.write(f"\nКоличество элементов: {length}")
textfile2.write(f"\nИндекс последнего максимального элемента: {maxnumint}")
textfile2.write(f"\nЗаменённые трети: {thirdslist}")
textfile2.close

textfile2 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text2.txt', 'r', encoding='utf-8')
print(textfile2.read())