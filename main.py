#!venv/bin/python

from tkinter import *
from tkinter import ttk
import re

def digit(val):
    formula.set(f'{formula.get()}{val}')

def calculate():
    formulaFormated = formula.get().replace(" ", "")

    if re.search('^[0-9\+\*\-\/\(\)\.]+$', formulaFormated):
        formula.set(eval(formulaFormated))
    else:
        formula.set('Operação invalida!')

def clear():
    formula.set("")

def delDigit():
    formula.set(formula.get()[0:-1])

buttons = [
    ['(', ')', 'C', '<'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '*'],
    ['.', '0', '=', '/']
]

app = Tk()
app.title('Calculadora')

mainframe = ttk.Frame(app, padding="5")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

styleInput = ttk.Style()
styleInput.configure('ReadOnly.TEntry', background='white')

formula = StringVar()
inputformula = ttk.Entry(mainframe, width=42, textvariable=formula, state='readonly', style='ReadOnly.TEntry')
inputformula.grid(column=1, row=1, columnspan=4, padx=2, pady=10)

for indexX, buttonCell in enumerate(buttons):
    for indexY, cell in enumerate(buttonCell):
        if cell == '':
            continue

        if cell == 'C':
            ttk.Button(mainframe, text=cell, command=clear).grid(column=indexY + 1, row=indexX + 2, padx=2, pady=2)
            continue

        if cell == '<':
            ttk.Button(mainframe, text=cell, command=delDigit).grid(column=indexY + 1, row=indexX + 2, padx=2, pady=2)
            continue

        if cell == '=':
            ttk.Button(mainframe, text=cell, command=calculate).grid(column=indexY + 1, row=indexX + 2, padx=2, pady=2)
            continue

        ttk.Button(mainframe, text=cell, command=lambda x=cell:digit(x)).grid(column=indexY + 1, row=indexX + 2, padx=2, pady=2)

app.mainloop()