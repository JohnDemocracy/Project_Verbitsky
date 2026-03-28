# Из заданной строки отобразить только символы нижнего регистра. Использовать
# библиотеку string. Строка'In PyCharm, you can specify third-party standalone applications and
# run them as External Tools'.

import string

given = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'

def showlowercase(givenstr):
    output = "".join([c for c in givenstr if c in string.ascii_lowercase])
    return(output)

print(showlowercase(given))