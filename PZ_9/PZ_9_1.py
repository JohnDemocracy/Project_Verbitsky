# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
# мясо, молоко, сыр. Перекресток – молоко, творог, сыр, сахар. Определить:
# 1. полный список всех товаров.
# 2. в каких магазинах можно приобрести одновременно молоко и сыр.
# 3. в каких магазинах можно приобрести сахар.

magnit = {"молоко", "соль", "сахар"}
pyatyorochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}

stores = {
    "Магнит": magnit,
    "Пятёрочка": pyatyorochka,
    "Перекрёсток": perekrestok
}

print(f'Полный список всех товаров: {magnit | pyatyorochka | perekrestok}')

storelist1 = []
storelist2 = []
for store, products in stores.items():
    if "молоко" in products and "сыр" in products:
        storelist1.append(store)
    if "сахар" in products:
        storelist2.append(store)

print(f'Где можно купить сыр и молоко: {", ".join(storelist1)}')
print(f'Где можно купить сахар: {", ".join(storelist2)}')

