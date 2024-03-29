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
        self.labeCheckPass.config(text= "Password re-entry: ")
        self.labeCheckPass.grid(row=50,column=0)

        self.PassTwoEntry = ttk.Entry(master)
        self.PassTwoEntry.grid(row=50,column=15)

        self.SubmitBut = ttk.Button(master)
        self.SubmitBut.config(text= "Submit")
        self.SubmitBut.config(command=self.saveInfo)
        self.SubmitBut.grid(row=100,column=5)

        self.checkLable1 = ttk.Label(master)
        self.checkLable1.grid(row=150, column=5)
        self.checkLable2 = ttk.Label(master)
        self.checkLable2.grid(row=200, column=5)

    def saveInfo(self):
        emails = self.EmailEntry.get()
        passwords = self.PassEntry.get()
        passwordTwo = self.PassTwoEntry.get()
        if "@" not in emails:
            self.checkLable1.config(text="Invaild email")
            return
        if "." not in emails:
            self.checkLable1.config(text="Invaild email")
            return
        if "@" and "." in emails:
            self.checkLable1.config(text=" ")

        if passwords != passwordTwo:
            self.checkLable2.config(text="Passwords do not match")
            return

        def checker(emails):
            curse.execute("SELECT email FROM userInfo WHERE email=?", (emails,))
        if checker(emails):
            self.checkLable1.config(text="Email already in database")
        else:
            addUser(emails,passwords)
            self.checkLable1.config(text="")
            self.checkLable2.config(text="")

        self.EmailEntry.delete(0,'end')
        self.PassEntry.delete(0,'end')
        self.PassTwoEntry.delete(0,'end')
        




        

        



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




root.mainloop()