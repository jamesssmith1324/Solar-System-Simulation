import pygame
from pygame.locals import *
import math
import time
import sys
import os
import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random
import numpy as np
from scipy.interpolate import spline

# Large mass so newtons equation outputs a significant number.
class Star():
    def __init__(self, planetList, screen, mass = 10000000, massS = 100000000 , gravityConstant = (6.673 * 10 ** -9)):
        self.planets = planetList
        self.iterations = 1
        self.mass = mass
        self.massS = massS
        self.screen = screen
        # How big the planet appears on screen
        self.sizeMe = int(mass/12000000)
        self.sizeV = int(mass/8500000)
        self.sizeE = int(mass/8000000)
        self.sizeM = int(mass/10000000)
        self.sizeJ = int(mass/1000000)
        self.sizeSa = int(mass/1000000)
        self.sizeU = int(mass/1000000)
        self.sizeN = int(mass/1000000)
        self.sizeS = int(massS/9000000)
        self.gravityConstant = gravityConstant
        self.velXListMe = []
        self.velXListV = []
        self.velXListE = []
        self.velXListM = []
        self.velYListMe = []
        self.velYListV = []
        self.velYListE = []
        self.velYListM = []
        self.dictCount = -1
        self.f = open("XYText.txt","w")
        
        
        
        

    def draw(self):
        # Draws sun
        # [960,540] = Middle of the screen
        pygame.draw.circle(self.screen, [255, 200, 0], [768, 432], self.sizeS)
        # Draws Planets
        textMe = pygame.font.SysFont("Comic Sans MS",10)
        for i in (self.planets):
                textsurface = textMe.render(i.name, False, (0, 0, 0))
                self.screen.blit(textsurface,(i.position[0],i.position[1]))
                pygame.draw.lines(self.screen,[0,0,0],False,i.path)
                pygame.draw.circle(self.screen,i.colour,[int(i.position[0]),int(i.position[1])],int(i.size))
        
                                
        
    

                
            
                

    def update(self):
        end = False
        num = 0
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    length = len(self.velXListMe)
                    while num != length:
                        self.f.write("\n{0}/{1},{2}/{3},{4}/{5},{6}/{7}".format(self.velXListMe[num],self.velYListMe[num],self.velXListV[num],self.velYListV[num],self.velXListE[num],self.velYListE[num],self.velXListM[num],self.velYListM[num],))
                        num += 1
                    end = True
                    Graph()
        self.dictCount = -1
        self.dictCount += 1
        lenCount = 0
        if self.dictCount < 4:
            self.dictCount = -1
        xDic = {0:"",1:"",2:"",3:""}
        yDic= {0:"",1:"",2:"",3:""}
        for i in range(self.iterations):
                for i in (self.planets[0:4]):
                        r = math.sqrt((i.position[0] - 768) ** 2 + (i.position[1] - 432) ** 2)
                        # Newtons Law of Gravitaion
                        force = (self.gravityConstant * self.mass * i.mass)/(r ** 2)
                        force = round(force,3)
                        vect = [round(((768 - i.position[0]) / r ) * force,3), round(((432 - i.position[1]) / r ) * force,3)]
            
                        i.velocity[0] += vect[0]
                        i.velocity[1] += vect[1]
                        
                        self.dictCount += 1
                        lenCount += 1
                        xDic[self.dictCount] = round(i.velocity[0],3)
                        yDic[self.dictCount] = round(i.velocity[1],3)
                        if lenCount == (len(self.planets)):
                            self.velXListMe.append(xDic[0])
                            self.velYListMe.append(yDic[0])
                            self.velXListV.append(xDic[1])
                            self.velYListV.append(yDic[1])
                            self.velXListE.append(xDic[2])
                            self.velYListE.append(yDic[2])
                            self.velXListM.append(xDic[3])
                            self.velYListM.append(yDic[3])
                            


                        #print(xDic)
                        
                        i.update()
        self.draw()
        return end
                        
                        
                    
        
        

##    def animate():
##      style.use("fivethirtyeight")
##      fig = plt.figure()
##      ax1 = fig.add_subplot(1,1,1)
##      xs = []
##      ys = []
##      for i in range(20):
##        randx = random.randint(0,12)
##        xs.append(randx)
##        randy = random.randint(0,12)
##        ys.append(randy)
##
##      ax1.clear()
##      ax1.plot(xs,ys)
##      ani = animation.FuncAnimation(fig, ax1.plot(xs,ys), interval = 1000)
        
        
                    
                


            
                


####################################################################################################################################################################################################


class Planet():
    def __init__(self,velocity,name,mass,size,position,pathLength,colour):
        self.velocity = velocity
        self.name = name
