from tkinter import *
from tkinter import ttk

text="Boo!!"
button="eek!!"

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text=text).grid(column=0, row=0)
ttk.Button(frm, text=button, command=root.destroy).grid(column=1, row=0)
root.mainloop()