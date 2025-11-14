# Дан список размера N. Найти количество участков, на которых его элементы 
# монотонно убывают.

import random

list = []
currentIndex = 0
previousIndex = 0
descendingSectionsCounter = 0
inDescendingSection = 0
yes = "Y"
no = "N"

try:
    N = int(input("Введите размер списка "))
    totalN = N
    choice = str(input("Ввести список вручную? (Y/N) "))

    while (choice != yes) and (choice != no):
        choice = str(input("Ввести список вручную? (Y/N) "))

    # Выбор между ручным и автоматическим созданием списка

    while N > 0:
        N -= 1
        if choice == yes:
            num = int(input(f'Введите {totalN - N} число'))
        else:
            num = random.randint(0, 9999)
        list.append(num)

    # Созданием списка

    for i in list:
        if previousIndex == 0:
            previousIndex = i
        else:
            currentIndex = i
            if (currentIndex < previousIndex):
                if (inDescendingSection == 0):
                    descendingSectionsCounter += 1
                    inDescendingSection = 1
            else:
                    inDescendingSection = 0
        previousIndex = i

    # Проверка на монотонное убывание. inDescendingSection отвечает за положение на участке: при 0, мы не находимся
    # на участке убывания, а при 1 - находимся. 

    print(list)
    print(descendingSectionsCounter)

except ValueError:
    print("Ошибка")
