ё   1                   # Поменяйте местами ключи и значения в словаре
# {"red": "красный", "green": "зелёный"}

colors = {"red": "красный", "green": "зелёный"}

print(f'Исходный словарь: {colors}')

for color, rcolor in list(colors.items()):
    del colors[color]
    colors[rcolor] = color

print(f'Изменённый словарь: {colors}')