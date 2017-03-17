from Tkinter import *
import time

class MyLogger():
    
    def __init__(self, textArea):
        self.textArea = textArea
        self.textArea.tag_config('ERROR', foreground='red')
        self.textArea.tag_config('NORMAL', foreground='black')
        self.counter = 0;
        
    def debug(self, text):
        self.__log(text + "\n", 'NORMAL')
        
    def error(self, text):
        self.__log(text + "\n", 'ERROR')
        
    def info(self, text):
        self.__log(text + "\n", 'NORMAL')
        
    def step(self, text):
        self.__log("(" + str(self.counter) + ") " + text + "\n", 'NORMAL')
        self.counter += 1
        
    def __log(self, text, textType):
        t = time.mktime(time.localtime())
        outText = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
        self.textArea.insert(END, "[" + outText + "] " + text, textType)