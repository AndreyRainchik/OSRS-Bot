# Globals
#---------------
x_pad = 0 #27
y_pad = 0 #258

import ImageGrab
import os
import time
import win32api,win32con

def screenGrab():
    box = ()
    #box = (x_pad+1,y_pad+1,x_pad+640,y_pad+480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap_' + str(int(time.time())) + '.png', 'PNG')

def mousePos(cord):
    win32api.SetCursorPos((cord[0],cord[1]))

def get_cords():
    x,y = win32api.GetCursorPos()
    print x,y

def main():
    #screenGrab()
    get_cords()
    mousePos((576,534))

if __name__ == '__main__':
    main()

