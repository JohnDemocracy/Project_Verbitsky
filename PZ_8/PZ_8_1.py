# Удалите ключи ["name", "salary"] из sample_dict

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

print(f"Начальный словарь: {sample_dict}")

del sample_dict["name"]
del sample_dict["salary"]

print(f"Изменённый словарь: {sample_dict}")