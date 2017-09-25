#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

import wx
from method import get_problem, get_answer,a, problem_num

class MultiTextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"抽题系统",
                          size=(600, 600))
        panel = wx.Panel(self, -1)
        # panel.SetBackgroundColour('#4f5049')
        # font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font = wx.Font(12, wx.ROMAN, wx.NORMAL, wx.BOLD, False)
        font.SetPointSize(16)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add((-1, 15))
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label=u'题目')
        st1.SetFont(font)

        hbox1.Add(st1, flag=wx.RIGHT, border=10)
        self.tc = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_READONLY)
        self.tc.SetFont(font)
        hbox1.Add(self.tc, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox1, proportion=2, flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)

        vbox.Add((-1, 15))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label=u'答案')
        st2.SetFont(font)
        hbox3.Add(st2,flag=wx.RIGHT, border=10)
        self.tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_RICH2 | wx.TE_READONLY)
        self.tc2.SetFont(font)
        hbox3.Add(self.tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.EXPAND,border=10)

        vbox.Add((-1, 20))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        btn1 = wx.Button(panel, label=u'随机抽题', size=(110, 50))
        btn1.SetFont(font)
        hbox5.Add(btn1)
        btn2 = wx.Button(panel, label=u'显示答案', size=(110, 50))
        btn2.SetFont(font)
        hbox5.Add(btn2, flag=wx.LEFT | wx.BOTTOM, border=50)
        vbox.Add(hbox5, flag=wx.ALIGN_CENTER_HORIZONTAL  | wx.RIGHT, border=10)

        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, self.getProblem, btn1)
        self.Bind(wx.EVT_BUTTON, self.getAnswer, btn2)
        self.b = 0

    def getProblem(self, event):
        self.b = self.b+1
        if self.b > problem_num:
            self.Close()
        self.tc.Clear()
        self.tc2.Clear()
        self.tc.AppendText(get_problem())


    def getAnswer(self, event):
        self.tc2.Clear()
        self.tc2.AppendText(get_answer())


class MyApp(wx.App):
    def __init__(self):
        # 重构__init__方法，将错误信息重定位到文件中;
        # 默认redirect=True，输出到StdOut或StdError;
        # 为防止程序因错误一闪而过无法捕捉信息，可在
        # 控制台中使用python -i example.py来运行程序。
        wx.App.__init__(self, redirect=False, filename=r"./IO.txt")

    def OnInit(self):
        frame = MultiTextFrame()
        frame.Show(True)
        return True


def main():
    app = MyApp()
    app.MainLoop()


if __name__ == "__main__":
    main()