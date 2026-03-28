# Из предложенного текстового файла (text18-9.txt) вывести на экран его содержимое,
# количество букв в нижнем регистре. Сформировать новый файл, в который поместить текст
# в стихотворной форме предварительно поставив последнюю строку фразой введенной
# пользователем.

# Содержимое

textfile1 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text18-9.txt', 'r', encoding='utf-8')
text = textfile1.read()

# Количество букв в нижнем регистре

letters = " ".join(text).split()
lowercount = 0
for i in letters:
    if i.islower() == True:
        lowercount += 1

# Формирование нового файла с добавленной строкой

textlist = "".join(text).split("\n")
addtext = str(input("Введите дополнительную строку: "))
textlist.append(addtext)
newtext = "\n".join(textlist)

textfile2 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text18-9-2.txt', 'w', encoding='utf-8')
textfile2.write(newtext)
textfile2.close

textfile2 = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_10\text18-9-2.txt', 'r', encoding='utf-8')

print(f"Содержимое файла:\n\n{text}\n")
print(f"Количество букв в нижнем регистре: {lowercount}\n")
print(f"Новый файл:\n\n{textfile2.read()}")