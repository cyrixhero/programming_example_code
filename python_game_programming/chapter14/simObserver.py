#
# Chapter 14. User Interfaces
#
# simObserver.py
#

import os
from random import randint

import pyui
from hoop.world import World
from hoop import engine
from hoop.entity import Entity

from infopanel import InfoPanel

class UCategory:
    def __init__(self):
        self.name = "gob"
        self.mobile = 1
        self.collide = 1
        self.threshold = 0
        self.life = 0
        self.image = "basic.png"
        self.source = "sourceQuad.py"

class Updater(Entity):
    """make sure notify is called every frame.
    """
    def update(self, interval, world):
        self.dirty = 1
        return Entity.update(self, interval, world)
    
class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = pyui.desktop.getRenderer()
        self.world = World(width, height)
        engine.initialize(width, height)        
        self.renderer.setBackMethod(self.drawStuff, width, height)
        pyui.desktop.getDesktop().registerHandler(pyui.locals.MOUSEMOVE, self.pickObject)
        
        self.f = pyui.widgets.Frame(20,20,260,180, "Object Info");
        self.infoPanel = InfoPanel()
        self.f.replacePanel(self.infoPanel)

        self.sims = []
        category = UCategory()
        
        for i in range(0,20):
            sim = Updater(category)
            self.sims.append(sim)
            x = randint(0,width-20)
            y = randint(0,height-20)
            facing = randint(0,360)
            speed = randint(0,200)
            sim.turnRate = 200
            self.world.addToWorld(sim ,x, y, facing, speed)

        self.selected = self.sims[0]
        self.selected.addObserver(self.infoPanel)

    def drawStuff(self, width, height):
        engine.clear()
        engine.render()

    def pickObject(self, event):
        (worldX, worldY) = engine.screenToWorld(event.pos[0], event.pos[1])
        sim = self.world.checkPoint(worldX, worldY)
        if sim:
            self.selected.removeObserver(self.infoPanel)
            sim.addObserver(self.infoPanel)
            self.selected = sim
            self.selected.notify()
        
    def run(self):
        running = 1
        frames = 0
        counter = 0
        lastFrame = pyui.readTimer()
        endFrame = pyui.readTimer()
        
        while running:
            pyui.draw()
            if pyui.update():
                interval = pyui.readTimer() - endFrame
                self.world.update(interval)
                endFrame = pyui.readTimer()
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
                print "FPS: %2d" % (FPS )
                
                
def run():
    width = 800
    height = 600
    pyui.init(width, height, "p3d", 0)
    app = Application(width, height)
    app.run()
    pyui.quit()

if __name__ == '__main__':
    run()
