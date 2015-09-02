#
# Chapter 8. Graphics
#
# firstGraphics.py
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

    engine.drawRect(50, 50, 300, 200, pyui.colors.blue)
    engine.drawText("First Graphics Test", (50,50), pyui.colors.white)
    
class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = pyui.desktop.getRenderer()
        self.dm = datamanager.DataManager()
        self.world = world.World(width, height)

        self.renderer.setBackMethod(drawStuff, width, height)
        engine.initialize(width, height)        
        
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
    width = 400
    height = 300
    pyui.init(width, height)
    app = Application(width, height)
    app.run()
    pyui.quit()

if __name__ == '__main__':
    run()

        
