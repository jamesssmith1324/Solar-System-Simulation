import tkinter as tk
from PIL import ImageTk, Image
import Inner_Planets
import Outer_Planets
import Login_Screen
import Create_SolarSystem
import LoadedSS

class MAIN():
    def __init__(self,ID):
        self.root = tk.Toplevel()
        self.mainFrame = tk.Frame(self.root, width = 600, height = 300)
        self.mainFrame.grid(row = 0, column = 0)
        self.mainFrame.grid_propagate(True)
        self.frames = {}
        self.homeFrame(ID)
        

    def homeFrame(self,ID):
        self.homeScreen = tk.Frame(self.mainFrame, width = 600, height = 300)
        #self.homeScreen.grid(row = 0, column = 0)
        self.homeScreen.grid_propagate(True)
        self.titleL = tk.Label(self.mainFrame, text = "Solar System Simulation", font = 30, padx = 20)
        self.titleL.grid(row = 0, column = 1)
        self.logOutB = tk.Button(self.mainFrame, text = "Log Out", padx = 10, pady = 10, command = self.loginPage)
        self.logOutB.grid(row = 0, column = 0, padx = 20, pady = 10)
        ####
        self.pvar1 = tk.IntVar()
        self.box1 = tk.Checkbutton(self.mainFrame, text = "Mercury", variable = self.pvar1)
        self.box1.grid(row = 2, column = 0)
        self.pvar2 = tk.IntVar()
        self.box2 = tk.Checkbutton(self.mainFrame, text = "Venus", variable = self.pvar2)
        self.box2.grid(row = 3, column = 0)
        self.pvar3 = tk.IntVar()
        self.box3 = tk.Checkbutton(self.mainFrame, text = "Earth", variable = self.pvar3)
        self.box3.grid(row = 4, column = 0)
        self.pvar4 = tk.IntVar()
        self.box4 = tk.Checkbutton(self.mainFrame, text = "Mars", variable = self.pvar4)
        self.box4.grid(row = 5, column = 0)
        ####
        
        self.pvar5 = tk.IntVar()
        self.box5 = tk.Checkbutton(self.mainFrame, text = "Jupiter", variable = self.pvar5)
        self.box5.grid(row = 2, column = 1)
        self.pvar6 = tk.IntVar()
        self.box6 = tk.Checkbutton(self.mainFrame, text = "Saturn", variable = self.pvar6)
        self.box6.grid(row = 3, column = 1)
        self.pvar7 = tk.IntVar()
        self.box7 = tk.Checkbutton(self.mainFrame, text = "Uranus", variable = self.pvar7)
        self.box7.grid(row = 4, column = 1)
        self.pvar8 = tk.IntVar()
        self.box8 = tk.Checkbutton(self.mainFrame, text = "Neptune", variable = self.pvar8)
        self.box8.grid(row = 5, column = 1)

        ####
        self.innnerSSB = tk.Button(self.mainFrame, text = "Inner Solar System", padx = 10, pady = 10, command = self.innerPlanetsPage)
        self.innnerSSB.grid(row = 1, column = 0, padx = 20, pady = 10)
        self.outerSSB = tk.Button(self.mainFrame, text = "Outer Solar System", padx = 10, pady = 10, command = self.outerPlanetsPage)
        self.outerSSB.grid(row = 1, column = 1, padx = 20, pady = 10)
        self.quizPageB = tk.Button(self.mainFrame, text = "Quiz Page", padx = 10, pady = 10)
        self.quizPageB.grid(row = 1, column = 2, padx = 20, pady = 10)
        self.createSSB = tk.Button(self.mainFrame, text = "Create Solar System", padx = 10, pady = 10, command = self.createSS)
        self.createSSB.grid(row = 6, column = 0, padx = 20, pady = 10)
        self.loadSSB = tk.Button(self.mainFrame, text = "Load Solar System", padx = 10, pady = 10, command = self.loadSS)
        self.loadSSB.grid(row = 6, column = 1, padx = 20, pady = 10)
        #self.descriptionL = tk.Label(self.mainFrame, text = """######                    Description Here                    #####""")
        #self.descriptionL.grid(row = 8, column = 1)
        self.userDetailsL = tk.Label(self.mainFrame, text = ("User ID: {0}".format(ID)))
        self.userDetailsL.grid(row = 0 , column = 2)

    def raiseMainFrame(self):
        self.frames["self.homeFrame"].tkraise()

    def innerPlanetsPage(self):
        val1 = self.pvar1.get()
        val2 = self.pvar2.get()
        val3 = self.pvar3.get()
        val4 = self.pvar4.get()
        Inner_Planets.Run(val1,val2,val3,val4)
        
    def outerPlanetsPage(self):
        val5 = self.pvar5.get()
        val6 = self.pvar6.get()
        val7 = self.pvar7.get()
        val8 = self.pvar8.get()        
        Outer_Planets.Run(val5,val6,val7,val8)
        
    def loginPage(self):
        self.root.destroy()
        Login_Screen.GUI()

    def createSS(self):
        Create_SolarSystem.CreateSS()

    def loadSS(self):
        LoadedSS.Run()
        
        


        









