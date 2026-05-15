number = input("Введите цифру: ")

def makenewnumber(a):
    return int("".join(str(int(digit)**2) for digit in a if digit.isdigit()))
print(makenewnumber(number))