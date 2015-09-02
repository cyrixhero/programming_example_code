#
# Chapter 4. Python Game Framework
# main.py
#

from pyui import core

class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def run(self):
        """I am called to begin the running of the game. 
        """
        running = 1
        frames = 0
        counter = 0
        lastFrame = 0
        while running:
            core.draw()
            if core.update():
                pass # update world here
            else:
                running = 0
            
            # track frames per second
            frames += 1
            counter += 1
            now = core.readTimer()
            
            # calculate FPS
            if now - lastFrame > 1.0:
                FPS = counter
                counter = 0
                lastFrame = now
                print "FPS: %2d " % FPS
                
def run():
    width = 100
    height = 100
    core.init(width, height)
    app = Application(width, height)
    app.run()
    core.quit()

if __name__ == '__main__':
    run()
