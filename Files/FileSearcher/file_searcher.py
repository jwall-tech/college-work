import os
import msvcrt
RootDir = "I:\Desktop\college-work\Files\FileSearcher\Root"

class Element():
    def __init__(self,name,value,typ,func):
        self.Name = name
        self.Value = value
        self.Type = typ
        self.OpenFunc = func

class Screen():
    Title = "Menu"
    Elements = {}
    CurrentIndex = 0
    Elements = 0

    def AddElement(self):
        pass
    
    def Loop(self):
        while True:
            print(msvcrt.getwch())
            if msvcrt.kbhit():
                key = msvcrt.getch()
                print(key)

MyScreen = Screen()

MyScreen.Loop()
