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



win = Tk()

win.geometry('600x700')
#win.configure(bg='#334353')

gui_style = ttk.Style()
#gui_style.configure("TButton", foreground='#334353')
gui_style.configure('TButton', background='green')


frame = ttk.Frame(win, style='TFrame')

win.title("Sea of Stats App")


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



Q1list = [
        ("I can do all these tasks very quickly and efficiently without any help", 1),
        ("I can do these tasks relatively easily without help", 2),
        ("I can do these tasks only very slowly without help", 3),
        ("I cannot do most of these tasks unless I have help", 4),
        ("I can do none of these tasks by myself.", 5),
    ]
Label(win, text="Q1. How much help do you need with jobs around your place of residence (eg preparing food, cleaning, gardening)?", justify = LEFT, wraplength=500 ).grid(row=3, columnspan=2)
q1 = IntVar()
for text, value in Q1list:
    b = Radiobutton(win, text=text, variable=q1, value=value)
    b.grid(sticky='W', rowspan=5, columnspan=2)


Q2list = [
        ("getting around is enjoyable and easy", 1),
        ("I have no difficulty getting around outside my place of residence", 2),
        ("I have a little difficulty", 3),
        ("I have moderate difficulty", 4),
        ("I have a lot of difficulty", 5),
        ("I cannot get around unless somebody is there to help me.", 6)
    ]
Label(win, text="Q2. How easy or difficult is it for you to get around by yourself outside your place of residence (eg to go shopping, visiting)?", justify = LEFT, wraplength=500 ).grid(rowspan=2, columnspan=2)
q2 = IntVar()
for text, value in Q2list:
    b = Radiobutton(win, text=text, variable=q2, value=value)
    b.grid(sticky='W', rowspan=6, columnspan=2)




def print_button():
    s = AqolScore(dvQ1, dvQ2)
    s.printscore()

btn2 = Button(win, text="Print Value", command=print_button).grid(row=99, column=1)

def clicked():
    dir_name = filedialog.asksaveasfilename(initialdir="~/Downloads/", title="Select file", filetypes=(("pdf files", "*.pdf"),))
    generate_pdf(dir_name, q1)


btn = Button(win, text="Generate Report", command=clicked)
btn.grid(row=100, column=1)

win.mainloop()
