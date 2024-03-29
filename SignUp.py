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
        self.labeEmail.grid(row=0,column=0)

        self.EmailEntry = ttk.Entry(master)
        self.EmailEntry.grid(row=0,column=15)

        self.labePass = ttk.Label(master)
        self.labePass.config(text="Password: ")
        self.labePass.grid(row=25,column=0)

        self.PassEntry = ttk.Entry(master)
        self.PassEntry.grid(row=25,column=15)

        self.labeCheckPass = ttk.Label(master)
        self.labeCheckPass.config(text= "Password again: ")
        self.labeCheckPass.grid(row=50,column=0)

        self.PassTwoEntry = ttk.Entry(master)
        self.PassTwoEntry.grid(row=50,column=15)

        self.SubmitBut = ttk.Button(master)
        self.SubmitBut.config(text= "Submit")
        self.SubmitBut.grid(row=100,column=5)





curse.execute("""
              CREATE TABLE IF NOT EXISTS DatabaseInfo (
              email INTEGER,
              password TEXT )
              """)

def addUser(email, password):

    curse.execute("""
                INSERT INTO userInfo(email, password) 
                VALUES (?,?,?,?)""", (email, password)
    )
    conn.commit()


Welcom = SignUpTime(root)

#addUser()


root.mainloop()