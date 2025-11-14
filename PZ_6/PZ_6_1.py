# Дан целочисленный список размера 10. Вывести вначале все содержащиеся в данном 
# списке четные числа в порядке возрастания их индексов, а затем — все нечетные 
# числа в порядке убывания их индексов. 

import random

list = []
even = []
odd =  []
N = 10
yes = "Y"
no = "N"
choice = str(input("Ввести список вручную? (Y/N) "))

try:
    while (choice != yes) and (choice != no):
        choice = str(input("Ввести список вручную? (Y/N) "))

    while N > 0:
        N -= 1
        if choice == yes:
            num = int(input(f'Введите {10 - N} число'))
        else:
            num = random.randint(0, 9999)
        list.append(num)
        

    for i in list:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)   
    odd.reverse()

    print(even)
    print(odd)

except ValueError:
    print("Ошибка")