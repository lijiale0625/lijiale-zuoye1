#conding:utf8
'''############################################################################
#
#-->    AutoSweeper for Windows 7
#
#           Code By Broly
#           From http://www.dreamlikes.net
#
#-->    Testing environment:
#           Windows 7 Ultimate with SP1 (x86)
#           Python 2.7
#
#-->    Note:
#           1.Please make sure that you have open the MineSweeper.exe
#            program before running this script. Moreover, the 
#            MineSweeper.exe should be neither maximized nor minimized.
#    
#           2.When this script running, don't move your mouse.
#    
############################################################################
'''
# import
import win32api
import win32gui
import win32con
import win32process
import time,subprocess
from ctypes import *
#const variable
TH32CS_SNAPMODULE = 0x00000008
PROCESS_ALL_ACCESS = 0x1F0FFF
HWND_NOTOPMOST = -2
HWND_TOPMOST = -1
SWP_NOSIZE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
 
#struct
class MODULEENTRY32(Structure):
    _fields_ = [ ( 'dwSize' , c_long ) , 
                ( 'th32ModuleID' , c_long ),
                ( 'th32ProcessID' , c_long ),
                ( 'GlblcntUsage' , c_long ),
                ( 'ProccntUsage' , c_long ) ,
                ( 'modBaseAddr' , c_long ) ,
                ( 'modBaseSize' , c_long ) , 
                ( 'hModule' , c_void_p ) ,
                ( 'szModule' , c_char * 256 ),
                ( 'szExePath' , c_char * 260 ) ]
    
## LoadLibrary
kernel32 = windll.LoadLibrary("kernel32.dll")
## OpenProcess
OpenProcess = kernel32.OpenProcess
## CreateToolhelp32Snapshot
CreateToolhelp32Snapshot = kernel32.CreateToolhelp32Snapshot
CreateToolhelp32Snapshot.reltype = c_long
CreateToolhelp32Snapshot.argtypes = [ c_int , c_int ]
## Module32First
Module32First = kernel32.Module32First
Module32First.argtypes = [ c_void_p , POINTER(MODULEENTRY32) ]
Module32First.rettype = c_int
## Module32Next
Module32Next = kernel32.Module32Next
Module32Next.argtypes = [ c_void_p , POINTER(MODULEENTRY32) ]
Module32Next.rettype = c_int
## CloseHandle
CloseHandle = kernel32.CloseHandle
CloseHandle.argtypes = [ c_void_p ]
CloseHandle.rettype = c_int
## ReadProcessMemory
ReadProcessMemory = kernel32.ReadProcessMemory

