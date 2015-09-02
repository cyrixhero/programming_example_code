#
# Chapter 6. Data Driven Simulations
# world.py
#

import math

class World:
    """Simulation world.
    """
    def __init__(self, width, height):
        self.width = width
	self.height = height
	self.mobiles = []    # the set of mobile simObjects
	self.immobiles = []	 # the set of immobile simObjects

    def addToWorld(self, sim, x, y, facing, speed=0, force=0):
        sim.posX = x
        sim.posY = y
        if force==0 and self.canMove(sim,x, y, facing) == 0:
            return 0
        if sim.mobile:
            self.mobiles.append(sim)
	else:
            self.immobiles.append(sim)
        sim.setState(x, y, facing, speed)
        return 1

    def removeFromWorld(self, sim):
        if sim.mobile:
            self.mobiles.remove(sim)
        else:
            self.immobiles.remove(sim)
        if sim.removeCallback:
            sim.removeCallback(self)
        return 1

    def update(self, interval):
	"""update the simulation world for an interval
        """
        deleteList = []
        for sim in self.mobiles:
            if sim.update(interval, self) == 0:
                deleteList.append(sim)
        for sim in deleteList:
            self.removeFromWorld(sim)
        return 1

    def canMove(self, sim, newPosX, newPosY, newFacing):
        if newPosX < 0 or newPosY < 0:
            return 0
        if newPosX + sim.width >= self.width or newPosY + sim.height >= self.height:
            return 0
        return 1

    def removeAll(self):
        while len(self.mobiles):
            m = self.mobiles[0]
            self.removeFromWorld(m)
        while len(self.immobiles):
            m = self.immobiles[0]
            self.removeFromWorld(m)


def toRadians(degrees):
    return ((360-degrees) / 360.0) * 2 * math.pi    

class SimObject:
    """A Simulation object in a two-dimensional space.
    """
    def __init__(self, category):
        self.category = category
        self.width = category.width         # width of object
        self.height = category.height       # height of object
        self.mobile = category.mobile       # is object mobile        
        self.life = category.life           # lifetime (seconds)
        self.threshold = category.threshold # variable update frequency
        
        self.posX = 0         # current X position
        self.posY = 0         # current Y position
        self.velocityX = 0    # current X velocity
        self.velocityY = 0    # current Y velocity
        self.facing = 0       # current facing (degrees)
        self.turnRate = 0     # degrees / second
        self.accel = 0        # speed / second
        self.alive = 1        # flag for staying alive
        self.uDelay = 0       # update delay
        self.uTimer = 0       # update timer
        self.removeCallback = None # callback when removed from the world

    def setState(self, posX, posY, facing, speed = 0):
	"""Set the simulation state of the object.
        """
	self.posX = posX
	self.posY = posY
	self.facing = facing
	self.calculateVelocity(speed, facing)

    def calculateVelocity(self, speed, facing):
	radians = toRadians(self.facing)
        self.velocityX = math.cos(radians) * speed
        self.velocityY = math.sin(radians) * speed
        
    def update(self, interval, world):
        """update an object's physical state for an interval.
        """
        if self.threshold and self.uDelay:
            self.uTimer += interval
            if self.uTimer < self.uDelay:
                return
            else:
                interval = self.uTimer
                self.uTimer -= self.uDelay
        
        radians = toRadians(self.facing)
        if self.accel:
            dx = math.cos(radians) * self.accel
            dy = math.sin(radians) * self.accel
            self.velocityX += dx
            self.velocityY += dy

        newPosX = self.posX + (self.velocityX * interval)
        newPosY = self.posY - (self.velocityY * interval)

        if self.turnRate:
            newFacing = self.facing + self.turnRate*interval
            newFacing = newFacing % 360
        else:
            newFacing = self.facing

        if world.canMove(self, newPosX, newPosY, newFacing):
            self.posX = newPosX
            self.posY = newPosY
            self.facing = newFacing
            
        if self.life:
            self.life -= interval
            if self.life <= 0:
                self.alive = 0

        print "life: %2.1f sim at %f2.1,%2.1f, %1.2f" %(self.life, self.posX, self.posY, interval)
        # calculate the variable delay
        if self.threshold:
            value = max( abs(self.velocityX), abs(self.velocityY), abs(self.turnRate) )
            if value < self.threshold:
                self.uDelay = 1.0 - (value / self.threshold)
            else:
                self.uDelay = 0
        #print "vx: %2.1f vy: %2.1f rotation: %s uDelay: %2.4f uTimer: %2.1f" % (self.velocityX, self.velocityY, self.turnRate, self.uDelay, self.uTimer)
        return self.alive

    def setRemoveCallback(self, callback):
        self.removeCallback = callback

    def findOffset(self, direction, distance):
        """find a position in a direction a distance from the center of the sim.
        """
        radians = toRadians(direction)        
        dx = math.cos(radians) * distance
        dy = math.sin(radians) * distance
        return (self.posX + dx, self.posY - dy)
