from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()



conn= sqlite3.connect('LoginInfo.db')
curse = conn.cursor()


class SignUpTime:
    def __init__(self, master):
        self.labe1 = ttk.Label(master)


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