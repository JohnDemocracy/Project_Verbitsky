# Дана строка '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15', отражающая средние
# температуры по месяцам в году. Преобразовать информацию из строки в словарь, с
# использованием функции найти среднюю и минимальные температуры, результаты
# вывести на экран

string = '2020год -16 -10 -6 4 20 32 36 32 32 15 1 -15'
dictkeys = ["year", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
temps = {}

def minmaxtemp(dictionary):
    values = [int(i) for i in list(dictionary.values())[1:]]
    mintemp = min(values)
    avgtemp = sum(values) // len(values)
    print(f"Минимальная температура: {mintemp}")
    print(f"Средняя температура: {avgtemp}")

for idx, val in enumerate(string.split()):
    temps[dictkeys[idx]] = val

print(f"Словарь: {temps}")

minmaxtemp(temps)

