import pygame
from pygame.locals import *
import math
import time
import sys
import os
import tkinter as tk
import sqlite3 as sql

# Large mass so newtons equation outputs a significant number.
class Star():
    def __init__(self, planetList,screen, mass = 10000000, massS = 20000000 , gravityConstant = (6.673 * 10 ** -9)):
        self.planets = planetList
        self.screen = screen
        self.iterations = 1
        self.mass = mass
        self.massS = massS
        self.screen = pygame.display.set_mode([1536,864],pygame.FULLSCREEN)
        self.sizeS = int(massS/9000000)
        self.gravityConstant = gravityConstant

    def draw(self):
        # Draws sun
        # [960,540] = Middle of the screen
        pygame.draw.circle(self.screen, [255, 200, 0], [768, 432], self.sizeS)
        # Draws Planets
        for i in (self.planets):
                strip = i.colour.lstrip('#')
                col = (tuple(int(strip[i:i+2], 16) for i in (0, 2 ,4)))
                textMe = pygame.font.SysFont("Comic Sans MS",10)
                textsurface = textMe.render(i.name, False, (0, 0, 0))
                self.screen.blit(textsurface,(i.positionX,i.positionY))
                pygame.draw.lines(self.screen,[0,0,0],False,i.path)
                pygame.draw.circle(self.screen,col,[int(i.positionX),int(i.positionY)],int(i.size))

                
            
                

    def update(self):
        end = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    end = True
        for i in range(self.iterations):
                for i in (self.planets):
                        r = math.sqrt((i.positionX - 768) ** 2 + (i.positionY - 432) ** 2)
                        # Newtons Law of Gravitaion
                        force = (self.gravityConstant * self.mass * i.mass)/(r ** 2)
                        force = round(force,3)
                        #print(force)
                        # As the planet gets closer to the sun it speeds up
                        vect = [round(((768 - i.positionX) / r ) * force,3), round(((432 - i.positionY) / r ) * force,3)]
                        
                        #print(vect)
                        i.velocityX += vect[0]
                        i.velocityY += vect[1]
                        i.update()
                    
        self.draw()
        return end


            
                


####################################################################################################################################################################################################


class Planet():
    def __init__(self,velocityX,velocityY,name,mass,size,positionX,positionY,pathLength,colour):
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.name = name
        self.mass = mass
        self.size = size
        self.colour = colour
        self.positionX = positionX
        self.positionY = positionY
        self.pathLength = pathLength
        self.path = [[self.positionX, self.positionY]]

    def update(self):
        self.positionX += self.velocityX
        self.positionY += self.velocityY
        self.path.append([self.positionX, self.positionY])
        if len(self.path) == self.pathLength:
            self.path.pop(0)
        

####################################################################################################################################################################################################
                  

class Run():
    def __init__(self):
        self.root = tk.Tk()
        self.loadScreen = tk.Frame(self.root, width = 500, height = 500)
        self.loadScreen.grid(row = 0, column = 0)
        self.FileName()



    def getPlanetData(self):
        mydb = sql.connect('SimulationLogin.db')
        c = mydb.cursor()
        c.execute("""SELECT FileID FROM Planets""")
        data = c.fetchall()
        fileName = self.fileNameE.get()
        #print("D",data)
        c.execute("""SELECT VelocityX, VelocityY, Name, Mass, Size, PositionX, PositionY, PathLength, PlanetColour FROM Planets WHERE FileID = '{0}' """.format(fileName))
        results = c.fetchall()
        LIST =[]
        count = -1
        self.dic = {}
        for i in results:
            count += 1
            self.dic[count] = list(i)

            #for i in self.dic[count]:
            #    print(i)
        print(self.dic)

        for i in range(len(self.dic)):
            LIST.append(self.dic[i])

        print(LIST)


        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        mass = 10000000

        
        print(self.dic)
        planets = []
        for i in self.dic:
            newPlanet = Planet(self.dic[i][0],self.dic[i][1],self.dic[i][2],self.dic[i][3],self.dic[i][4],self.dic[i][5],self.dic[i][6],self.dic[i][7],self.dic[i][8])
            planets.append(newPlanet)
        #saturn = Planet([3,-0],"Saturn",5*10**4,int(mass/1000000),[718,692],40,[246,210,60])
        #uranus = Planet([3,0],"Uranus",5*10**4,int(mass/1000000),[658,750],40,[91,93,223])
        #neptune = Planet([2.8,0],"Neptune",5*10**4,int(mass/1000000),[618,832],40,[91,93,223])
        #for i in range(len(self.dic)):
        #   print(i)
        #    for k in (self.dic[i]):
        #        print(k)
        Sun = Star((planets), pygame.display.set_mode([1536,864],pygame.FULLSCREEN))


        end = False
            
        while not end:
            screen.fill([255, 255, 255])
            end = Sun.update()
            clock.tick()    
            pygame.display.update()
        pygame.quit()
            

        

    def FileName(self):
      self.fileNameFrame = tk.Frame(self.loadScreen, width = 500, height = 500)
      self.fileNameFrame.grid(row = 0, column = 0)
      self.fileNameFrame.grid_propagate(False)
      self.fileNameL = tk.Label(self.fileNameFrame, text = "File Name : ")
      self.fileNameL.grid(row = 0, column = 0)
      self.fileNameE = tk.Entry(self.fileNameFrame)
      self.fileNameE.grid(row = 0, column = 1)
      self.fileNameB = tk.Button(self.fileNameFrame, text = "Load File", command = self.getPlanetData)
      self.fileNameB.grid(row = 1, column = 0)


# edit database Position X and Y same for Velocity
#when reading from the database
#change planet class to accecpt X and Y for both
#change self.position[0] to self.positionX