#function
def autoSweep():
    hWnd = win32gui.FindWindow('Minesweeper',None)
    if hWnd == win32con.NULL:
        print 'Failed to find the Minesweeper\'s window.'
        return 1
        
        
    ThreadID,ProcessID = win32process.GetWindowThreadProcessId(hWnd)
    hProcess = OpenProcess(PROCESS_ALL_ACCESS,
                                    False ,
                                    ProcessID)
    if hProcess == win32con.NULL:
        print 'Failed to open the Minesweeper\'s process.'
        return 1
    
    
    hSnapshot = c_void_p(0)
    me32 = MODULEENTRY32()
    me32.dwSize = sizeof(MODULEENTRY32)
    
    hSnapshot = CreateToolhelp32Snapshot(TH32CS_SNAPMODULE, ProcessID)
    ret = Module32First(hSnapshot, pointer(me32))
    if ret == False:
        CloseHandle(hSnapshot)
        print 'Failed to enumerate the module'
        return 1
    
    while ret:
         if cmp(me32.szModule.lower(),'minesweeper.exe') == 0:
            mineBaseAddr = int(me32.modBaseAddr)
         ret = Module32Next(hSnapshot, pointer(me32))
        
    CloseHandle(hSnapshot)
    
    
    buffer = c_void_p(0)
    dwDate = c_void_p(0)
    topBaseAddr = mineBaseAddr + 0x868B4
    MineInfo = {'count' : 0,'row' : 0,'column' : 0}
    
    try:
        ReadProcessMemory(hProcess, topBaseAddr, pointer(buffer), 4, win32con.NULL)
        ReadProcessMemory(hProcess, buffer.value + 0x10, pointer(buffer), 4, win32con.NULL)
        ReadProcessMemory(hProcess, buffer.value + 0x04, pointer(dwDate), 4, win32con.NULL)
        MineInfo['count'] = dwDate.value
        ReadProcessMemory(hProcess, buffer.value + 0x08, pointer(dwDate), 4, win32con.NULL)
        MineInfo['row'] = dwDate.value
        ReadProcessMemory(hProcess, buffer.value + 0x0C, pointer(dwDate), 4, win32con.NULL)
        MineInfo['column'] = dwDate.value
    except:
        print 'Failed to read the Minesweeper\'s memory date.'
        return 1
    
    
    win32gui.SetWindowPos(hWnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE)
    cleft, ctop, cright, cbottom = win32gui.GetClientRect(hWnd)

    if cright<=0 or cbottom<=0:
        print 'Failed to get the rectangle of th Minesweeper\'s window.'
        return 1
        
    
    x, y = win32gui.ClientToScreen(hWnd,(cleft,ctop))
    edge = cright/(MineInfo['column'] + 4) + 1
    
    originX = edge*2 + edge/2 + x
    originY = (cbottom-MineInfo['row']*edge)/2 + edge/2 + y
    
    
    win32api.SetCursorPos((originX,originY))
    
    time.sleep(0.05)
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP,0,0,0,0)
    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP,0,0,0,0)
                
    time.sleep(1)
    
    ReadProcessMemory(hProcess, buffer.value + 0x44, pointer(buffer), 4, win32con.NULL)
    ReadProcessMemory(hProcess, buffer.value + 0x0C, pointer(buffer), 4, win32con.NULL)
    
    
    buffer2 = c_void_p(0)
    dwDate2 = c_void_p(0)
    bFlag = [[0 for col in range(MineInfo['row'])] for row in range(MineInfo['column'])]
    
    
    for i in range(0, MineInfo['column']):
        ReadProcessMemory(hProcess, buffer.value + 4*i, pointer(buffer2), 4, win32con.NULL)
        ReadProcessMemory(hProcess, buffer2.value + 0x0C, pointer(buffer2), 4, win32con.NULL)    
        for j in range(0, MineInfo['row']):
            ReadProcessMemory(hProcess, buffer2.value + j, pointer(dwDate2), 1, win32con.NULL)         
            if dwDate2.value==None:
                bFlag[i][j] = 0
            else:
                bFlag[i][j] = dwDate2.value
                print i,j,bFlag[i][j]
                
                
    CloseHandle(hProcess)
    
    Count = 0
    for i in range(0, MineInfo['row']):
        for j in range(0, MineInfo['column']):
            if win32gui.FindWindow('Minesweeper',None) != win32con.NULL:
                win32api.SetCursorPos((originX+j*edge,originY+i*edge))
                if bFlag[j][i] == 0:
                    win32api.mouse_event(MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP,0,0,0,0)
                    Count += 1
                else:
                    if Count == (MineInfo['row']*MineInfo['column']-MineInfo['count']):
                        break
                    win32api.mouse_event(MOUSEEVENTF_RIGHTDOWN|MOUSEEVENTF_RIGHTUP,0,0,0,0)
    
                time.sleep(.015)
            else:
                print 'Failed to find the Minesweeper\'s window.'
                return 1
    
    print hWnd
    win32gui.SetWindowPos(hWnd, HWND_NOTOPMOST, 0, 0, 0, 0, SWP_NOSIZE)
    return 0

# main
if __name__ == '__main__' :
    print __doc__
    print '\n\n'
    subprocess.Popen("C:\Program Files\Microsoft Games\Minesweeper\MineSweeper.exe")
    time.sleep(2)
    bSuccess = autoSweep()
    if bSuccess == 1:
        input('Press ENTER to exit.')