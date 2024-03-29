from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()



conn= sqlite3.connect('LoginInfo.db')
curse = conn.cursor()



root.mainloop()