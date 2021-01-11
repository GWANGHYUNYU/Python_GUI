# ┌─────┬─────┬─────┬─────┐
# │ 0,0 │ 0,1 │ 0,2 │ 0,3 │
# ├─────┼─────┼─────┼─────┤
# │ 1,0 │ 1,1 │ 1,2 │ 1,3 │
# ├─────┼─────┼─────┼─────┤
# │ 2,0 │ 2,1 │ 2,2 │ 2,3 │
# └─────┴─────┴─────┴─────┘

# Pycharm은 ctrl+shift+r
# VisualCode는 ctrl+f

import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import *
import time

root = Tk()
root.title("Gwanghyun GUI")
root.geometry("640x480")  # 가로 * 세로

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# btn1.pack(side="left")
# btn2.pack(side="left")
# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

btn_f16.grid(row=0, column=0, padx=3, pady=3, sticky=N+E+W+S)
btn_f17.grid(row=0, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_f18.grid(row=0, column=2, padx=3, pady=3, sticky=N+E+W+S)
btn_f19.grid(row=0, column=3, padx=3, pady=3, sticky=N+E+W+S)

btn_claer = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_claer.grid(row=1, column=0, padx=3, pady=3, sticky=N+E+W+S)
btn_equal.grid(row=1, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_div.grid(row=1, column=2, padx=3, pady=3, sticky=N+E+W+S)
btn_mul.grid(row=1, column=3, padx=3, pady=3, sticky=N+E+W+S)

btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, padx=3, pady=3, sticky=N+E+W+S)
btn_8.grid(row=2, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_9.grid(row=2, column=2, padx=3, pady=3, sticky=N+E+W+S)
btn_sub.grid(row=2, column=3, padx=3, pady=3, sticky=N+E+W+S)

btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_sum = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, padx=3, pady=3, sticky=N+E+W+S)
btn_5.grid(row=3, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_6.grid(row=3, column=2, padx=3, pady=3, sticky=N+E+W+S)
btn_sum.grid(row=3, column=3, padx=3, pady=3, sticky=N+E+W+S)

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_dot = Button(root, text=".", width=5, height=2)

btn_1.grid(row=4, column=0, padx=3, pady=3, sticky=N+E+W+S)
btn_2.grid(row=4, column=1, padx=3, pady=3, sticky=N+E+W+S)
btn_3.grid(row=4, column=2, padx=3, pady=3, sticky=N+E+W+S)
btn_dot.grid(row=5, column=2, padx=3, pady=3, sticky=N+E+W+S)

btn_0 = Button(root, text="0", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, padx=3, pady=3, sticky=N+E+W+S)
btn_enter.grid(row=4, column=3, rowspan=2, padx=3, pady=3, sticky=N+E+W+S)

root.mainloop()
