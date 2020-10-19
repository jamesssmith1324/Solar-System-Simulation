import tkinter as tk
import sqlite3 as sql
import os
import pygame
import Main_Screen

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.mainFrame = tk.Frame(self.root, width = 500, height = 500)
        #self.root.config(width = self.root.winfo_screenwidth(), height = self.root.winfo_screenheight())
        self.mainFrame.grid(row = 0, column = 0)
        self.mainFrame.grid_propagate(False)
        self.frames = {}
        self.loginScreen()
        self.makeUserScreen()
        self.raiseLoginScreen()
        
##############
        
    def loginScreen(self):
        self.userLoginScreen = tk.Frame(self.mainFrame, width = 1400, height = 500)
        self.userLoginScreen.grid(row = 0, column = 0)
        self.userLoginScreen.grid_propagate(False)
        self.frames['loginScreen'] = self.userLoginScreen
        self.backButton = tk.Button(self.userLoginScreen, text = 'Make User', command = self.raiseMakeUserScreen)
        self.backButton.grid(row = 5, column = 3, pady = 20)

        self.Title = tk.Label(self.userLoginScreen, text = "Solar System Simulation", font = 40)
        self.Title.grid(row = 0, column = 3)

        self.Title1 = tk.Label(self.userLoginScreen, text = 'Enter Details')
        self.Title1.grid(row = 1, column = 3)
        
        self.usernameTitle = tk.Label(self.userLoginScreen, text = 'Username')
        self.usernameTitle.grid(row = 2, column = 2)
        self.username = tk.Entry(self.userLoginScreen)
        self.username.grid(row = 2, column = 3)

        self.passwordTitle = tk.Label(self.userLoginScreen, text = 'Password')
        self.passwordTitle.grid(row = 3, column = 2)
        self.password = tk.Entry(self.userLoginScreen, show = "*")
        self.password.grid(row = 3, column = 3)

        self.loginButton = tk.Button(self.userLoginScreen, text = 'Login', command = self.userInput)
        self.loginButton.grid(row = 4, column = 3)

        
    def raiseLoginScreen(self):
        self.frames['loginScreen'].tkraise()
        
###############
        
    def makeUserScreen(self):
        self.newUserScreen = tk.Frame(self.mainFrame, width = 1400, height = 500)
        self.newUserScreen.grid(row = 0, column = 0)
        self.newUserScreen.grid_propagate(False)
        self.frames['AddUserScreen'] = self.newUserScreen
        self.backButton = tk.Button(self.newUserScreen, text = 'Login', command = self.raiseLoginScreen)
        self.backButton.grid(row = 5, column = 1, pady = 20)

        self.Title = tk.Label(self.newUserScreen, text = "Solar System Simulation", font = 40)
        self.Title.grid(row = 0, column = 1)

        self.Title = tk.Label(self.newUserScreen, text = 'New User')
        self.Title.grid(row = 1, column = 1)

        self.newUsernameTitle = tk.Label(self.newUserScreen, text = 'New Username')
        self.newUsernameTitle.grid(row = 2, column = 0)
        self.newUsername = tk.Entry(self.newUserScreen)
        self.newUsername.grid(row = 2, column = 1)
        
        self.passwordTitle = tk.Label(self.newUserScreen, text = 'New Password')
        self.passwordTitle.grid(row = 3, column = 0)
        self.newPassword = tk.Entry(self.newUserScreen)
        self.newPassword.grid(row = 3, column = 1)

        self.createButton = tk.Button(self.newUserScreen, text = 'Create Account', command = self.takeNewUser)
        self.createButton.grid(row = 4, column = 1)
        
    def raiseMakeUserScreen(self):
        self.frames['AddUserScreen'].tkraise()

################
        
    def userInput(self):
        mydb = sql.connect('SimulationLogin.db')
        c = mydb.cursor()
        validUser = False
        validLogin = False
        userID = self.username.get()
        password = self.password.get()

        c.execute('''
        SELECT Username
        FROM DataStore''')

        data = c.fetchall()


        for i in data:
            if i[0][:] == userID:
                validUser = True
                user = i[0][:]
        if validUser:
            c.execute("SELECT Password FROM DataStore WHERE Username = '{0}'".format(user))
            userpass = c.fetchone()
            if password == userpass[0][:]:
                validLogin = True

        print(validUser)
        print(validLogin)
        if validUser == True and validLogin == True:
            self.mainScreen()


    def takeNewUser(self):
        mydb = sql.connect('SimulationLogin.db')
        c = mydb.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS DataStore (Username text, Password text)''')
        newUserID = self.newUsername.get()
        newPassword = self.newPassword.get()
        print(newUserID)
        c.execute('''
        INSERT INTO DataStore
        VALUES ('{0}','{1}')'''.format(newUserID, newPassword))
    
        mydb.commit()

        mydb.close()

###################

    def mainScreen(self):
        ID = self.username.get()
        Main_Screen.MAIN(ID)
        


    #def raiseMainScreen(self):
     #   self.frames["self.mainScreen"].tkraise()
        
        

