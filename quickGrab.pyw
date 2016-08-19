import ImageGrab
import os
import time

#globals


def screenGrab():
    box = (655,46,1154,529)    #creates bounding box for the image
    im = ImageGrab.grab()       #takes snapshot  
    im.save(os.getcwd() + '\\tempSnapshots\\full_snap__' + str(int(time.time())) + '.png' , 'PNG') #saves snapshot

def main():
    screenGrab()


if  __name__ == '__main__' :
    main()
