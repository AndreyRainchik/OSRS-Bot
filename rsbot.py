__author__ = 'Andrey'

import ImageOps
from numpy import *
import ImageGrab
import os
import time
import win32api,win32con
import random

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def rightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print 'left down'

def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print 'left up'

def mousePos(cord):
    #win32api.SetCursorPos((cord[0],cord[1]))
    nx = cord[0]*65535/win32api.GetSystemMetrics(0)
    ny = cord[1]*65535/win32api.GetSystemMetrics(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,nx,ny)

def get_cords():
    x,y = win32api.GetCursorPos()
    print x,y

def randWait():
    seed = random.randint(20,25)/float(10)
    return seed

class Cord:
    offset = -5

    wine1 = (1076,540-offset)
    wine2 = (1117,542-offset)
    wine3 = (1161,542-offset)
    wine4 = (1203,541-offset)
    wine5 = (1076,577-offset)
    wine6 = (1119,577-offset)
    wine7 = (1162,578-offset)
    wine8 = (1203,576-offset)
    wine9 = (1077,611-offset)
    wine10 = (1118,615-offset)
    wine11 = (1162,613-offset)
    wine12 = (1203,618-offset)
    wine13 = (1076,651-offset)
    wine14 = (1118,650-offset)
    wine15 = (1159,652-offset)
    wine16 = (1206,651-offset)
    wine17 = (1076,685-offset)
    wine18 = (1119,689-offset)
    wine19 = (1161,687-offset)
    wine20 = (1203,687-offset)
    wine21 = (1076,722-offset)
    wine22 = (1118,724-offset)
    wine23 = (1162,723-offset)
    wine24 = (1202,725-offset)
    wine25 = (1076,759-offset)
    wine26 = (1120,758-offset)
    wine27 = (1161,759-offset)
    wine28 = (1202,761-offset)
    bank = (645,481-offset)
    bankFull = (674,197)
    bankEmpty = (674,169)
    bankClose = (737,55)

def emptySlot():
    leftClick()
    wait = randWait()
    time.sleep(wait)

