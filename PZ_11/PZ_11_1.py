# Даны две последовательности. Найти элементы, общие для двух
# последовательностей и их количество.

import random

def makelist():
    list1 = [random.randint(1, 100) for i in range(20)]
    list2 = [random.randint(1, 100) for i in range(20)]
    print(f"Последовательность 1: {list1}\nПоследовательность 2: {list2}")
    return list1, list2

def findsimiliar(a, b):
    set1 = set(a)
    set2 = set(b)
    set3 = set1 & set2
    print(f"Общие элементы: {set3}")
    return(set3)

def findsimiliarcount(c):
    list3 = list(c)
    lenlist3 = len(list3)
    print(f"Количество общих элементов: {lenlist3}")
    return(lenlist3)

returned_list1, returned_list2 = makelist()
returned_set = findsimiliar(returned_list1, returned_list2)
findsimiliarcount(returned_set)