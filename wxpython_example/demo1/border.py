#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

import wx

class Border(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 200))

        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('#4f5049')  #4f5049
        vbox = wx.BoxSizer(wx.VERTICAL)
        #vbox = wx.BoxSizer(wx.HORIZONTAL)

        midPan = wx.Panel(panel, -1)
        midPan.SetBackgroundColour('#ededed') #ededed

        vbox.Add(midPan, 1, wx.EXPAND | wx.ALL, 20)  #上面的代码将为 midPan 面板的四边添加宽度为20像素的边框。
        panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

app = wx.App()
Border(None, -1,'')
app.MainLoop()