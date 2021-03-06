#
# Chapter 14. User Interface
#
# observer.py
#

class Observable:
    def __init__(self):
        self.dirty = 0
        self.observers = []

    def addObserver(self, observer):
        self.observers.append(observer)
        self.dirty = 1

    def removeObserver(self, observer):
        self.observers.remove(observer)
        self.dirty = 1        

    def notify(self):
        for o in self.observers:
            o.signal(self)
        self.dirty = 0

    def setDirty(self):
        self.dirty = 1

    def clearObservers(self):
        self.observers = []
        
