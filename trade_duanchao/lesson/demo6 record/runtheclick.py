#coding:gbk
from funlib import Active, GetPixelColour
import time,os,sys
import win32api
import win32con
import win32gui

MY_DIR = os.path.abspath(sys.path[0])
MOUSE_MICKEYS = 65535
keynum = {'A':65,'B':66,'C':67,'D':68,'E':69,
'F':70,'G':71,'H':72,'I':73,'J':74,'K':75,'L':76,'M':77,'N':78,'O':79,
'P':80,'Q':81,'R':82,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88,'Y':89,
'Z':90,'0':48,'1':49,'2':50,'3':51,'4':52,'5':53,'6':54,'7':55,'8':56,
'9':57,'F1':112,'F2':113,'F3':114,'F4':115,'F5':116,'F6':117,'F7':118,
'F8':119,'F9':120,'F10':121,'F11':122,'F12':123,'BACKSPACE':8,'TAB':9,
'CLEAR':12,'ENTER':13,'SHIFT':16,'CONTROL':17,'ALT':18,'CAPSLOCK':20,
'ESC':27,'SPACEBAR':32,'PAGEUP':33,'PAGEDOWN':34,'END':35,'HOME':36,
'LEFT':37,'UP':38,'RIGHT':39,'DOWN':40,'INSERT':45,'DELETE':46,'HELP':47,'NUMLOCK':114,'.':110,'/':111,'-':109
}
def PressKey(key):
    print key
    print keynum[key]
    win32api.keybd_event(keynum[key],0,0,0)
    win32api.keybd_event(keynum[key],0,win32con.KEYEVENTF_KEYUP,0)
    
def MoveMouse(_x, _y):
    '''
    @desc: 移动鼠标到桌面的指定位置 in: _x横坐标，_y纵坐标
    异常原因：1.参数不正确
              2.坐标值设置非法
    '''
    screenWidth = win32api.GetSystemMetrics(0)
    screenHeight = win32api.GetSystemMetrics(1)

    _x = _x % screenWidth * MOUSE_MICKEYS / screenWidth
    _y = _y % screenHeight * MOUSE_MICKEYS / screenHeight

    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE, _x, _y, 0, 0)
    
def MouseClick(_x, _y, _left=True, _dbClick=False):
    '''
    @desc: 在屏幕上的某个坐标(_x,_y)进行鼠标点击
    @param _left               in, 是否左键点击，默认为左键
    @param _dbClick            in, 是否双击，默认单击
    异常原因：1.参数不正确
              2.坐标值设置非法
    '''
    MoveMouse(_x, _y)
    time.sleep(0.05)

    if _left:
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
        if _dbClick:
            time.sleep(0.05)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    else:
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
        if _dbClick:
            time.sleep(0.05)
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
#ie.clickButton('Button')

def MoveMouseInsideHWnd(_hwnd, _x, _y, _mode):
    '''
    @desc: 移动鼠标到某窗口(_hWnd)下的某个相对坐标(_x,_y)
    异常原因：1.参数不正确
              2.坐标值设置非法
              3.窗口不存在
    '''
    x, y, w, h = GetWndRect(_hwnd)
    MoveMouse(x + _x, y + _y)
    
def GetWndRect(_hwnd):
    '''
    @desc: 获取window的x、y、width、height等信息 in: _hwnd窗口句柄 out: x, y, width, height
    异常原因：1.参数不正确
              2.待获取窗口已经被关闭
    '''
    left, top, right, bottom = win32gui.GetWindowRect(_hwnd)
    return left, top, right - left, bottom - top    
    
def MouseClickInsideHWnd(_hwnd, _x=0, _y=0, _left=True, _dbClick=False, _mode=0):
    '''
    @desc: 在某个窗口(_hWnd)下的某个相对坐标(_x,_y)进行鼠标点击操作
    @param _left               in, 是否左键点击，默认为左键
    @param _dbClick            in, 是否双击，默认单击
    异常原因：1.参数不正确
              2.坐标值设置非法
              3.窗口不存在
    '''
    if _mode == 0:
        x, y, w, h = GetWndRect(_hwnd) 
        if(_x == 0 and _y == 0):
            xx=x+w/2
            yy=y+h/2
            MouseClick(xx, yy, _left, _dbClick)
        else:
            xx=x+_x
            yy=y+_y
            MouseClick(xx, yy, _left, _dbClick)
    if _mode == 1:
        x, y, w, h = GetWndRect(_hwnd) 
        if(_x == 0 and _y == 0):
            xx=x+w/2
            yy=y+h/2
            for i in range(100):
                icolor=GetPixelColour(_hwnd, xx, yy)      
                MouseClick( xx, yy, _left, _dbClick)
                time.sleep(1)
                icolor2=GetPixelColour(_hwnd, xx, yy)
                if icolor != icolor2:
                    break     
        else:
            xx=x+w/2
            yy=y+h/2
            for i in range(10):
                icolor=GetPixelColour(_hwnd, xx, yy)      
                MouseClick( xx, yy, _left, _dbClick)
                time.sleep(1)
                icolor2=GetPixelColour(_hwnd, xx, yy)
                if icolor != icolor2:
                    break             
            else:
                print "按钮点击超时"
        
if __name__ == "__main__":
    print '当前目录：',MY_DIR
    win32api.ShellExecute(0,'open',MY_DIR+'\\Xenu.exe',None,None,1)
    xenuini = MY_DIR+'\\Xenu.ini'
    if os.path.isfile(xenuini):
        os.remove(xenuini)  #删除Xenu的配置文件
    time.sleep(3)
    f = open(MY_DIR+'\\script.ini', 'r')
    lines = f.readline()
    while(lines != ''):
        print '-------------------------',lines
        #title,classname,x,y,delaytime=lines.split('---')
        #print title,classname,x,y,delaytime
        #lines = f.readline()
        temp = (lines.strip('\n')).split('---')
        
        #ar={title,classname,x,y,delaytime}
        #ar={title,classname,x,y,delaytime}
        #print title,classname,x,y,delaytime
        #lines = f.readline()
        
        a = {"flag":'',"title":'', "classname":'', "x":"", "y":'', "delaytime":''}
        for i in range(len(temp)):
            a[a.keys()[i]] = temp[i]
        flag ,title, classname, x, y, delaytime = a.values()
        print flag,title, classname, x, y, delaytime
        if flag == 'Click':
            for i in range(3):
                try:            
                    handle = win32gui.FindWindow(classname, title)
                    if handle == 0:
                        handle = win32gui.FindWindow(None, title)
                    print title,handle
                    if handle !=0:
                        Active(handle)
                        MouseClickInsideHWnd(handle, int(x), int(y), True, True)
                        break
                    print "sleep %s s"% delaytime
                    time.sleep(int(delaytime))
                except Exception,e:
                    print "not find window====",e
                    continue
        if flag == 'Sendkey':
            for i in title:
                print 'sendkey--',i
                PressKey(str.upper(i))
        lines = f.readline()
        
        
        
        
        
