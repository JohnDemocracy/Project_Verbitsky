# Дано множество A из N точек на плоскости и точка B (точки заданы своими 
# координатами х, у). Найти точку из множества A, наиболее близкую к точке B. 
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по 
# формуле: R = √(x2 – x1)^2 + (у2 – y1)^2.

import math
import random

points = []
B = [random.randint(0, 50), random.randint(0, 50)]
previousDistance = 9999999
N = int(input("Введите кол-во точек"))

while N > 0:
    N -= 1
    points.append([random.randint(0, 50), random.randint(0, 50)])

for point in points:
    distance = math.sqrt((B[0] - point[0]) ** 2 + (B[1] - point[1]) ** 2)
    if distance < previousDistance:
        previousDistance = distance
        targetPoint = point

print(f"Вторая точка: {B}")
print(f"Ближайшая точка: {targetPoint}")
print(f"Расстояние: {round(distance)}")