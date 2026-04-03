# Даны две последовательности. Найти элементы, общие для двух
# последовательностей и их количество.

import random

def makelist():
    list1 = [random.randint(1, 100) for i in range(20)]
    list2 = [random.randint(1, 100) for i in range(20)]
    print(f"Последовательность 1: {list1}\nПоследовательность 2: {list2}")
    return(list1, list2)

def findsimiliar(a, b):
    set3 = {x for x in a if x in b}
    print(f"Общие элементы: {set3}")
    return(set3)

def findsimiliarcount(c):
    print(f"Количество общих элементов: {len(list(c))}")
    return(len(list(c)))

returned_list1, returned_list2 = makelist()
returned_set = findsimiliar(returned_list1, returned_list2)
findsimiliarcount(returned_set)