#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

import wx

class Sizer(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 180))

        menubar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

        wx.TextCtrl(self, -1)

        self.Centre()
        self.Show(True)

app = wx.App(0)
Sizer(None, -1,'')
app.MainLoop()