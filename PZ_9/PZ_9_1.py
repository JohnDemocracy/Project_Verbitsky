# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.

magnit = {"молоко", "соль", "сахар"}
pyatyorochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}

listselect = input("Использовать вариант со списками и кортежами? (Y/N) ")

while listselect.lower() != 'y' and listselect.lower() != 'n':
   listselect = input("Использовать вариант со списками? (Y/N) ") 

storeshaveitems1 = set()
storeshaveitems2 = set()

# Без списков и кортежей:

neededitems1 = {"молоко", "сыр"}
neededitems2 = {"сахар"}

if listselect.lower() == 'n':

    if neededitems1.issubset(magnit):
        storeshaveitems1.add("Магнит")
    if neededitems1.issubset(pyatyorochka):
        storeshaveitems1.add("Пятёрочка")
    if neededitems1.issubset(perekrestok):
        storeshaveitems1.add("Перекрёсток")

    if neededitems2.issubset(magnit):
        storeshaveitems2.add("Магнит")
    if neededitems2.issubset(pyatyorochka):
        storeshaveitems2.add("Пятёрочка")
    if neededitems2.issubset(perekrestok):
        storeshaveitems2.add("Перекрёсток")

# Со списками и кортежами:

else:
    storelist = [("Магнит", magnit), ("Пятёрочка", pyatyorochka), ("Перекрёсток", perekrestok)]
    for store, products in storelist:
        if 'молоко' in products and 'сыр' in products:
            storeshaveitems1.add(store)
        if 'сахар' in products:
            storeshaveitems2.add(store)


print(f'Полный список всех товаров: {magnit | pyatyorochka | perekrestok}')
print(f'Где можно купить сыр и молоко: {storeshaveitems1}')
print(f'Где можно купить сахар: {storeshaveitems2}')