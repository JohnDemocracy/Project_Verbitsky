import sqlite3
import sys

database = 'plan.db'

def insert_data():
    initial_data = [
        ('Д01', 'Программирование', 'ИС', 36, 36, 18, 'Экзамен'),
        ('Д02', 'Базы данных', 'ИС', 36, 18, 36, 'Экзамен'),
        ('Д03', 'Высшая математика', 'ИС', 72, 72, 0, 'Экзамен'),
        ('Д04', 'Философия', 'ИС', 18, 18, 0, 'Зачет'),
        ('Д05', 'Сети и телекоммуникации', 'СА', 36, 18, 36, 'Экзамен')
    ]
    with sqlite3.connect("plan.db") as conn:
        cursor = conn.cursor()
        cursor.executemany("""
            INSERT INTO Disciplines (
                discipline_code, name, specialty, lectures, practices, labs, assessment
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, initial_data)
        conn.commit()