import tkinter as tk
from tkinter import *


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

pad = Tk()

ans_str = StringVar()

text_widget = tk.Text(pad, height = 1, width=13, font=("Helvetica", 40))
mode=Button(pad, text="(", height=1, width=1, padx=40, pady=20)

parenthesisopen = Button(pad, text="(", height=1, width=1, padx=40, pady=20, command=lambda: keypad("("))
parenthesisclose = Button(pad, text=")", height=1, width=1, padx=40, pady=20, command=lambda: keypad(")"))
x_Value = Button(pad, text="x", height=1, width=1, padx=40, pady=20, command=lambda: keypad("X"))
exponential = Button(pad, text="power()", height=1, width=1, padx=40, pady=20, command=button_add)
hist = Button(pad, text="HIST", height=1, width=1, padx=40, pady=20, command=button_add)
Number9 = Button(pad, text="9", height=1, width=1, padx=40, pady=20, command=lambda: keypad("9"))
Number8 = Button(pad, text="8", height=1, width=1, padx=40, pady=20, command=lambda: keypad("8"))
Number7 = Button(pad, text="7", height=1, width=1, padx=40, pady=20, command=lambda: keypad("7"))
Number6 = Button(pad, text="6", height=1, width=1, padx=40, pady=20, command=lambda: keypad("6"))
Number5 = Button(pad, text="5", height=1, width=1, padx=40, pady=20, command=lambda: keypad("5"))
Number4 = Button(pad, text="4", height=1, width=1, padx=40, pady=20, command=lambda: keypad("4"))
Number3 = Button(pad, text="3", height=1, width=1, padx=40, pady=20, command=lambda: keypad("3"))
Number2 = Button(pad, text="2", height=1, width=1, padx=40, pady=20, command=lambda: keypad("2"))
Number1 = Button(pad, text="1", height=1, width=1, padx=40, pady=20, command=lambda: keypad("1"))
Number0 = Button(pad, text="0", height=1, width=1, padx=40, pady=20, command=lambda: keypad("0"))
Del = Button(pad, text="DEL", height=1, width=1, padx=40, pady=20, command=delete)
Ac = Button(pad, text="AC", height=1, width=1, padx=40, pady=20, command=all_clear)
mutiply = Button(pad, text="x", height=1, width=1, padx=40, pady=20, command=lambda: keypad("*"))
plus = Button(pad, text="+", height=1, width=1, padx=40, pady=20, command=lambda: keypad("+"))
divide = Button(pad, text=":", height=1, width=1, padx=40, pady=20, command=lambda: keypad("/"))
minus = Button(pad, text="-", height=1, width=1, padx=40, pady=20, command=lambda: keypad("-"))
mutiply10 = Button(pad, text="x10", height=1, width=1, padx=40, pady=20, command=multiply_10)
node = Button(pad, text=".", height=1, width=1, padx=40, pady=20, command=lambda: keypad("."))
Ans = Button(pad, text="ANS", height=1, width=1, padx=40, pady=20, command=ans_copy)
equal = Button(pad, text="=", height=1, width=1, padx=40, pady=20, command=equals)

text_widget.grid(row=0, column=0, columnspan=4, sticky="w")
parenthesisopen.grid(row=3, column=0)
parenthesisclose.grid(row=3, column=1)
x_Value.grid(row=3, column=2)
exponential.grid(row=3, column=3)
hist.grid(row=3, column=4)
Number9.grid(row=4, column=2)
Number8.grid(row=4, column=1)
Number7.grid(row=4, column=0)
Number6.grid(row=5, column=2)
Number5.grid(row=5, column=1)
Number4.grid(row=5, column=0)
Number3.grid(row=6, column=2)
Number2.grid(row=6, column=1)
Number1.grid(row=6, column=0)
Number0.grid(row=7, column=0)
Del.grid(row=4, column=3)
Ac.grid(row=4, column=4)
mutiply.grid(row=5, column=3)
plus.grid(row=6, column=3)
divide.grid(row=5, column=4)
minus.grid(row=6, column=4)
mutiply10.grid(row=7, column=2)
node.grid(row=7, column=1)
Ans.grid(row=7, column=3)
equal.grid(row=7, column=4)

pad.mainloop()

# root.mainloop()
