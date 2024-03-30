from tkinter import *
from tkinter import ttk
import sqlite3

#adds everything needed for windows and labed the window
root = Tk()
root.title("Sign Up Page")


#connects to the database file
conn= sqlite3.connect('LoginInfo.db')
curse = conn.cursor()

#the class that runs everything
class SignUpTime:
    def __init__(self, master):
        #lable for email
        self.labeEmail = ttk.Label(master)
        self.labeEmail.config(text= "Email: ")
        self.labeEmail.grid(row=0,column=0)

        #email entry box
        self.EmailEntry = ttk.Entry(master)
        self.EmailEntry.grid(row=0,column=15)

        #lable for putting in the password the first time
        self.labePass = ttk.Label(master)
        self.labePass.config(text="Password: ")
        self.labePass.grid(row=25,column=0)

        #entry box for the first time password
        self.PassEntry = ttk.Entry(master)
        self.PassEntry.grid(row=25,column=15)

        #label for putting in the password the second time
        self.labeCheckPass = ttk.Label(master)
        self.labeCheckPass.config(text= "Password re-entry: ")
        self.labeCheckPass.grid(row=50,column=0)

        #entry box for the second time password
        self.PassTwoEntry = ttk.Entry(master)
        self.PassTwoEntry.grid(row=50,column=15)

        #button for submitting users inputs
        self.SubmitBut = ttk.Button(master)
        self.SubmitBut.config(text= "Submit")
        self.SubmitBut.config(command=self.saveInfo) # Go to check if can add user
        self.SubmitBut.grid(row=100,column=5)

        #labe for is the password is good
        self.checkLable1 = ttk.Label(master)
        self.checkLable1.grid(row=150, column=5)
        #Lable for if the passwords match
        self.checkLable2 = ttk.Label(master)
        self.checkLable2.grid(row=200, column=5)

    #The functions where we check the user info and maybe add it
    def saveInfo(self):
        emails = self.EmailEntry.get()
        passwords = self.PassEntry.get()
        passwordTwo = self.PassTwoEntry.get()
        #these 3 if statemesnt check for if the email is valid
        if "@" not in emails:
            self.checkLable1.config(text="Invaild email")
            return
        if "." not in emails:
            self.checkLable1.config(text="Invaild email")
            return
        if "@" and "." in emails: #Clears
            self.checkLable1.config(text=" ")

        #these 2 if statmants check to see if the passwords match
        if passwords != passwordTwo:
            self.checkLable2.config(text="Passwords do not match")
            return
        if passwords == passwordTwo:
            self.checkLable2.config(text="")
        
        #This is the funaction that shows if the email is already in the database
        def checker(emails):
            curse.execute("SELECT * FROM DatabaseInfo WHERE email=?", (emails,))
            if curse.fetchall():
                return True
            else:
                return False
        
        #If the email is in use prints that cant use that email
        if checker(emails) == TRUE:
            self.checkLable1.config(text="Email already in database")
        
        #otherwise adds the user to the database and clears everything for sign up page
        else:
            addUser(emails,passwords)
            self.checkLable1.config(text="")
            self.checkLable2.config(text="")
            self.EmailEntry.delete(0,'end')
            self.PassEntry.delete(0,'end')
            self.PassTwoEntry.delete(0,'end')
        

#mades the database and table if not already there
curse.execute("""
              CREATE TABLE IF NOT EXISTS DatabaseInfo (
              email TEXT,
              password TEXT )
              """)


#function to add a user to the database
def addUser(email, password):

    curse.execute("""
                INSERT INTO DatabaseInfo(email, password) 
                VALUES (?,?)""", (email,password)

    )
    conn.commit()
    #print("User added :)") had for bug checks


#accually runs the program
Welcom = SignUpTime(root)





root.mainloop()