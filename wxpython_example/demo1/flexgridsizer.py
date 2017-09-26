#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

import wx

class FlexGridSizer(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(290, 250))

        panel = wx.Panel(self, -1)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        fgs = wx.FlexGridSizer(3, 2, 9, 25)

        title = wx.StaticText(panel, -1, 'Title')
        author = wx.StaticText(panel, -1, 'Author')
        review = wx.StaticText(panel, -1, 'Review')

        tc1 = wx.TextCtrl(panel, -1)
        tc2 = wx.TextCtrl(panel, -1)
        tc3 = wx.TextCtrl(panel, -1, style=wx.TE_MULTILINE)

        fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author), (tc2, 1, wx.EXPAND),
            (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)])

        fgs.AddGrowableRow(2, 1)
        fgs.AddGrowableCol(1, 1)

        hbox.Add(fgs, 1, wx.ALL | wx.EXPAND, 15)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

app = wx.App()
FlexGridSizer(None, -1, 'FlexGridSizer')
app.MainLoop()