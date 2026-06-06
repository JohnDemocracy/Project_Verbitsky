# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы".

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return f"{self.name} выполняет свои обязанности."

    def receive_salary(self):
        return f"{self.name} получил зарплату: {self.salary} руб."

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def manage_team(self):
        return f"{self.name} эффективно управляет командой из {self.team_size} человек."

class Engineer(Employee):
    def __init__(self, name, salary, project):
        super().__init__(name, salary)
        self.project = project

    def project_systems(self):
        return f"{self.name} проектирует новую систему для проекта: {self.project}."

manager = Manager("Анна", 120000, 15)
engineer = Engineer("Иван", 150000, "Облачная инфраструктура")

print(manager.work())
print(manager.receive_salary())
print(manager.manage_team())

print(engineer.work())
print(engineer.receive_salary())
print(engineer.project_systems())