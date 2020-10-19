import pygame
import math
import tkinter as tk
import sqlite3 as sql
class CreateSS:
   def __init__(self):
      self.root = tk.Tk()
      self.planetFrame = tk.Frame(self.root, width = 500, height = 500)
      self.planetFrame.grid(row = 0, column = 0)
      self.planetFrame.grid_propagate(False)
      self.dataList = []
      self.frames = {}
      self.PlanetList()
      self.PlanetStats()
      self.FileName()
      self.COUNT = 1


   def FileName(self):
      self.fileNameFrame = tk.Frame(self.planetFrame, width = 500, height = 500)
      self.fileNameFrame.grid(row = 0, column = 0)
      self.fileNameFrame.grid_propagate(False)
      self.frames["FileName"] = self.fileNameFrame
      self.fileNameL = tk.Label(self.fileNameFrame, text = "File Name : ")
      self.fileNameL.grid(row = 0, column = 0)
      self.fileNameE = tk.Entry(self.fileNameFrame)
      self.fileNameE.grid(row = 0, column = 1)
      self.fileNameB = tk.Button(self.fileNameFrame, text = "Make File",command = self.raisePlanetList)
      self.fileNameB.grid(row = 1, column = 0)
      self.fileNameGet = self.fileNameE.get()
      

   def PlanetList(self):
      self.planetList = tk.Frame(self.planetFrame, width = 500, height = 500)
      self.planetList.grid(row = 0, column = 0)
      self.planetList.grid_propagate(False)
      self.frames["PlanetList"] = self.planetList
      self.addPlanetB = tk.Button(self.planetList, text = "Add Planet", command = self.raisePlanetStats)
      self.addPlanetB.grid(row = 0, column = 0)
      self.saveAllB = tk.Button(self.planetList, text = "Save", command = self.listSaveFunction)
      self.saveAllB.grid(row = 0, column = 1)
      


   
   def PlanetStats(self):
      self.planetStats = tk.Frame(self.planetFrame, width = 500, height = 500)
      self.planetStats.grid(row = 0, column = 0)
      self.planetStats.grid_propagate(False)
      self.frames["PlanetStats"] = self.planetStats
      self.velocityXL = tk.Label(self.planetStats, text = "Velocity X : ")
      self.velocityXL.grid(row = 1, column = 0)
      self.velocityXE = tk.Entry(self.planetStats)
      self.velocityXE.grid(row = 1, column = 1)
      self.velocityYL = tk.Label(self.planetStats, text = "Velocity Y : ")
      self.velocityYL.grid(row = 2, column = 0)
      self.velocityYE = tk.Entry(self.planetStats)
      self.velocityYE.grid(row = 2, column = 1)
      self.nameL = tk.Label(self.planetStats, text = "Name : ")
      self.nameL.grid(row = 3, column = 0)
      self.nameE = tk.Entry(self.planetStats)
      self.nameE.grid(row = 3, column = 1)
      self.massL = tk.Label(self.planetStats, text = "Mass : ")
      self.massL.grid(row = 4, column = 0)
      self.massE = tk.Entry(self.planetStats)
      self.massE.grid(row = 4, column = 1)
      self.sizeL = tk.Label(self.planetStats, text = "Size : ")
      self.sizeL.grid(row = 5, column = 0)
      self.sizeE = tk.Entry(self.planetStats)
      self.sizeE.grid(row = 5, column = 1)
      self.postionXL = tk.Label(self.planetStats, text = "Position X : ")
      self.postionXL.grid(row = 6, column = 0)
      self.positionXE = tk.Entry(self.planetStats)
      self.positionXE.grid(row = 6, column = 1)
      self.postionYL = tk.Label(self.planetStats, text = "Position Y : ")
      self.postionYL.grid(row = 7, column = 0)
      self.positionYE = tk.Entry(self.planetStats)
      self.positionYE.grid(row = 7, column = 1)
      self.pathLengthL = tk.Label(self.planetStats, text = "Path Length : ")
      self.pathLengthL.grid(row = 8, column = 0)
      self.pathLengthE = tk.Entry(self.planetStats)
      self.pathLengthE.grid(row = 8, column = 1)
      self.colourL = tk.Label(self.planetStats, text = "Colour (HEX) : ")
      self.colourL.grid(row = 9, column = 0)
      self.colourE = tk.Entry(self.planetStats)
      self.colourE.grid(row = 9, column = 1)
      self.addB = tk.Button(self.planetStats, text = "Add Planet", command = self.count)
      self.addB.grid(row = 10, column = 0)


      
   
   def count(self):
      self.COUNT = self.COUNT + 1
      print(self.COUNT)
      self.getPlanetVal()
      

   def getPlanetVal(self):
      get1 = self.velocityXE.get()
      get2 = self.velocityYE.get()
      get3 = self.nameE.get()
      get4 = self.massE.get()
      get5 = self.sizeE.get()
      get6 = self.positionXE.get()
      get7 = self.positionYE.get()
      get8 = self.pathLengthE.get()
      get9 = self.colourE.get()


      
      self.allStats = (get1,get2,get3,get4,get5,get6,get7,get8,get9)
      print(self.allStats)
      self.dataList.append(self.allStats)
      print(self.dataList)
#      self.dataList[self.fileNameGet] = self.allStats
#      print(self.dataList)
      self.addedPlanet = tk.Label(self.planetList, text = self.allStats)
      self.addedPlanet.grid(row = self.COUNT, column = 0)
      self.raisePlanetList()



   def listSaveFunction(self):
      mydb = sql.connect("SimulationLogin.db")
      c = mydb.cursor()
      #getFileName = self.fileNameE.get()
      c.execute("""CREATE TABLE IF NOT EXISTS Planets
(FileID TEXT, VelocityX INTEGER, VelocityY INTEGER, Name TEXT, Mass REAL, Size REAL, PositionX INTEGER ,PositionY INTEGER, PathLength INTEGER, PlanetColour TEXT)""")
      print(len(self.dataList))
      for i in self.dataList:
         c.execute("""INSERT INTO Planets VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}")""".format(self.fileNameE.get(),i[0],i[int(1)],i[int(2)],i[3],i[4],i[5],i[6],i[7],i[8]))
             
      mydb.commit()
      mydb.close()

   

   def raisePlanetList(self):
      self.frames["PlanetList"].tkraise()


   def raisePlanetStats(self):
      self.frames["PlanetStats"].tkraise()
      
      


















# BEFORE CHANGES

##   def listSaveFunction(self):
##      mydb = sql.connect("SimulationLogin.db")
##      c = mydb.cursor()
##      #getFileName = self.fileNameE.get()
##      c.execute("""CREATE TABLE IF NOT EXISTS Planets
##(FileID text, VelocityX integer, VelocityY integer, Name text, Mass real, Size real, PositionX integer, PositionY integer, PathLength integer, PlanetColour text)""")
##      print(len(self.dataList))
##      for i in self.dataList:
##         c.execute("""INSERT INTO Planets VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}","{7}","{8}","{9}")""".format(self.fileNameE.get(),i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
##             
##      mydb.commit()
##      mydb.close()






      
