#
# Chapter 8. Graphics
# visualize.py
#
import math
import pyui
import pygame
from random import randint

from hoop.datamanager import SimCategory, DataManager
from hoop import world
from hoop import engine
from hoop.sim import SimObject

def drawGrid(grid):
    """Draw the collision grid
    """
    engine.clear()
    for x in range(0,grid.numSquaresX):
        engine.drawLine( x * grid.squareWidth, 0, 
                         x * grid.squareWidth, grid.height, pyui.colors.grey)
    for y in range(0,grid.numSquaresY):
        engine.drawLine( 0, y * grid.squareHeight, 
                         grid.width, y * grid.squareHeight, pyui.colors.grey)
    for square in grid.squares.values():
        pyui.desktop.getRenderer().drawText( "%d" % len(square.sims),
                         (square.posX+30, 580-square.posY), pyui.colors.white, flipped=1)
    engine.render()

class CollisionSim(SimObject):
    def __init__(self, category):
        SimObject.__init__(self, category, self.drawAABB)
        
    def drawAABB(self):
        engine.drawRect(
            self.aabb.worldAABB.minX,
            self.aabb.worldAABB.minY,
            self.aabb.worldAABB.maxX - self.aabb.worldAABB.minX,
            self.aabb.worldAABB.maxY - self.aabb.worldAABB.minY,
            (255,255,255,100) )

    def drawBoundingSphere(self):
        engine.drawRect(
            self.aabb.worldSphere.posX - self.aabb.worldSphere.radius,
            self.aabb.worldSphere.posY - self.aabb.worldSphere.radius,
            self.aabb.worldSphere.radius*2,
            self.aabb.worldSphere.radius*2,            
            (255,255,255,100) )            

class CollisionCategory(SimCategory):
    def __init__(self):
        SimCategory.__init__(self,"collision",1,0,1,0,"sourceQuad",None)

class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = pyui.desktop.getRenderer()
        
        self.dm = DataManager()
        self.world = world.World(width, height)

        self.renderer.setBackMethod(drawGrid, self.world.grid)
        engine.initialize(width, height)
        
        cat = CollisionCategory()
        for i in range(0,20):
            collisionSim = CollisionSim(cat)
            collisionSim.turnRate = randint(-200,200)
            x = randint(0,width-20)
            y = randint(0,height-20)
            facing = randint(0,360)
            speed = randint(0,200)
            self.world.addToWorld(collisionSim,x, y, facing, speed)
            
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

        
