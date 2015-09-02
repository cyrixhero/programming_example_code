#
# Chapter 6. Data Driven Simulations
#
# example.py
#

import pyui

from world import World, SimObject
from datamanager import DataManager

class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world = World(100,100)

        self.dm = DataManager()
        newObject = self.dm.createInstance("mobile rectangle", "sims")
        self.world.addToWorld(newObject, 20, 20, 10, 5)

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
		# update world here
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
                print "FPS: %2d " % FPS
                
def run():
    width = 800
    height = 600
    pyui.init(width, height)
    app = Application(width, height)
    app.run()
    pyui.quit()

if __name__ == '__main__':
    run()
