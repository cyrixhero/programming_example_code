#
# Chapter 14. User Interfaces
#
# infopanel.py
#

import pyui

from hoop import engine

class InfoPanel(pyui.widgets.FormPanel):
    """Panel to display data about a sim.
    """
    
    setup = [
        ("int",   "gid",      "Game Id:",    1, None),        
        ("float", "posX",     "X Position:", 1, None),
        ("float", "posY",     "Y Position:", 1, None),
        ("float", "velocityX","X Velocity:", 1, None),
        ("float", "velocityY","Y Velocity:", 1, None),
        ("float", "facing",   "Facing:",     1, None)
        ]
    
    def __init__(self):
        pyui.widgets.FormPanel.__init__(self, InfoPanel.setup)
        self.subject = None
        
    def signal(self, subject):
        (screenX, screenY) = engine.worldToScreen(subject.posX, subject.posY)
        self.window.moveto(screenX, screenY)
        self.populate(subject)        

