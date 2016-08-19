import ImageGrab
import ImageOps
from numpy import *
import os
import time
import win32api,win32con

def getCords():
    x,y = win32api.GetCursorPos()
    print x,y


def main():
    pass

if  __name__ == '__main__' :
    main()
    
