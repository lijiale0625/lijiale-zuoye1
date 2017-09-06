#coding:gbk
import ctypes
import win32api
import win32con
import win32gui
import win32process

def Active(_hwnd):
    try:
        win32gui.SetWindowPos(_hwnd, -1, 0, 0, 0, 0, 1 | 2)
        curWnd = ctypes.windll.user32.GetForegroundWindow()
        if(curWnd == _hwnd):
            return
        curId = win32process.GetWindowThreadProcessId(curWnd)[0]
        targetid = win32process.GetWindowThreadProcessId(_hwnd)[0]
        if(targetid == curId):
            win32gui.SetForegroundWindow(_hwnd)
        else:
            ctypes.windll.user32.AttachThreadInput(curId, targetid, True)
            win32gui.SetForegroundWindow(_hwnd)
            win32gui.BringWindowToTop(_hwnd)
            ctypes.windll.user32.AttachThreadInput(curId, targetid, False)
        if(win32gui.IsIconic(_hwnd)):
            win32gui.ShowWindow(_hwnd, win32con.SW_RESTORE)
        else:
            win32gui.ShowWindow(_hwnd, win32con.SW_SHOW)
    except:
        pass      
        
def getmouseinfo():
    ForegroundWindowHandle = win32gui.GetForegroundWindow()
#    Active(ForegroundWindowHandle)
    print "ForegroundWindowHandle========",ForegroundWindowHandle
    title = win32gui.GetWindowText(ForegroundWindowHandle)
    classname = win32gui.GetClassName(ForegroundWindowHandle)
    (x_, y_, w_, z_) = win32gui.GetWindowRect(ForegroundWindowHandle)
    (x, y) = win32gui.GetCursorPos()
    x_insidewindow = x - x_
    y_insidewindow = y - y_
    return title, classname, x_insidewindow, y_insidewindow

def GetPixelColour(hwnd , i_x, i_y):
    GetPosWnd(hwnd , i_x, i_y)
    Active(hwnd)
    i_x, i_y = win32gui.GetCursorPos()
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def GetColor(i_x,i_y):
    i_desktop_window_id = win32gui.GetDesktopWindow()
    i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
    long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
    i_colour = int(long_colour)
    print "icolour====",i_colour
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

def GetPosWnd(hwnd, LShift, RShift):
    Active(hwnd)
    (left, top, right, bottom) = win32gui.GetWindowRect(hwnd)
    win32api.SetCursorPos((left + LShift, top + RShift))
    point=win32api.GetCursorPos()
    return win32gui.WindowFromPoint(point)