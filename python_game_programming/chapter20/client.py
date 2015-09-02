import time
import random
import pyui
from hoop import engine

from tictac.client.application import TicTacClientApp

class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = pyui.desktop.getRenderer()
        self.renderer.setMouseCursor(None)
        engine.initialize(width, height)
        self.client = TicTacClientApp(width, height)
        self.client.connect("localhost", 7777)
        self.renderer.setBackMethod(self.render)
        
    def render(self):
        engine.clear()
        engine.render()
            
    def run(self):
        """I am called to begin running the game. 
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
                if self.client.update(interval) == 0:
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
                print "FPS: %2d" % (FPS )

            time.sleep(0.03)
                
                
def run():
    width = 800
    height = 600
    pyui.init(width, height, "p3d", 0)
    app = Application(width, height)
    app.run()
    pyui.quit()

if __name__ == '__main__':
    run()
