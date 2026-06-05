# Разработать программу с применением пакета tk, взяв в качестве условия одну
# любую задачу из ПЗ №№ 1 – 9.
# ПЗ 2

# Вариант 9:
# Даны целые положительные числа A и B (A > B). На отрезке длины A
# размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию деления нацело, найти количество отрезков B, размещенных на
# отрезке A

import tkinter as tk
from tkinter import ttk

def calculate():
    firstnum = int(firstnum_entry.get())
    secondnum = int(secondnum_entry.get())

    if firstnum >= secondnum:
        result = firstnum // secondnum
        result_lbl.config(text=result)
    else:
        result = 0

root = tk.Tk()
root.title("Mathstuffs")
root.geometry("500x500")
root.resizable(False, False)

firstnum_lbl = tk.Label(root, text="Первое число", width=45, font=("Arial", 10))
firstnum_lbl.pack(pady=(15, 5))

firstnum_entry = tk.Entry(root, width=20, font=("Arial", 10))
firstnum_entry.pack()

secondnum_lbl = tk.Label(root, text="Второе число", width=45, font=("Arial", 10))
secondnum_lbl.pack(pady=(15, 5))

secondnum_entry = tk.Entry(root, width=20, font=("Arial", 10))
secondnum_entry.pack()

btn_calc = tk.Button(root, text="Рассчитать", command=calculate, font=("Arial", 10, "bold"), width=15)
btn_calc.pack(pady=20)

result_lbl = tk.Label(root, text="", width=45, font=("Arial", 10))
result_lbl.pack(pady=(20))

root.mainloop()