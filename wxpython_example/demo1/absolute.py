#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

import wx

class Absolute(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(250, 180))
        panel = wx.Panel(self, -1)

        menubar = wx.MenuBar()
        file = wx.Menu()
        edit = wx.Menu()
        help = wx.Menu()

        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)

        wx.TextCtrl(panel, -1, pos=(-1, -1), size=(250, 150))

        self.Centre()
        self.Show(True)

app = wx.App(0)
Absolute(None, -1,'')
app.MainLoop()