def emptyWine():
    Cord.wine1 = (Cord.wine1[0]+random.randint(-5,5),Cord.wine1[1]+random.randint(-5,5))
    mousePos(Cord.wine1)
    emptySlot()
    Cord.wine2 = (Cord.wine2[0]+random.randint(-5,5),Cord.wine2[1]+random.randint(-5,5))
    mousePos(Cord.wine2)
    emptySlot()
    Cord.wine3 = (Cord.wine3[0]+random.randint(-5,5),Cord.wine3[1]+random.randint(-5,5))
    mousePos(Cord.wine3)
    emptySlot()
    Cord.wine4 = (Cord.wine4[0]+random.randint(-5,5),Cord.wine4[1]+random.randint(-5,5))
    mousePos(Cord.wine4)
    emptySlot()
    Cord.wine8 = (Cord.wine8[0]+random.randint(-5,5),Cord.wine8[1]+random.randint(-5,5))
    mousePos(Cord.wine8)
    emptySlot()
    Cord.wine7 = (Cord.wine7[0]+random.randint(-5,5),Cord.wine7[1]+random.randint(-5,5))
    mousePos(Cord.wine7)
    emptySlot()
    Cord.wine6 = (Cord.wine6[0]+random.randint(-5,5),Cord.wine6[1]+random.randint(-5,5))
    mousePos(Cord.wine6)
    emptySlot()
    Cord.wine5 = (Cord.wine5[0]+random.randint(-5,5),Cord.wine5[1]+random.randint(-5,5))
    mousePos(Cord.wine5)
    emptySlot()
    Cord.wine9 = (Cord.wine9[0]+random.randint(-5,5),Cord.wine9[1]+random.randint(-5,5))
    mousePos(Cord.wine9)
    emptySlot()
    Cord.wine10 = (Cord.wine10[0]+random.randint(-5,5),Cord.wine10[1]+random.randint(-5,5))
    mousePos(Cord.wine10)
    emptySlot()
    Cord.wine11 = (Cord.wine11[0]+random.randint(-5,5),Cord.wine11[1]+random.randint(-5,5))
    mousePos(Cord.wine11)
    emptySlot()
    Cord.wine12 = (Cord.wine12[0]+random.randint(-5,5),Cord.wine12[1]+random.randint(-5,5))
    mousePos(Cord.wine12)
    emptySlot()
    Cord.wine16 = (Cord.wine16[0]+random.randint(-5,5),Cord.wine16[1]+random.randint(-5,5))
    mousePos(Cord.wine16)
    emptySlot()
    Cord.wine15 = (Cord.wine15[0]+random.randint(-5,5),Cord.wine15[1]+random.randint(-5,5))
    mousePos(Cord.wine15)
    emptySlot()
    Cord.wine14 = (Cord.wine14[0]+random.randint(-5,5),Cord.wine14[1]+random.randint(-5,5))
    mousePos(Cord.wine14)
    emptySlot()
    Cord.wine13 = (Cord.wine13[0]+random.randint(-5,5),Cord.wine13[1]+random.randint(-5,5))
    mousePos(Cord.wine13)
    emptySlot()
    Cord.wine17 = (Cord.wine17[0]+random.randint(-5,5),Cord.wine17[1]+random.randint(-5,5))
    mousePos(Cord.wine17)
    emptySlot()
    Cord.wine18 = (Cord.wine18[0]+random.randint(-5,5),Cord.wine18[1]+random.randint(-5,5))
    mousePos(Cord.wine18)
    emptySlot()
    Cord.wine19 = (Cord.wine19[0]+random.randint(-5,5),Cord.wine19[1]+random.randint(-5,5))
    mousePos(Cord.wine19)
    emptySlot()
    Cord.wine20 = (Cord.wine20[0]+random.randint(-5,5),Cord.wine20[1]+random.randint(-5,5))
    mousePos(Cord.wine20)
    emptySlot()
    Cord.wine24 = (Cord.wine24[0]+random.randint(-5,5),Cord.wine24[1]+random.randint(-5,5))
    mousePos(Cord.wine24)
    emptySlot()
    Cord.wine23 = (Cord.wine23[0]+random.randint(-5,5),Cord.wine23[1]+random.randint(-5,5))
    mousePos(Cord.wine23)
    emptySlot()
    Cord.wine22 = (Cord.wine22[0]+random.randint(-5,5),Cord.wine22[1]+random.randint(-5,5))
    mousePos(Cord.wine22)
    emptySlot()
    Cord.wine21 = (Cord.wine21[0]+random.randint(-5,5),Cord.wine21[1]+random.randint(-5,5))
    mousePos(Cord.wine21)
    emptySlot()
    Cord.wine25 = (Cord.wine25[0]+random.randint(-5,5),Cord.wine25[1]+random.randint(-5,5))
    mousePos(Cord.wine25)
    emptySlot()
    Cord.wine26 = (Cord.wine26[0]+random.randint(-5,5),Cord.wine26[1]+random.randint(-5,5))
    mousePos(Cord.wine26)
    emptySlot()
    Cord.wine27 = (Cord.wine27[0]+random.randint(-5,5),Cord.wine27[1]+random.randint(-5,5))
    mousePos(Cord.wine27)
    emptySlot()
    Cord.wine28 = (Cord.wine28[0]+random.randint(-5,5),Cord.wine28[1]+random.randint(-5,5))
    mousePos(Cord.wine28)
    emptySlot()

def bank():
    Cord.bank = (Cord.bank[0]+(random.randint(-5,5)),Cord.bank[1]+random.randint(-5,5)-Cord.offset)
    mousePos(Cord.bank)
    time.sleep(random.randint(6,16)/float(10))
    leftClick()
    #Cord.bank = (Cord.bank[0]+(random.randint(-5,5)),Cord.bank[1]+random.randint(-3,3)+30)
    #mousePos(Cord.bank)
    #time.sleep(random.randint(6,16)/float(10))
    #leftClick()
    time.sleep(random.randint(15,25)/float(10))
    Cord.wine1 = (Cord.wine1[0]+random.randint(-5,5),Cord.wine1[1]+random.randint(-5,5))
    mousePos(Cord.wine1)
    time.sleep(random.randint(6,16)/float(10))
    rightClick()
    Cord.wine1 = (Cord.wine1[0]+random.randint(-5,5),Cord.wine1[1]+random.randint(-1,1)+100)
    mousePos(Cord.wine1)
    time.sleep(random.randint(6,16)/float(10))
    leftClick()
    time.sleep(random.randint(15,25)/float(10))

    Cord.bankFull = (Cord.bankFull[0]+random.randint(-5,5),Cord.bankFull[1]+random.randint(-5,5))
    mousePos(Cord.bankFull)
    rightClick()
    time.sleep(random.randint(6,16)/float(10))
    Cord.bankFull = (Cord.bankFull[0]+random.randint(-5,5),Cord.bankFull[1]+100)
    mousePos(Cord.bankFull)
    time.sleep(random.randint(6,16)/float(10))
    leftClick()
    time.sleep(random.randint(15,25)/float(10))
    Cord.bankClose = (Cord.bankClose[0]+random.randint(-3,3),Cord.bankClose[1]+random.randint(-3,3))
    leftClick()

def main():
    #get_cords()
    cont = 1
    while (cont == 1):
        emptyWine()
        bank()
        cont = input("Continue? 1=yes, 2=no")

if __name__ == '__main__':
    main()