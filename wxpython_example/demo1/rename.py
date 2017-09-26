
# -*- coding:UTF-8 -*-
import wx

class Rename(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(320, 130))

        panel = wx.Panel(self, -1)
        sizer = wx.GridBagSizer(4, 4)

        text = wx.StaticText(panel, -1, 'Rename To')
        sizer.Add(text, (0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)

        tc = wx.TextCtrl(panel, -1)
        sizer.Add(tc, (1, 0), (1, 5), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        buttonOk = wx.Button(panel, -1, 'Ok', size=(90, 28))
        buttonClose = wx.Button(panel, -1, 'Close', size=(90, 28))
        sizer.Add(buttonOk, (3, 3))
        sizer.Add(buttonClose, (3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizerAndFit(sizer)
        self.Centre()
        self.Show(True)

app = wx.App()
Rename(None, -1, 'Rename Dialog')
app.MainLoop()

 # text = wx.StaticText(panel, -1, 'Rename To')
 # sizer.Add(text, (0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
 #       将文本 “Rename to”放于窗口的左上角，因此将 pos 指定为 (0,0)。
 #
 # tc = wx.TextCtrl(panel, -1)
 # sizer.Add(tc, (1, 0), (1, 5), wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
 #       将文本输入框放于第二行的始端(1,0) ── 紧记，是用 0 开始计数的。同时文本框跨越1行5列(1,5)。
 #
 # sizer.Add(buttonOk, (3, 3))
 # sizer.Add(buttonClose, (3, 4), flag=wx.RIGHT | wx.BOTTOM, border=5)
 #       在第4行放置两个按钮（第三行我们空着），分别放于第4列和第5列。