from Tkinter import *
import tkMessageBox
import sys
from ttk import Treeview
import inspect
import importlib
import os
from PIL import Image, ImageTk
import logging
import Tkinter
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Runner', 'tests'))
from testThread import TestThread

class MainWindow(Tkinter.Tk):
    
    IMAGES_PATH = "gui/images/"
    
    def __init__(self, parent, testCases):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.counter = 0
        self.testCases = testCases
        
        self.mainPanel()
        self.createRunBtn()
        
#GridLayout
    def mainPanel(self):
        self.mainPanel = PanedWindow(orient=HORIZONTAL, borderwidth=5, relief=SUNKEN, showhandle=True)
        self.mainPanel.pack(fill="both", expand=True)
        
        self.treeFrame = PanedWindow(orient=HORIZONTAL, borderwidth=5, relief=SUNKEN, showhandle=True)
        self.createTreeView()
        
        self.logFrame = PanedWindow(orient=HORIZONTAL, borderwidth=5, relief=SUNKEN, showhandle=True)
        self.createLogArea()
        
        self.mainPanel.add(self.treeFrame)
        self.mainPanel.add(self.logFrame)
    
    def createFrames(self):
        print ""
#Widgets     
    def createLogArea(self):
        logFrame = Frame()
        #logFrame.grid(sticky="NSEW")
        logFrame.grid_columnconfigure(0,weight=1)
        logFrame.grid_rowconfigure(0,weight=1)
        
        self.logArea = Text(logFrame, wrap=NONE)
        self.logArea.grid(row = 0, column = 0, sticky="NSEW")
        
        scrollbY = Scrollbar(logFrame, command=self.logArea.yview)
        scrollbY.grid(row=0, column=1, sticky='NSEW')
        self.logArea['yscrollcommand'] = scrollbY.set

        scrollbX = Scrollbar(logFrame, command=self.logArea.xview, orient=HORIZONTAL)
        scrollbX.grid(row=1, column=0, sticky='NEW')
        self.logArea['xscrollcommand'] = scrollbX.set
        
        self.logFrame.add(logFrame)
        
        #self.logArea.insert(END, "Just a text Widget\nin two lines\n")
        sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Runner', 'components'))
        from myLogger import MyLogger
        self.logger = MyLogger(self.logArea)
        self.logger.debug("debugabcdefghijkdebugabcdefghijkdebugabcdefghijkdebugabcdefghijkdebugabcdefghijkdebugabcdefghijkdebugabcdefghijk")
        for i in range(0, 15):
            self.logger.debug("debugabcdefghijk")
            self.logger.error("error")
        
    def createRunBtn(self):
        self.frameThree = Frame(self)
        self.frameThree.pack()
        
        self.btn_run = Button(self.frameThree, text = "Run", command = self.runAction)
        self.btn_run.grid(column = 0, row = 0, sticky = "NSEW")
        
    def createTreeView(self):        
        self.tree = Treeview()
        index = 0
        for case in self.testCases:
            parent = self.tree.insert("", index, case.getId(), text = case.getName(), open = True)
            index += 1
            for test in case.getTestCases():
                self.tree.insert(parent, index, test.getId(), text = test.getName())
                index += 1
        #self.tree.grid(row = 0, column = 0, sticky='NSEW')
        
        self.treeFrame.add(self.tree)
#Actions        
    def updateText(self):
        self.counter += 1
        self.btn_run["text"] = "Run " + str(self.counter)
       
    def runAction(self):
        testId = self.tree.focus()
        path = self.getTestPath(testId)

        self.setYellowDot(testId)
        print path
        if(path != None) :
            self.setYellowDot(testId)
            try:
                threadOne = TestThread(self, testId, path, self.logger)
                threadOne.start()
            except:
                self.setRedDot(testId)
        else:
            tkMessageBox.showinfo("Runner info", "You should choose some testCase")

    def getTestPath(self, testId):
        for case in self.testCases:
            for test in case.getTestCases():
                if test.getId() == testId:
                    return test.getPath()
                
    def setDot(self, testId, rootPic):    
        self.rootPic2 = ImageTk.PhotoImage(rootPic)
        self.tree.item(testId, image = self.rootPic2)
                
    def setYellowDot(self, testId):
        rootPic = Image.open(self.IMAGES_PATH + 'YellowDot.png')
        self.setDot(testId, rootPic)
                
    def setGreenDot(self, testId):
        rootPic = Image.open(self.IMAGES_PATH + 'GreenDot.png')
        self.setDot(testId, rootPic)
        
    def setRedDot(self, testId):
        rootPic = Image.open(self.IMAGES_PATH + 'RedDot.png')
        self.setDot(testId, rootPic)
            
def createWindow(testCases):
    app = MainWindow(None, testCases)
    app.title("Test runner")
    '''window = Tk()
    window.title("Test runner")
    window.geometry("400x400")
    
    app = MainWindow(None, testCases)'''
    
    app.mainloop()
        

