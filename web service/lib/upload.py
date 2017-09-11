upload_button = self.driver.find_element(*ImportLocators.Import_Order_Button)
upload_button.click()
upload_window = win32gui.GetForegroundWindow()
win32gui.SetForegroundWindow(upload_window)
str = file_path
str = str.decode(‘utf-8’).encode(‘gbk’) #转码
w.OpenClipboard()
w.EmptyClipboard()
w.SetClipboardData(win32con.CF_TEXT, str) #复制路径到剪贴板ctrl + c
w.CloseClipboard()
time.sleep(3)
SendKeys.SendKeys(“^+V”) #ctrl+v
SendKeys.SendKeys(“{ENTER}”)