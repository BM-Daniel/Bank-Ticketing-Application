from operator import iconcat
from tkinter import *
from tkinter.ttk import Combobox
import tkinter as tk
from tkinter import messagebox


def submit():
    pass

def clear():
    nameValue.set('')
    contactValue.set('')
    AgeValue.set('')
    addressEntry.delete(1.0,END)

WIN_HEIGHT = 360
WIN_WIDTH = 640
HEADING = "Welcome to DIGESJC Bank"
THEME_DARK = '#283A73'
THEME_LIGHT = '#eeeeee'
DEFAULT_FONT = 'montserrat'

root = Tk()
root.title("DIGESJC BANK TICKETING SYSTEM")
root.geometry(f'{WIN_WIDTH}x{WIN_HEIGHT}')
root.resizable(False,False)
root.configure(bg=THEME_LIGHT)


# heading
Label(root,text=HEADING,font=f'{DEFAULT_FONT} 18 bold',fg=THEME_DARK).place(x=165,y=20)

# buttons
Button(root, text="Submit", bg="#326273", fg="#fff", width=15, height=2).place(x=50,y=160)
Button(root, text="Clear", bg="#326273", fg="#fff", width=15, height=2,command=clear).place(x=260,y=160)
Button(root, text="Exit", bg="#326273", fg="#fff", width=15, height=2,command=lambda:root.destroy()).place(x=470,y=160)

root.mainloop()
