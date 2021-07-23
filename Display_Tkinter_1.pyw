import tkinter as tk
from tkinter import *
from tkinter import ttk


def button_add():
    print("fuck")


def equals():
    equ = text_widget.get('1.0', 'end -1c')
    result = eval(equ)
    all_clear()
    text_widget.insert('insert', result)
    ans_str.set(result)
    print(text_widget.get('1.0', 'end -1c'))


def keypad(key):
    text_widget.insert('insert', key)

    print(text_widget.get('1.0', 'end -1c'))


def print_text():
    print()


def all_clear():
    text_widget.delete('1.0', 'end')


def delete():
    text_widget.delete('insert -1c', 'insert')
    print(text_widget.get('1.0', 'end -1c'))


def ans_copy():
    text_widget.delete('1.0', 'end')
    text_widget.insert('insert', ans_str.get())


def multiply_10():
    text_widget.insert('insert', 0)


rows = 5
columns = 5
keypad_shift_ver = 1
keypad_shift_hor = 0

key_matrix = [["(", ")", "x", "power()", "HIST"],
              ["7", "8", "9", "DEL", "AC"],
              ["4", "5", "6", "x", "/"],
              ["1", "2", "3", "+", "-"],
              ["0", ".", "x10", "ANS", "="]]

key_commands = [[lambda: keypad("("), lambda: keypad(")"), lambda: keypad("X"), button_add, button_add],
                [lambda: keypad("7"), lambda: keypad("8"), lambda: keypad("9"), delete, all_clear],
                [lambda: keypad("4"), lambda: keypad("5"), lambda: keypad("6"), lambda: keypad("*"),
                 lambda: keypad("/")],
                [lambda: keypad("1"), lambda: keypad("2"), lambda: keypad("3"), lambda: keypad("+"),
                 lambda: keypad("-")],
                [lambda: keypad("0"), lambda: keypad("."), multiply_10, ans_copy, equals]]

key_colors = [["#f8f7f3", "#f8f7f3", "#f8f7f3", "#f8f7f3", "#f8f7f3"],
              ["#fcfcfc", "#fcfcfc", "#fcfcfc", "#f8f7f3", "#f8f7f3"],
              ["#fcfcfc", "#fcfcfc", "#fcfcfc", "#f8f7f3", "#f8f7f3"],
              ["#fcfcfc", "#fcfcfc", "#fcfcfc", "#f8f7f3", "#f8f7f3"],
              ["#fcfcfc", "#fcfcfc", "#fcfcfc", "#f8f7f3", "#f8f7f3"]]

modes = ["Complete", "Equation", "Table", "Integ", "Differe"]

pad = Tk()

pad.config(bg="#eff1f1")
# d4f7f5 (high)
# d9d9d9 (85)
# ebebeb (92)
# f5f5f5 (96)
# fcfcfc (99)

ans_str = StringVar()

text_widget = tk.Text(pad, height=2, width=35, font=("Helvetica", 22))
text_widget.grid(row=0, column=0, columnspan=4)
mode_button = ttk.Combobox(pad, justify="left", values=modes, width=15, state="readonly")
mode_button.current(0)
mode_button.grid(row=0, column=4)

button_style = ttk.Style()
button_style.theme_use("default")
button_style.configure('MyWidget.TButton',
                       background='#f5f5f5',
                       foreground='black',
                       highlightthickness='2',
                       bordercolor='#00FF00',
                       borderwidth=0,
                       focuscolor=button_style.configure(".")["background"],
                       font=('Helvetica', 22))
#tkinter style, map
button_style.map('MyWidget.TButton',
                 foreground=[('pressed', 'red')],
                 background=[('pressed', '#d9d9d9'),
                             ('active', '#d9d9d9')],
                 highlightcolor=[('focus', 'green'),
                                 ('!focus', 'red')],
                 relief=[('pressed', 'sunken'),
                         ('!pressed', 'flat')])

cells = [] #2d
for i in range(rows):
    row = []
    for j in range(columns):
        # button_style.configure('MyWidget.TButton', background=key_colors[i][j])
        cell = ttk.Button(pad, text=key_matrix[i][j], width=20, padding=(-100, 20, -100, 20), style="MyWidget.TButton",
                          command=key_commands[i][j])
        cell.grid(row=i + keypad_shift_ver, column=j + keypad_shift_hor, ipadx=2, ipady=2, padx=3, pady=3)
        row.append(cell)
    cells.append(row)

pad.mainloop()

# root.mainloop()
