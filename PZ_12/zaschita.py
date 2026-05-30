# Напишите функцию maskEmail, которая принимает адрес электронной почты (строку) и возвращает его с замаскированной частью до символа '@'. Все символы до '@', кроме первого и последнего, должны быть заменены на '*'.  
# Пример:  
# "example@mail.com" -> "e*****e@mail.com"  
# "a@b.com" -> "a@b.com"

#def maskEmail(e):
#    at = e.find('@')
#    return e if at <= 2 else e[0] + '*' * (at - 2) + e[at - 1:]\

email = input("Введите почту: ")

maskEmail = lambda e: e if (at:=e.find('@')) <= 2 else e[0] + '*' * (at-2) + e[at - 1:]

print(maskEmail(email))
