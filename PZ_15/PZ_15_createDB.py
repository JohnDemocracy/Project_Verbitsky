import sqlite3
import sys
from PZ_15_insert import insert_data

database = 'plan.db'

with sqlite3.connect(database) as conn:
    cursor = conn.cursor()
    def initialize_database():
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Disciplines (
                    discipline_code TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    specialty TEXT NOT NULL,
                    lectures INTEGER NOT NULL,
                    practices INTEGER NOT NULL,
                    labs INTEGER NOT NULL,
                    assessment TEXT NOT NULL
                )
            """)
        except sqlite3.Error:
            pass
        insert_data()
    
    def print_records(records):
        if not records:
            return
        for row in records:
            print(f"{row[0]:<5} | {row[1]:<30} | {row[2]:<8} | {row[3]:<7} | {row[4]:<9} | {row[5]:<5} | {row[6]}")

    def search_records():
        print("1. Поиск по специальности\n2. Поиск по форме зачёта\n3. Поиск по лекциям (> чем)")
        choice = input("Выбор: ")
        try:
            if choice == '1':
                cursor.execute("SELECT * FROM Disciplines WHERE specialty = ?", (input("Специальность: "),))
            elif choice == '2':
                cursor.execute("SELECT * FROM Disciplines WHERE assessment = ?", (input("Форма зачёта: "),))
            elif choice == '3':
                cursor.execute("SELECT * FROM Disciplines WHERE lectures > ?", (int(input("Лекции >: ")),))
            else:
                return
            print_records(cursor.fetchall())
        except (sqlite3.Error, ValueError):
            pass

    def edit_records():
        print("1. Изменить форму зачёта по коду\n2. Изменить лекции по коду\n3. Изменить специальность по коду")
        choice = input("Выбор: ")
        if choice not in ('1', '2', '3'): 
            return
        code = input("Код: ")
        try:
            if choice == '1':
                cursor.execute("UPDATE Disciplines SET assessment = ? WHERE discipline_code = ?", (input("Новая форма зачёта: "), code))
            elif choice == '2':
                cursor.execute("UPDATE Disciplines SET lectures = ? WHERE discipline_code = ?", (int(input("Новые лекции: ")), code))
            elif choice == '3':
                cursor.execute("UPDATE Disciplines SET specialty = ? WHERE discipline_code = ?", (input("Новая специальность: "), code))
            conn.commit()
        except (sqlite3.Error, ValueError):
            pass

    def delete_records():
        print("1. Удалить по коду\n2. Удалить по специальности\n3. Удалить по форме зачёта")
        choice = input("Выбор: ")
        try:
            if choice == '1':
                cursor.execute("DELETE FROM Disciplines WHERE discipline_code = ?", (input("Код: "),))
            elif choice == '2':
                cursor.execute("DELETE FROM Disciplines WHERE specialty = ?", (input("Специальность: "),))
            elif choice == '3':
                cursor.execute("DELETE FROM Disciplines WHERE assessment = ?", (input("Форма: "),))
            else:
                return
            conn.commit()
        except sqlite3.Error:
            pass

    def view_all():
        try:
            cursor.execute("SELECT * FROM Disciplines")
            print_records(cursor.fetchall())
        except sqlite3.Error:
            pass

    def main():
        initialize_database()
        while True:
            print("\n1. Все записи\n2. Поиск\n3. Редактировать\n4. Удалить\n0. Выход")
            choice = input("Действие: ")
            if choice == '1': 
                view_all()
            elif choice == '2': 
                search_records()
            elif choice == '3': 
                edit_records()
            elif choice == '4': 
                delete_records()
            elif choice == '0': 
                break

main()