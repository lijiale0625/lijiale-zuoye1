#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

import wx

class GridSizer(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 250))

        menubar = wx.MenuBar()
        file = wx.Menu()
        file.Append(1, '&Quit', 'Exit Calculator')
        menubar.Append(file, '&File')
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_MENU, self.OnClose, id=1)

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.display = wx.TextCtrl(self, -1,'',  style=wx.TE_RIGHT)
        sizer.Add(self.display, 0, wx.EXPAND | wx.TOP | wx.BOTTOM, 4)
        gs = wx.GridSizer(4, 4, 3, 3) #这是 wx.GridSizer 的构造函数。分别定义布局表格的行列数以及行列的大小。
        # 注意，我们在Bck和Close按钮之间放置一个空白的wx.StaticText，这是布局上的一个有用技巧。
        # 例子中的AddMany()方法可以一次过放置多个widgets到sizer上。
        # AddMany(listitems)widgets放置在布局表格上是按一定顺序的，先放满第一行，再放置第二行…如此类推。
        gs.AddMany( [(wx.Button(self, -1, 'Cls'), 0, wx.EXPAND),
            (wx.Button(self, -1, 'Bck'), 0, wx.EXPAND),
            (wx.StaticText(self, -1, ''), 0, wx.EXPAND),
            (wx.Button(self, -1, 'Close'), 0, wx.EXPAND),
            (wx.Button(self, -1, '7'), 0, wx.EXPAND),
            (wx.Button(self, -1, '8'), 0, wx.EXPAND),
            (wx.Button(self, -1, '9'), 0, wx.EXPAND),
            (wx.Button(self, -1, '/'), 0, wx.EXPAND),
            (wx.Button(self, -1, '4'), 0, wx.EXPAND),
            (wx.Button(self, -1, '5'), 0, wx.EXPAND),
            (wx.Button(self, -1, '6'), 0, wx.EXPAND),
            (wx.Button(self, -1, '*'), 0, wx.EXPAND),
            (wx.Button(self, -1, '1'), 0, wx.EXPAND),
            (wx.Button(self, -1, '2'), 0, wx.EXPAND),
            (wx.Button(self, -1, '3'), 0, wx.EXPAND),
            (wx.Button(self, -1, '-'), 0, wx.EXPAND),
            (wx.Button(self, -1, '0'), 0, wx.EXPAND),
            (wx.Button(self, -1, '.'), 0, wx.EXPAND),
            (wx.Button(self, -1, '='), 0, wx.EXPAND),
            (wx.Button(self, -1, '+'), 0, wx.EXPAND) ])

        sizer.Add(gs, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Centre()
        self.Show(True)

    def OnClose(self, event):
        self.Close()

app = wx.App()
GridSizer(None, -1, 'GridSizer')
app.MainLoop()