import ImageGrab
import ImageOps
import Image
from numpy import *
import os
import time
import win32api,win32con
import sys

#button press cords
cordDone = (1467,877)
cordDown = (1495,636)
cordUp = (1489,514)
cordRob = (711,824)
cordMenu = (1215,833)
cordReturn = (1207,822)
#house select cords
cordHouses = [(1000,400),(1000,448),(1000,496),(1000,544),(1000,592),(1000,640),(1000,688),(1000,736)]

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    print "Click"

def rightArrow():
    win32api.keybd_event(win32con.VK_RIGHT, 0, 0,0)
    time.sleep(.2)
    win32api.keybd_event(win32con.VK_RIGHT, 0, win32con.KEYEVENTF_KEYUP,0)

def leftArrow():
    win32api.keybd_event(win32con.VK_LEFT, 0, 0,0)
    time.sleep(.2)
    win32api.keybd_event(win32con.VK_LEFT, 0, win32con.KEYEVENTF_KEYUP,0)

def mousePos(cord):
    win32api.SetCursorPos(cord)

def pageLoad():
    box = (1000,374, 1425, 758)
    im = ImageGrab.grab(box)
    while im.getpixel((1,380)) == (0,0,0):
        
        print "page loading"
        time.sleep(.2)
        im = ImageGrab.grab(box)
    print "loaded"
    #im.save(os.getcwd() + '\\tempSnapshots\\full_snap__' + str(int(time.time())) + '.png' , 'PNG') #saves snapshot
    return im

def initialPriceCheck():
    im = pageLoad()     #image of all of the houses
    box1 = (43,344,83,376)
    bottomHouseCheck1 = im.crop(box1)    #crop for $# msb
    box2 = (151, 151, 158,175)
    bottomHouseCheck2 = im.crop(box2)
    
    #bottomHouseCheck2.save(os.getcwd() + '\\tempSnapshots\\snap__' + str(int(time.time())) + '.png' , 'PNG') #saves snapshot
    tempNumb = Image.open(os.getcwd() + '\\referenceSnapshots\\$2grey.png')
    tempGreyRect = Image.open(os.getcwd() + '\\referenceSnapshots\\greyRect.png')
    tempBlackRect = Image.open(os.getcwd() + '\\referenceSnapshots\\blackRect.png')

    while bottomHouseCheck2.tostring() != tempGreyRect.tostring():
        mousePos(cordDown)
        leftClick()
        time.sleep(.2)
        im = pageLoad()
        bottomHouseCheck2 = im.crop(box2)
    while bottomHouseCheck1.tostring() != tempNumb.tostring():
        mousePos(cordDown)
        leftClick()
        time.sleep(.2)
        im = pageLoad()
        bottomHouseCheck1 = im.crop(box1)
        
        
#now we are in the $2000s!
    print "Now in $2000s"
    return im

def chooseHouse(im):
    targetHouse1 = Image.open(os.getcwd() + '\\referenceSnapshots\\targetHouse1.png')
    targetHouse2 = Image.open(os.getcwd() + '\\referenceSnapshots\\targetHouse2.png')
    oneThousandCheck = Image.open(os.getcwd() + '\\referenceSnapshots\\$1black.png')
    threeThousandCheck = Image.open(os.getcwd() + '\\referenceSnapshots\\$3black.png')
    fourThousandCheck = Image.open(os.getcwd() + '\\referenceSnapshots\\$4black.png')
    
    topLeftX = 43
    topLeftY = 8
    bottomRightX = 395
    bottomRightY = 40

    down = 1
    picNumber = 0
    counter = 0
    while counter != 8:
        box = (topLeftX, topLeftY + counter * 48, bottomRightX, bottomRightY + counter * 48)
        houseInfo = im.crop(box)
        #houseInfo.save(os.getcwd() + '\\tempSnapshots\\snap__' + str(picNumber) + '.png' , 'PNG') #saves snapshot
        picNumber = picNumber + 1
        if houseInfo.tostring() == targetHouse1.tostring() or houseInfo.tostring() == targetHouse2.tostring():
            selectHouse(counter) #house is going to be robbed
        if counter == 7:        #no $2000 0 0 house found on page
            box2 = (43,8,79,40)
            box3 = (43,344,79,376)
            topHouseCheck = im.crop(box2)
            bottomHouseCheck = im.crop(box3)
            topHouseCheck = im.crop(box2)
            #topHouseCheck.save(os.getcwd() + '\\tempSnapshots\\snap__' + str(int(time.time())) + '.png' , 'PNG') #saves snapshot
            if bottomHouseCheck.tostring() == oneThousandCheck.tostring():
                print "numbers to low"
                down = 0
            elif topHouseCheck.tostring() == threeThousandCheck.tostring() or topHouseCheck.tostring() == fourThousandCheck.tostring():
                print "numbers to high" 
                down = 1

            if down == 1:
                mousePos(cordDown)
            else:
                mousePos(cordUp)
            leftClick()# go to next page
            
            im = pageLoad()
            counter = 0
            
        counter = counter + 1
        

def selectHouse(index):
    mousePos(cordHouses[index])
    leftClick()
    time.sleep(.1)
    mousePos(cordRob)
    leftClick()
    print "the house has been chosen"
    box = (1105,466,1155,530)
    box2 = (655,466,665,530)
    time.sleep(2)
    entrance = ImageGrab.grab(box2)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\tempSnapshots\\snap__' + str(int(time.time())) + '.png' , 'PNG')
    targetVault = Image.open(os.getcwd() + '\\referenceSnapshots\\targetVault.png')
   
    if im.tostring() == targetVault.tostring():
        print 'reached if'
        counter = 0
        while counter != 9:
            rightArrow()
            counter = counter + 1
        counter = 0
        time.sleep(1)
        mousePos(cordReturn)
        leftClick()
        time.sleep(.2)
        mousePos(cordDone)
        leftClick()
        return
    elif entrance.getpixel((5,5)) != (0,0,0):
        print 'reached elif'
        leftArrow()
        time.sleep(.1)
        muousePos(cordReturn)
        leftClick()
        return
    else:
        print 'reached else'
        mousePos(cordMenu)
        leftClick()
        return
    
    sys.exit()
    

def main():
    mousePos(cordDone)  #get to house list 
    leftClick()         #'' ''  ''  ''
    time.sleep(.5)      #allow menu to transition
    #initialPriceCheck()
    chooseHouse(initialPriceCheck())

if  __name__ == '__main__' :
    main()
    
