from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Sign Up Page")



conn= sqlite3.connect('LoginInfo.db')
curse = conn.cursor()


class SignUpTime:
    def __init__(self, master):
        self.labeEmail = ttk.Label(master)
        self.labeEmail.config(text= "Email: ")
        self.labeEmail.grid()

        self.EmailEntry = ttk.Entry(master)
        self.EmailEntry.grid()

        self.labePass = ttk.Label(master)
        self.labePass.config(text="Password: ")
        self.labePass.grid()

        self.PassEntry = ttk.Entry(master)
        self.PassEntry.grid()

        self.labeCheckPass = ttk.Label(master)
        self.labeCheckPass.config(text= "Password again: ")
        self.labeCheckPass.grid()

        self.PassTwoEntry = ttk.Entry(master)
        self.PassTwoEntry.grid()

        self.SubmitBut = ttk.Button(master)
        self.SubmitBut.config(text= "Submit")
        self.SubmitBut.grid()



curse.execute("""
              CREATE TABLE IF NOT EXISTS userInfo (
              email TEXT,
              password TEXT,
              """)

def addUser(email, password):

    curse.execute("""
                INSERT INTO userInfo(email, password) 
                VALUES (?,?,?,?)""", (email, password)
    )
    conn.commit()




#addUser()


root.mainloop()