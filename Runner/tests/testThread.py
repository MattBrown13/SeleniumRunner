import threading
import sys, os, traceback
import importlib
from Tkinter import *

class TestThread(threading.Thread):
    def __init__(self, mainWindow, testId, testPath, logger):
        super(TestThread, self).__init__()
        self.mainWindow = mainWindow
        self.testId = testId
        self.testPath = testPath
        self.logger = logger
        self.logger.counter = 0
        self.mainWindow.logArea.delete('1.0', END)#clear textArea
        
    def run(self):
        try:
            print "1"
            sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Runner', 'tests'))
            #sys.path.insert(0, "/home/matt/Dokumenty/eclipse_workspace/Runner/tests")
            print "2"
            i = importlib.import_module(self.testPath)
            print "3"
            i.run(self.logger)
            self.mainWindow.setGreenDot(self.testId)
        except:
            traceback.print_exc()
            self.mainWindow.setRedDot(self.testId)
    