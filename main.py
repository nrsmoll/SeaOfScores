from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os
import pandas as pd
import numpy as np
import csv
from pdf_gen import generate_pdf
from scoring import AqolScore
from questions import *



win = Tk()

win.geometry('600x700')
#win.configure(bg='#334353')

gui_style = ttk.Style()
#gui_style.configure("TButton", foreground='#334353')
gui_style.configure('TButton', background='green')


frame = ttk.Frame(win, style='TFrame')

win.title("Sea of Stats App")
myscrollbar.pack(side="right", fill="y")

Label(win, text="First Name").grid(sticky="E", row=0)
Label(win, text="Last Name").grid(sticky="E", row=1)
Label(win, text="DOB").grid(sticky="E", row=2)

e1 = Entry(win)
e2 = Entry(win)
e3 = Entry(win)
e3.insert(0, "DD/MM/YYYY")

e1.grid(sticky="W", row=0, column=1)
e2.grid(sticky="W", row=1, column=1)
e3.grid(sticky="W", row=2, column=1)


import questions




def print_button():
    s = AqolScore()
    print(s.dvQ1)

btn2 = Button(win, text="Print Value", command=print_button).grid(row=99, column=1)

def clicked():
    dir_name = filedialog.asksaveasfilename(initialdir="~/Downloads/", title="Select file", filetypes=(("pdf files", "*.pdf"),))
    generate_pdf(dir_name, q1)


btn = Button(win, text="Generate Report", command=clicked)
btn.grid(row=100, column=1)

win.mainloop()
