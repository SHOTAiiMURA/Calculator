# import pprint
# import tkinter as tk
# import tkinter.ttk as ttk
#
# def theme_changed(theme):
#     style.theme_use(theme)
#
#     print(theme)
#     pprint.pprint(style.layout('TButton'))
#     pprint.pprint(style.element_options('Button.border'))
#
#     style.configure(
#         'Custom.TButton',
#         background='#FFFFFF', # White
#         bordercolor='#00FF00', # Green
#         lightcolor='#FF0000', # Red
#         darkcolor='#0000FF', # Blue
#         borderwidth=4,
#         foreground='#00FFFF', # Cyan
#     )
#
# root = tk.Tk()
# style = ttk.Style()
#
# combo = ttk.Combobox(root, values=sorted(style.theme_names()), state='readonly')
# combo.set(style.theme_use())
# combo.bind('<<ComboboxSelected>>', lambda _e: theme_changed(combo.get()))
# combo.pack()
#
# theme_changed(style.theme_use())
#
# button = ttk.Button(root, text="Normal Button")
# button.pack()
#
# button = ttk.Button(root, style="Custom.TButton", text="Custom Button")
# button.pack()
#
# root.mainloop()

import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.geometry('350x250')
# Label
ttk.Label(window, text="Select the Month :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=15, padx=10, pady=25)

n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width=27,
                            textvariable=n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column=1, row=15)

# Shows february as a default value
monthchoosen.current(2)
window.mainloop()
