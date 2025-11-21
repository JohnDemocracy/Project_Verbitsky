# Дано четное число N (>0) и символы C1 и C2. Вывести строку длины N, которая
# состоит из чередующихся символов C1 и C2, начиная с C1.

try:    
    C1 = str(input("Введите символ C1 "))
    C2 = str(input("Введите символ C2 "))
    N = int(input("Введите длину строки "))
    string = []

    while N <= 0:
        N = int(input("Введите длину строки "))

    i = 1
    while N != 0:
        if (i % 2) == 1:
            string.append(C1)
        else:
            string.append(C2)
        i += 1
        N -= 1

    print("".join(string))
    
except ValueError:
    print("Ошибка")