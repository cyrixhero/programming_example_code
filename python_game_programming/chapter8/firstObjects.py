#
# Chapter 8. Graphics
#
# firstObjects.py
#

import math
import pyui
import pygame
from random import randint

from hoop import datamanager
from hoop import world
from hoop import engine

def drawStuff(width, height):
    engine.clear()
    color = pyui.colors.yellow
    engine.drawLine(10,10, width-10,10, color)
    engine.drawLine(width-10,10, width-10,height-10, color)
    engine.drawLine(width-10,height-10, 10,height-10, color)
    engine.drawLine(10,height-10, 10,10, color)
    engine.render()

class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = pyui.desktop.getRenderer()
        
        self.dm = datamanager.DataManager()
        self.world = world.World(width, height)

        self.renderer.setBackMethod(drawStuff, width, height)
        engine.initialize(width, height)
        
        for i in range(0,25):
            sim1 = self.dm.createInstance("mobile square", "sims")
            sim1.turnRate = randint(-200,200)
            x = randint(0,width-20)
            y = randint(0,height-20)
            facing = randint(0,360)
            speed = randint(0,1200)
            self.world.addToWorld(sim1,x, y, facing, speed)

    def run(self):
        """I am called to begin the running of the game. 
        """
        running = 1
        frames = 0
        counter = 0
        lastFrame = pyui.readTimer()
        endFrame = pyui.readTimer()
        
        while running:
            pyui.draw()
            if pyui.update():
                interval = pyui.readTimer() - endFrame
                endFrame = pyui.readTimer()
                if self.world.update(interval) == 0:
                    running = 0
            else:
                running = 0
            
            # track frames per second
            frames += 1
            counter += 1
            
            # calculate FPS
            if endFrame - lastFrame > 1.0:
                FPS = counter
                counter = 0
                lastFrame = endFrame
                print "FPS: %2d mobiles: %d statics: %d " % (FPS, len(self.world.mobiles), len(self.world.immobiles) )

def run():
    width = 800
    height = 600
    pyui.init(width, height)
    app = Application(width, height)
    app.run()
    app = None
    pyui.quit()

if __name__ == '__main__':
    run()

        