# Defines the size
        self.mass = mass
        self.size = size
        self.colour = colour
# Size of the orbiting planet
        self.position = position
# Length of the line of behind the planet
        self.pathLength = pathLength
        self.path = [[self.position[0], self.position[1]]]
        self.posXList = []
        self.posYList = []

        

    def update(self):
# Position on the grid
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.posXList.append(self.position[0])
        self.posYList.append(self.position[1])
# Traces the location of the planet
        self.path.append([self.position[0], self.position[1]])
# When lenth of the path is equal to the asigned pathLength
        if len(self.path) == self.pathLength:
            self.path.pop(0)
        #print(self.posXList)
        

####################################################################################################################################################################################################
                  

class Run():
    def __init__(self,val1,val2,val3,val4):
        self.pval1 = val1
        self.pval2 = val2
        self.pval3 = val3
        self.pval4 = val4
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        mass = 10000000
        LIST = []
        #Velocity, Name, Mass, Postition[x,y], PathLangth
        if self.pval1 == 1:
            mercury = Planet([4,0],"Mercury",5*10**4,int(mass/8500000),[718, 572],20,[181,167,167])
            LIST.append(mercury)
        if self.pval2 == 1:
            venus = Planet([3,0],"Venus",5*10**4,int(mass/8000000),[718, 692],20,[187,183,171])
            LIST.append(venus)
        if self.pval3 == 1:    
            earth = Planet([2.6,0],"Earth",5*10**4,int(mass/10000000),[718,800],20,[113,148,68])
            LIST.append(earth)
        if self.pval4 == 1:
            mars = Planet([2.6,0],"Mars",5*10**4,int(mass/10000000),[718,832],20,[153,133,122])
            LIST.append(mars)
        
        Sun = Star(LIST, pygame.display.set_mode([1536,864],pygame.FULLSCREEN))
        #val = 1
        
    
        #screen.fill([255, 255, 255])

        
        
        end = False
        while not end :
            
            screen.fill([255, 255, 255])
            end = Sun.update()
            clock.tick()
            pygame.display.update()
        pygame.quit()
               

        


class Graph:
    def __init__(self):
        self.root = tk.Tk()
        self.mainFrame = tk.Frame(self.root, width = 200, height = 100)
        #self.mainFrame.grid(row = 0, column = 0)
        self.mainFrame.pack_propagate(False)
        self.Title = tk.Label(self.root, text = "Do you want to display a graph").pack()
        self.yesB = tk.Button(self.root, text = "Yes",command = self.animate).pack()
        self.GMe = tk.IntVar()
        self.box1 = tk.Checkbutton(self.root, text = "Mercury", variable = self.GMe).pack()
        self.GV = tk.IntVar()
        self.box2 = tk.Checkbutton(self.root, text = "Venus", variable = self.GV).pack()
        self.GE = tk.IntVar()
        self.box3 = tk.Checkbutton(self.root, text = "Earth", variable = self.GE).pack()
        self.GM = tk.IntVar()
        self.box4 = tk.Checkbutton(self.root, text = "Mars", variable = self.GM).pack()
        self.noB = tk.Button(self.root, text = "No").pack()


    def animate(self):
        MeXar = []
        MeYar = []
        VXar = []
        VYar = []
        EXar = []
        EYar = []
        MXar = []
        MYar = []
        pullData = open("XYtext.txt","r").read()
        dataArray = pullData.split('\n')
        #print(dataArray)
        for eachLine in dataArray:
            P = eachLine.split(",")
            #print(P)
            #print(P,"P")
            for eachXY in P:
                if len(eachXY)>1:
                        Me = P[0]
                        V = P[1]
                        E = P[2]
                        M = P[3]
                        #print(Me,V,E,M,"planets")
                        MeX,MeY = Me.split("/")
                        MeXar.append(MeX)
                        MeYar.append(MeY)
                        VX,VY = V.split("/")
                        VXar.append(VX)
                        VYar.append(VY)
                        EX,EY = E.split("/")
                        EXar.append(EX)
                        EYar.append(EY)
                        MX,MY = M.split("/")
                        MXar.append(MX)
                        MYar.append(MY)                

        #for eachLine in dataArray:
        #    if len(eachLine)>1:
        #        x,y = eachLine.split(",")
        #        xar.append((x))
        #       yar.append((y))
        print(self.GMe)
        if self.GMe.get() == 1:
            plt.scatter(MeXar,MeYar,1)
        if self.GV.get() == 1:
            plt.scatter(VXar,VYar,1)
        if self.GE.get() == 1:
            plt.scatter(EXar,EYar,1)
        if self.GM.get() == 1:
            plt.scatter(MXar,MYar,1)
        plt.axis("off")
        plt.show()

                








