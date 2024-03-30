from tkinter import *
from tkinter import ttk
import sqlite3

#imported everything for the window and labed window login page
root = Tk()
root.title("Login Page")

#connected to the database file
conn= sqlite3.connect('LoginInfo.db')
curse = conn.cursor()

#curse.execute("SELECT * FROM DatabaseInfo") # was using for bug cathcing
#print(curse.fetchall())

#class where the main progam is 
class LoginTime:

    def __init__(self, master):

        #lable for email
        self.labeEmail = ttk.Label(master)
        self.labeEmail.config(text= "Email: ")
        self.labeEmail.grid(row=0,column=0)

        #entry box for email
        self.EmailEntry = ttk.Entry(master)
        self.EmailEntry.grid(row=0,column=15)

        #lable for password
        self.labePass = ttk.Label(master)
        self.labePass.config(text="Password: ")
        self.labePass.grid(row=25,column=0)

        #entry box for password
        self.PassEntry = ttk.Entry(master)
        self.PassEntry.config(show = "*")
        self.PassEntry.grid(row=25,column=15)

        #Button to "login"
        self.LoginBut = ttk.Button(master)
        self.LoginBut.config(text="Login")
        self.LoginBut.config(command= self.checkLogin) # goes to function that checks login info
        self.LoginBut.grid(row=50, column= 5)

        #lable for if login success or failure
        self.checkLable1 = ttk.Label(master)
        self.checkLable1.grid(row=100, column=5)

    #function that checks user login info
    def checkLogin(self):
        emailss = self.EmailEntry.get()
        passwordss = self.PassEntry.get()
        #checks for email and password
        def Echecker(emailss):
            curse.execute("SELECT * FROM DatabaseInfo WHERE email=?", (emailss,))
            results = curse.fetchone()
            if results is not NONE and results[1] == passwordss:#Makes sure that the password matches the email and not just anypassword in the file
                return True
            else:
                return False


        #If both the email and password are correct then login succerful and then clear entry boxes    
        if Echecker(emailss) == TRUE:
            self.checkLable1.config(text= "Login Successful")
            self.checkLable1.config(foreground= 'green')
            self.EmailEntry.delete(0,'end')
            self.PassEntry.delete(0,'end')
        # If either email or password incorrect or not the write one then says incorrect       
        else:
            self.checkLable1.config(text="Email or Password Incorrect")
            self.checkLable1.config(foreground='red')


#accually runs the program
logger = LoginTime(root)


root.mainloop()