# Создайте класс "Калькулятор" с методами "сложение", "вычитание", "умножение" и
#"деление". Каждый метод должен принимать два аргумента и возвращать результат
# операции.

class Calculator:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a / b
        return "Ошибка: деление на ноль"

calc = Calculator()
print(calc.sum(10, 5))
print(calc.sub(10, 5))
print(calc.mul(10, 5))
print(calc.div(10, 5))