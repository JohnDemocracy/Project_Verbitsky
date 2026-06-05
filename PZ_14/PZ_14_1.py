# В соответствии с номером варианта перейти по ссылке на прототип. Реализовать
# его в IDE PyCharm Community с применением пакета tk. Получить интерфейс максимально
# приближенный к оригиналу
# Вариант 8 https://i.pinimg.com/originals/73/c6/0d/73c60def8c55043f9fd27b370530a9cf.jpg

import tkinter as tk
from tkinter import ttk
from datetime import datetime

BG_MAIN = "#2E3140"
BG_BAR = "#CA953E"
FG_LABEL = "#E7D457"
BTN_SUBMIT = "#75B97F"
BTN_CANCEL = "#CD605A"

def add_placeholder(entry, placeholder_text):
    entry.insert(0, placeholder_text)
    entry['fg'] = 'grey'

    def input_focus(event):
        if entry['fg'] == 'grey':
            entry.delete(0, 'end')
            entry['fg'] = 'black'

    def output_focus(event):
        if not entry.get():
            entry.insert(0, placeholder_text)
            entry['fg'] = 'grey'

    entry.bind("<FocusIn>", input_focus)
    entry.bind("<FocusOut>", output_focus)

root = tk.Tk()
root.title("Sign Up")
root.geometry("500x620")
root.configure(bg=BG_MAIN)
root.resizable(False, False)

header_frame = tk.Frame(root, bg=BG_BAR, height=40)
header_frame.pack(fill=tk.X)
header_frame.pack_propagate(False)

tk.Label(header_frame, text="Sign Up", bg=BG_BAR, fg="#F5E8A6", font=("Arial", 12)).pack(side=tk.LEFT, padx=15)

body_frame = tk.Frame(root, bg=BG_MAIN)
body_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

def create_label(text, row):
    lbl = tk.Label(body_frame, text=text, bg=BG_MAIN, fg=FG_LABEL, font=("Arial", 10))
    lbl.grid(row=row, column=0, sticky="e", padx=(10, 15), pady=10)

create_label("First Name", 0)
e_first_name = tk.Entry(body_frame, width=45, font=("Arial", 10))
add_placeholder(e_first_name, "Enter First Name...")
e_first_name.grid(row=0, column=1, sticky="w", pady=10)

create_label("Last Name", 1)
e_last_name = tk.Entry(body_frame, width=45, font=("Arial", 10))
add_placeholder(e_last_name, "Enter Last Name...")
e_last_name.grid(row=1, column=1, sticky="w", pady=10)

create_label("Screen Name", 2)
e_screen_name = tk.Entry(body_frame, width=45, font=("Arial", 10))
add_placeholder(e_screen_name, "Enter Screen Name...")
e_screen_name.grid(row=2, column=1, sticky="w", pady=10)

create_label("Date of Birth", 3)
dob_frame = tk.Frame(body_frame, bg=BG_MAIN)
dob_frame.grid(row=3, column=1, sticky="w", pady=10)

month_cb = ttk.Combobox(dob_frame, values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ], width=10, state="readonly")
month_cb.set("May")
month_cb.pack(side=tk.LEFT, padx=(0, 15))

day_cb = ttk.Combobox(dob_frame, values=[i for i in range(1, 31)], width=5, state="readonly")
day_cb.set("5")
day_cb.pack(side=tk.LEFT, padx=(0, 15))

year_cb = ttk.Combobox(dob_frame, values=[i for i in range(1900, datetime.now().year + 1)], width=8, state="readonly")
year_cb.set("1985")
year_cb.pack(side=tk.LEFT)

create_label("Gender", 4)
gender_frame = tk.Frame(body_frame, bg=BG_MAIN)
gender_frame.grid(row=4, column=1, sticky="w", pady=10)

gender_var = tk.StringVar(value="Male")
rb_male = tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg=BG_MAIN, fg=FG_LABEL, selectcolor=BG_MAIN, activebackground=BG_MAIN, activeforeground=FG_LABEL)
rb_male.pack(side=tk.LEFT, padx=(0, 10))

rb_female = tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg=BG_MAIN, fg=FG_LABEL, selectcolor=BG_MAIN, activebackground=BG_MAIN, activeforeground=FG_LABEL)
rb_female.pack(side=tk.LEFT)

create_label("Country", 5)
country_cb = ttk.Combobox(body_frame, values=["USA", "Canada", "UK"], width=43, state="readonly")
country_cb.set("USA")
country_cb.grid(row=5, column=1, sticky="w", pady=10)

create_label("E-mail", 6)
e_email = tk.Entry(body_frame, width=45, font=("Arial", 10))
add_placeholder(e_email, "Enter E-mail......")
e_email.grid(row=6, column=1, sticky="w", pady=10)

create_label("Phone", 7)
e_phone = tk.Entry(body_frame, width=45, font=("Arial", 10))
add_placeholder(e_phone, "Enter Phone......")
e_phone.grid(row=7, column=1, sticky="w", pady=10)

create_label("Password", 8)
e_pass = tk.Entry(body_frame, show="*", width=45, font=("Arial", 10))
e_pass.grid(row=8, column=1, sticky="w", pady=10)

create_label("Confirm Password", 9)
e_confirm_pass = tk.Entry(body_frame, show="*", width=45, font=("Arial", 10))
e_confirm_pass.grid(row=9, column=1, sticky="w", pady=10)

terms_var = tk.BooleanVar()
cb_terms = tk.Checkbutton(body_frame, text="I agree to the Terms of Use", variable=terms_var, bg=BG_MAIN, fg=FG_LABEL, selectcolor=BG_MAIN, activebackground=BG_MAIN, activeforeground=FG_LABEL)
cb_terms.grid(row=10, column=1, sticky="w", pady=(15, 0))

footer_frame = tk.Frame(root, bg=BG_BAR, height=50)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)
footer_frame.pack_propagate(False)

btn_frame = tk.Frame(footer_frame, bg=BG_BAR)
btn_frame.pack(side=tk.RIGHT, padx=15, pady=10)

btn_submit = tk.Button(btn_frame, text="submit", bg=BTN_SUBMIT, fg="white", font=("Arial", 10), relief=tk.FLAT, width=8)
btn_submit.pack(side=tk.LEFT, padx=5)

btn_cancel = tk.Button(btn_frame, text="Cancel", bg=BTN_CANCEL, fg="white", font=("Arial", 10), relief=tk.FLAT, width=8, command=root.destroy)
btn_cancel.pack(side=tk.LEFT, padx=5)

root.mainloop()