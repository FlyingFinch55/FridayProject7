from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Login Page")


conn= sqlite3.connect('LoginInfo.db')
curse = conn.cursor()

class LoginTime:

    def __init__(self, master):
        
        self.labeEmail = ttk.Label(master)
        self.labeEmail.config(text= "Email: ")
        self.labeEmail.grid(row=0,column=0)

        self.EmailEntry = ttk.Entry(master)
        self.EmailEntry.grid(row=0,column=15)

        self.labePass = ttk.Label(master)
        self.labePass.config(text="Password: ")
        self.labePass.grid(row=25,column=0)

        self.PassEntry = ttk.Entry(master)
        self.PassEntry.grid(row=25,column=15)






root.mainloop()