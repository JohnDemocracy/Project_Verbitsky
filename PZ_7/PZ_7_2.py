# Дана строка, содержащая полное имя файла, то есть имя диска, список каталогов
# (путь), собственно имя и расширение. Выделить из этой строки имя файла (без
# расширения).

import random

location = ["C:"]
N = random.randint(2, 7)
FileName = str(input("Введите название файла "))
Extension = str(input("Введите расширение файла ")).replace(".", "")
FullFileName = FileName + "." + Extension

i = 1
while N != 0:
    if N == 1:
        location.append(FullFileName)
    else:
        location.append(f'Location{i}')
    N -= 1
    i += 1

FullLocation = "/".join(location)
FindFileName = ((((FullLocation.split("/"))[-1]).split("."))[0])

print(FullLocation)
print(FindFileName)
