# В исходном текстовом файле(Dostoevsky.txt) найти все варианты фамилии
# Достоевского (т.е. с различными окончаниями, например, Достоевский,
# Достоевского) в единственном экземпляре.

import re

def find_dostoevsky_variants():
    file = open(r'C:\RKSI\OAP\Project_Verbitsky\PZ_13\Dostoevsky.txt', 'r', encoding='utf-8')
    text = file.read()
    pattern = r'\bДостоевск[а-я]+\b'
    matches = re.findall(pattern, text, re.UNICODE)
    unique_variants = []
    for word in matches:
        if word not in unique_variants:
            unique_variants.append(word)
    
    return unique_variants

print(find_dostoevsky_variants())