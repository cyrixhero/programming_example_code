#
# Chapter 6. Data Driven Simulations
# datamanager.py
#

import copy
from world import SimObject


class Category:
    """ base class for all Category classes that describe
    simulation objects in the game.
    """
    def __init__(self, name):
        self.name = name

class SimCategory(Category):
    """I am a category class for simulation objects. Each sim category
    has data that allows it to create a different type of actual
    simObject."""
    def __init__(self, name, width, height, mobile, life, threshold):
        Category.__init__(self, name)
        self.width = width
        self.height = height
        self.mobile = mobile
        self.life = life
        self.threshold = threshold
        
    def create(self):
        """Create a SimObject using my data as a template.
        """
        newSim = SimObject(self)
        return newSim

class DataManager:
    """Repository of category objects that define the types
    of simulation objects in the game.
    """
    def __init__(self):
        self.categories = {}    # lists of category objects
        self.initCategory("sims", initialSimCategories, SimCategory)        
        
    def initCategory(self, label, rawData, categoryClass):
        newCatList = []
        self.categories[label] = newCatList
        for categoryTuple in rawData:
            newCatObj = apply( categoryClass, categoryTuple)
            newCatList.append( newCatObj )

    def findCategory(self, name, categoryName):
        category = self.categories.get(categoryName, None)
        if not category:
            return None
        for cat in category:
            if cat.name == name:
                return cat

    def createInstance(self, name, categoryName, *args):
        category = self.findCategory(name, categoryName)
        if category:
            return apply(category.create, args)


initialSimCategories = [
     # name                width height mobile  life threshold
     ("mobile square",       10,    10,     1,     0,  0),
     ("mobile rectangle",    50,     4,     1,     0,  6),
     ("static square",       10,    10,     0,     0,  1) ]
