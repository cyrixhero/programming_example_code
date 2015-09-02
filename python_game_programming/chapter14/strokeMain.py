#
# Chapter 14. User Interfaces
#
# strokeMain.py
#
import os
import pyui
import pickle

# Colors for color menu
colors = [
    ("Red",   (255,0,0,255) ),
    ("Green", (0,255,0,255) ),
    ("Blue",  (0,0,255,255) ),
    ("White", (255,255,255,255) ),
    ("Grey",  (128,128,128,255) )
    ]


class SaveDialog(pyui.dialogs.Dialog):
    """Dialog to accept a filename entered by the user.
    """
    def __init__(self):
        pyui.dialogs.Dialog.__init__(self, w = 300, h=100, title = "Save File")
        self.setLayout(pyui.layouts.GridLayoutManager(2,2))
        self.label = pyui.widgets.Label("Filename:")        
        self.edit = pyui.widgets.Edit("stuff.stk", self.onEnter)
        self.okButton = pyui.widgets.Button("OK", self.onOK)
        self.cancelButton = pyui.widgets.Button("Cancel", self.onCancel)

        self.addChild(self.label)
        self.addChild(self.edit)
        self.addChild(self.okButton)
        self.addChild(self.cancelButton)
        self.pack()

    def onEnter(self, edit):
        self.close(self.edit.text)
        return 1

    def onOK(self, button):
        self.close(self.edit.text)
        return 1

    def onCancel(self, button):
        self.close(0)
        return 1

    
class CanvasFrame(pyui.widgets.Frame):
    """Frame with a menu that contains the draw canvas.
    """
    def __init__(self):
        pyui.widgets.Frame.__init__(self, 10, 10, 780, 580, "Canvas")
        self.canvas = CanvasPanel()
        self.replacePanel( self.canvas )
        self.createMenus()

    def frameResize(self, w, h):
        """dont allow resizing"""
        return

    def frameMove(self, x, y):
        """dont allow moving"""
        return

    def frameClose(self):
        """dont allow closing"""
        return
    
    def createMenus(self):
        self.menubar = pyui.frame.FrameMenuBar()
        self.actionMenu = pyui.frame.FrameMenu("Actions")        
        self.colorMenu = pyui.frame.FrameMenu("Colors")
        self.menubar.addMenu(self.actionMenu)
        self.menubar.addMenu(self.colorMenu)        
        self.setMenuBar(self.menubar)
        
        # add color menus
        for title, color in colors:
            menuItem = self.colorMenu.addItem(title, self.onColorMenu)
            menuItem.color = color
        self.colorMenu.addItem("Custom", self.onCustomColorMenu)

        # add actions
        self.actionMenu.addItem("Open", self.onOpenMenu)        
        self.actionMenu.addItem("Save", self.onSaveMenu)
        self.actionMenu.addItem("Clear", self.onClearMenu)

    ## Menu Handler Functions ##
        
    def onColorMenu(self, item):
        """this uses the color set on the menu item previously
        """
        self.canvas.color = item.color
        return 1

    def onCustomColorMenu(self, item):
        """this dispays a dialog to choose a color"""
        self.dialog = pyui.dialogs.ColorDialog(self.customColorChosen)
        self.dialog.doModal()
        return 1
        
    def onClearMenu(self, item):
        """Clears the strokes on the canvas panel."""
        self.canvas.clear()
        return 1

    def onSaveMenu(self, item):
        """Shows a dialog to save the strokes to"""
        self.dialog = SaveDialog()
        self.dialog.doModal(self.onSaveChosen)
        return 1

    def onOpenMenu(self, item):
        """Shows a dialog to load files from"""
        self.dialog = pyui.dialogs.FileDialog(os.getcwd(), self.onOpenChosen, ".*stk")
        self.dialog.doModal()
        return 1

    def customColorChosen(self, color):
        self.canvas.setColor(color)
        self.dialog.destroy()
        self.dialog = None

    def onSaveChosen(self, filename):
        if filename:
            saveFile = file(filename, 'w')
            pickle.dump(self.canvas.strokes, saveFile)
            saveFile.close()
        self.dialog.destroy()
        self.dialog = None

    def onOpenChosen(self, filename):
        loadFile = file(filename, 'r')
        strokes = pickle.load(loadFile)
        loadFile.close()
        self.canvas.strokes = strokes
        self.setDirty()
        self.dialog.destroy()
        self.dialog = None


class CanvasPanel(pyui.widgets.Panel):
    """Panel to track mouse operations and draw strokes.
    """
    def __init__(self):
        pyui.widgets.Panel.__init__(self)
        self.registerEvent(pyui.locals.LMOUSEBUTTONDOWN, self.onMouseDown)
        self.registerEvent(pyui.locals.LMOUSEBUTTONUP, self.onMouseUp)
        self.registerEvent(pyui.locals.MOUSEMOVE, self.onMouseMotion)

        self.strokes = []
        self.drawing = 0
        self.strokePos = None
        self.color = (255,255,255,255)

    def setColor(self, color):
        self.color = color

    def clear(self):
        self.strokes = []
        self.setDirty()
            
    def onMouseDown(self, event):
        if self.hit(event.pos):
            self.drawing = 1
            self.finishStroke(event.pos)
            return 1
        else:
            self.drawing = 0

    def onMouseUp(self, event):
        if self.hit(event.pos) and self.drawing:
            self.finishStroke(event.pos)
            self.strokePos = None
            self.drawing = 0
            return 1
        else:
            self.drawing = 0

    def onMouseMotion(self, event):
        if self.hit(event.pos) and self.drawing:
            self.finishStroke(event.pos)
            return 1
    
    def finishStroke(self, pos):
        """finish a single stroke and add it to the
        list of strokes.
        """
        windowX = pos[0] - self.window.rect[0]
        windowY = pos[1] - self.window.rect[1]
        endPos = (windowX, windowY)
        if self.strokePos:
            self.strokes.append( (self.strokePos, endPos, self.color) )
            self.setDirty()
        self.strokePos = endPos

    def draw(self, renderer):
        """Draw the strokes and the stroke count.
        """
        renderer.drawRect(pyui.colors.black, self.windowRect)
        renderer.drawText( "Strokes: %d" % len(self.strokes), (650,50), pyui.colors.white)
        for start, end, color in self.strokes:
            renderer.drawLine(start[0], start[1], end[0], end[1], color)

class Application:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.renderer = pyui.desktop.getRenderer()

        self.cf = CanvasFrame()
        
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
