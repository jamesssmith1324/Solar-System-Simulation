import pygame
from pygame.locals import *
import math
import time
import sys
import os
import tkinter as tk

# Large mass so newtons equation outputs a significant number.
class Star():
    def __init__(self, planetList, screen, mass = 10000000, massS = 20000000 , gravityConstant = (6.673 * 10 ** -9)):
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
        self.sizeS = int(massS/5000000)
        self.gravityConstant = gravityConstant

    def draw(self):
        # Draws sun
        # [960,540] = Middle of the screen
        pygame.draw.circle(self.screen, [255, 200, 0], [768, 432], self.sizeS)
        # Draws Planets
        for i in (self.planets):
                textMe = pygame.font.SysFont("Comic Sans MS",10)
                textsurface = textMe.render(i.name, False, (0, 0, 0))
                self.screen.blit(textsurface,(i.position[0],i.position[1]))
                pygame.draw.lines(self.screen,[0,0,0],False,i.path)
                pygame.draw.circle(self.screen,i.colour,[int(i.position[0]),int(i.position[1])],int(i.size))

                
            
                

    def update(self):
        end = False
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    end = True
                elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    end = True
        for i in range(self.iterations):
                for i in (self.planets[0:4]):
                        r = math.sqrt((i.position[0] - 768) ** 2 + (i.position[1] - 432) ** 2)
                        # Newtons Law of Gravitaion
                        force = (self.gravityConstant * self.mass * i.mass)/(r ** 2)
                        force = round(force,3)
                        #print(force)
                        # As the planet gets closer to the sun it speeds up
                        vect = [round(((768 - i.position[0]) / r ) * force,3), round(((432 - i.position[1]) / r ) * force,3)]
                        
                        #print(vect)
                        i.velocity[0] += vect[0]
                        i.velocity[1] += vect[1]
                        i.update()
                    
        self.draw()
        return end


            
                


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

    def update(self):
# Position on the grid
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
# Traces the location of the planet
        self.path.append([self.position[0], self.position[1]])
# When lenth of the path is equal to the asigned pathLength
        if len(self.path) == self.pathLength:
            self.path.pop(0)

####################################################################################################################################################################################################
                  

class Run():
    def __init__(self,val5,val6,val7,val8):
        self.pval5 = val5
        self.pval6 = val6
        self.pval7 = val7
        self.pval8 = val8
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode([0,0],pygame.FULLSCREEN)
        clock = pygame.time.Clock()
        mass = 10000000
        LIST = []
        #Velocity, Name, Mass, Postition[x,y], PathLangth
        if self.pval5 == 1:
            jupiter = Planet([4,0],"Jupiter",5*10**4,11,[718,572],40,[139,63,73])
            LIST.append(jupiter)
        if self.pval6 == 1:
            saturn = Planet([3,-0],"Saturn",5*10**4,10,[718,692],40,[246,210,60])
            LIST.append(saturn)
        if self.pval7 == 1:
            uranus = Planet([3,0],"Uranus",5*10**4,5,[658,750],40,[91,93,223])
            LIST.append(uranus)
        if self.pval8 == 1:
            neptune = Planet([2.8,0],"Neptune",5*10**4,5,[618,832],40,[91,93,223])
            LIST.append(neptune)
        Sun = Star(LIST, pygame.display.set_mode([1536,864],pygame.FULLSCREEN))


        
        end = False
        while not end:
            screen.fill([255, 255, 255])
            
            end = Sun.update()
            

            pygame.display.update()
            clock.tick()
        pygame.quit()

        

        














    

