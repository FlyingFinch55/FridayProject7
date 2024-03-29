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

        self.LoginBut = ttk.Button(master)
        self.LoginBut.config(text="Login")
        self.LoginBut.config(command= self.checkLogin)
        self.LoginBut.grid(row=50, column= 5)

        self.checkLable1 = ttk.Label(master)
        self.checkLable1.grid(row=100, column=5)
        self.checkLable2 = ttk.Label(master)
        self.checkLable2.grid(row=150, column=5)

    def checkLogin(self):
        emailss = self.EmailEntry.get()
        passwordss = self.PassEntry.get()



logger = LoginTime(root)


root.mainloop()