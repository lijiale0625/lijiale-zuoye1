#coding:gbk
#from funLib_byronxu import funQQPCMgr_FindWindowVague

from funlib import *
import pyHook
import pythoncom
import sys,os
import time
from pickle import FALSE

MY_DIR = os.path.abspath(sys.path[0])
timestamp = time.time()

def onKeyboardEvent(event): 
    eventtemp = str(event.Key)
    stamptemp = time.time()
    delaytime = stamptemp - timestamp
    timestamp = stamptemp
    print 'event============', eventtemp, '====', delaytime
    #if delaytime <= 0.48 or delaytime >= 0.52:
    #    print str(eventtemp)
    if eventtemp == "F":
        print "kaishixieru "
        global timestamp
        stamptemp = time.time()
        delaytime = stamptemp - timestamp
        timestamp = stamptemp
        writetotxt(getmouseinfo(), delaytime)#д�ű�
        print getmouseinfo()
        return True
    elif eventtemp == "CC":
        print "nononon "
        sys.exit(0)
    else:
        return True
 
def onMouseEvent(event):
    eventtemp = str(event.MessageName)
    #if delaytime <= 0.48 or delaytime >= 0.52:
    #    print str(eventtemp)
    #print "===========",eventtemp
    if eventtemp == "mouse left up":
        global timestamp
        stamptemp = time.time()
        delaytime = stamptemp - timestamp
        print "kaishixieru ====",delaytime
        timestamp = stamptemp
        try:
            writetotxt(getmouseinfo(), delaytime)#д�ű�
        except:
            print "д��ʧ��"
        return True
    elif eventtemp == "mouse right up":
        print "Eeeeeeeeeeeeeeeeeeeeend the record "
        sys.exit(0)
        #if temp==False: temp=True
        #else:temp=False
        return True
    else:
        return True
 
def getUserPushKey():
    #����hook���
    hm = pyHook.HookManager() 
    #��ؼ���ffff
    hm.MouseAll= onMouseEvent
    hm.KeyDown=onKeyboardEvent
    #hm.HookKeyboard()
    hm.HookMouse()
    hm.HookKeyboard()
    pythoncom.PumpMessages()  
    return True
  
def writetotxt((t, c, x,y), z):
    #д��TXT   
    txt = open(MY_DIR+'\\script.ini', 'a')
    txt.writelines('Click' + '---'+ t + '---' + c + '---' + str(x)+"---"+str(y) + '---' + str(int(z) + 1)  + '\n')
    txt.close()
    print t, c, x,y, int(z) + 1
    return True

if __name__ == "__main__":
    print "====start to record===="
    print " press 'mouse left' to record the coordinate int the ForegroundWindow "
    print " press 'mouse right' to exit"
    getUserPushKey()

    
    
    
