#coding=utf-8
import wx
import dubbo_telnet
import json

# 静态文本    对象名，显示名称，x,y
static_text_data =(('', u"Dubbo接口测试工具", 310, 29),('', u"主机地址：", 310, 80),('', u"Dubbo端口：", 850, 80),
                   ('', u"接口：", 310, 140),('', u"方法：", 850, 140),('', u"请求参数", 310, 180),('', u"响应", 310, 500),
                   ('response_time', "", 1188, 500))

# 输入框 对象名，类型，x,y,size_x,size_2
input_box_data = (('host','single', 370, 80, 393, -1),('port','single', 920, 80, 87, -1),('body','', 310, 230, 1000, 250),
                  ('response','', 310, 530, 1000, 250),('remark','', 50, 29, 249, 750))  # remark

# 下拉列表 保存对象名， x,y,size_x1,size_y,data
choice_list_data =(('interface',350, 140, 490, 100, []),('method',888, 140, 250, 100, []))

# 单选按钮 显示名称，x,y
# radio_button_data =((u'普通类型数据', 435, 200),(u'自由类型数据', 625, 200))

# 错误码
error_code ={"box-00000":{"title":u"提示信息","message":u"工具被玩坏了，请联系开发者。"}, "box-00001":{"title":u"提示信息","message":u"地址为空，请输入主机地址！"},
             "box-00002":{"title":u"提示信息","message":u"Dubbo端口为空，请输入Dubbo端口！"}, "box-00003":{"title":u"提示信息","message":u"请选择需要测试的接口。"},
             "box-00004":{"title":u"提示信息","message":u"请选择需要测试的方法。"}, "box-00005":{"title":u"提示信息","message":u"请输入请求数据。"},
             "box-00006":{"title":u"提示信息","message":u"请先连接服务器。"}, "box-00007":{"title":u"提示信息","message":u"连接已断开，请重新获取连接！"}}

tips_txt=u'注意事项：\n本工具只适用于dubbo版本2.0.5已上。\n\n使用说明:\n1、填写主机地址和dubbo的端口，然后点击“获取连接”；\n2、选择需要测试的接口和方法；\n3、填写请求参数；\n' \
         u'4、点击“send”。\n\n\n工具运行环境：python 2.7版本；\n依赖包：json 、wx_python；\n\n\n示例1：\ndubbo接口的方法只定义传一个json数据的情况；\ndemo1(batchFreezeDto) \n' \
         u'填写请求格式：{"key1":"value1","key2":"value2"}\n注意：传入参数，按实际情况填写。\n\n示例2：\ndubbo接口的方法只定义传一个变量的情况；\ndemo2(String outTradeNo)\n' \
         u'填写请求格式：\n"8582855"\n注意：数据是否加引号，需根据变量定义类型填写。\n\n示例3：\ndubbo接口的方法定义多个json数据的情况；\ndemo3(accountReqDto, subAccountReqDto, bankCardReqDto)' \
         u'\n填写请求格式：{"key1":"value1","key2":"value1"},{"key11":"value11","key22":"value22"},{"key33":"value33","key33":"value33"}\n注意：传入多个参数时，使用 , 号分隔。'

class interface(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u'Dubbo接口测试工具_V1.0', size=(1350, 835))
        # self.panel = wx.Panel(self, -1)         # 不带滚动窗口
        self.panel = wx.ScrolledWindow(self, -1) # 带滚动窗口
        self.panel.SetScrollbars(1, 30, 0, 20)   # 30*60=1800
        self.static_text_object = self.static_text_show(static_text_data)  # 显示静态文本
        self.input_box_object = self.input_box(input_box_data)             # 输入框
        self.new_button(self.get_button_data())                            # 普通按钮
        self.all_switch_object = self.new_toggle_button(self.toggle_button_data())  # 开关按钮
        # self.radio_object = self.new_radio_button(radio_button_data)       # 显示单选按钮(暂时不用)
        self.choice_object =self.new_choice(choice_list_data)      # 下拉列表
        self.connection_instance=None                              # 连接dubbo实例
        self.service_bind_trigger()                                # 绑定下拉列表方法
        self.input_box_object["remark"].SetValue(tips_txt)

    # 静态文本
    def static_text_show(self, data):
        static_text_object = {}
        for sign, name, pos1, pos2 in data:
            if sign == '':
                wx.StaticText(self.panel, -1, name, (pos1, pos2))
            else:
                static_text_object[sign] = wx.StaticText(self.panel, -1, name, (pos1, pos2))
        return static_text_object

    # single 表示单行输入框， 否则多行输入框
    def input_box(self,  data):
        object_box={}
        for name, mode, pos1, pos2, size1, size2 in data:
            if mode == 'single':
                object = wx.TextCtrl(self.panel, -1, pos=(pos1, pos2), size=(size1, size2))
            else:
                object = wx.TextCtrl(self.panel, -1, pos=(pos1, pos2), size=(size1, size2), style=wx.TE_MULTILINE | wx.TE_RICH2)
            object.SetInsertionPoint(0)
            object_box[name] =object
        return object_box

    # 下拉列表
    def new_choice(self, data):
        choice_list = {}
        for name, pos1, pos2, size_1, size_2, list_data in data:
            choice_list[name] = wx.Choice(self.panel, -1, (pos1, pos2),(size_1,size_2), choices=list_data)
        return choice_list

    # 按钮
    def new_button(self, data):
        for button_name, pos1, pos2, button_methods in data:
            button_object = wx.Button(self.panel, -1, button_name, pos=(pos1, pos2))
            self.Bind(wx.EVT_BUTTON, button_methods, button_object)

    def show_name(self, data):
        cache = {}
        list_data = data.split(';')
        for i in range(len(list_data)):
            cache[i] =list_data[i]
        return cache

    # 开关  ("默认显示名称", 默认状态, 开关唯一标识, x, y, 绑定方法)
    def new_toggle_button(self, data):
        switch_object = {}
        for state_all, button_name, state, pos1, pos2, button_methods in data:
            cache = {}
            button_object = wx.ToggleButton(self.panel, -1, button_name, pos=(pos1, pos2))
            self.Bind(wx.EVT_TOGGLEBUTTON, button_methods, button_object)
            cache['button_object'] = button_object
            cache['state'] = state
            cache['info'] = self.show_name(state_all)
            if state == 1:
                button_object.SetValue(True)
            switch_object[button_object.GetId()] = cache
        return switch_object

    #创建一组的单按钮
    def new_radio_box(self, data):
        radio_box_object = {}
        for radio_name, pos1, pos2, sample_list, num in data:
            print radio_name, pos1, pos2, sample_list, num
            radio_box_object[radio_name] = wx.RadioBox(self.panel, -1,'',(pos1, pos2), wx.DefaultSize,sample_list, num,\
                                                       wx.RA_SPECIFY_COLS|wx.NO_BORDER)
        return radio_box_object

    # 创建单选按钮
    def new_radio_button(self, data):
        radio_button_object = {}
        first =1
        for show_name, pos1, pos2 in data:
            if first ==1:
                radio_button_object[show_name] = wx.RadioButton(self.panel, -1, show_name, pos=(pos1, pos2),style=wx.RB_GROUP)
                first =0
            else:
                radio_button_object[show_name] = wx.RadioButton(self.panel, -1, show_name, pos=(pos1, pos2))
        return radio_button_object

    # 按钮数据
    def get_button_data(self):
        # 显示名称，x,y,绑定方法
        button_data = [("send", 1150, 140, self.send)]#("reload", 1230, 140, self.reload)
        return button_data

    # 开关数据 ('开关所有状态', "默认显示名称", 默认状态, 开关唯一标识, x, y, 绑定方法)
    def toggle_button_data(self):
        button_data = [(u'已连接;获取连接', u"获取连接", 1, 1150, 80, self.show_switch)]
        return button_data

    # 更新开关状态
    def show_switch(self, event):
        if self.check_state('connection') == '0':
            return
        switch_info = self.all_switch_object[event.GetEventObject().GetId()]
        switch_show = switch_info['info']
        #print u'调用开关id:',event.GetEventObject().GetId()
        print u'连接开关按钮状态:',switch_info['button_object'].GetValue()
        if switch_info['button_object'].GetValue() and self.connection_instance is not None: #调用断开连接
           self.connection_instance.disconnect()
           self.connection_instance = None
           self.choice_object['interface'].Clear()
           self.choice_object['method'].Clear()
        else:   # 连成功
            host = self.input_box_object["host"].GetValue().strip()
            port = self.input_box_object["port"].GetValue().strip()
            state, info = self.connection(host, port)
            if state == '1':
                all_service_list, info = self.connection_instance.do('ls')
                self.choice_object['interface'].Clear()
                for service in all_service_list[:-1]:
                    self.choice_object['interface'].Append(service)
            else:
                self.tips(u'提示信息', info)
                switch_info['button_object'].SetValue(True)  #False
                return
        if switch_info['button_object'].GetValue():
            switch_info['state'] = 1
            switch_info['button_object'].SetLabel(switch_show[1])
            switch_info['button_object'].SetBackgroundColour('Red')
        else:
            switch_info['state'] = 0
            switch_info['button_object'].SetLabel(switch_show[0])
            switch_info['button_object'].SetBackgroundColour('Green')
        self.all_switch_object['case_switch'] = switch_info

    # 窗口切换
    def OnRadio(self,event):
        if self.selectedText:
            self.selectedText.Enable(False)
        label_name = event.GetEventObject().GetLabel()
        one_correlate_data = self.correlate_data[label_name]
        print 'one_correlate_data:',one_correlate_data
        text = one_correlate_data[one_correlate_data['name']]
        text.Enable(True)
        self.selectedText = text

    # 列表绑定响应事件
    def service_bind_trigger(self):
        self.Bind(wx.EVT_CHOICE, self.refresh_method_display, self.choice_object['interface'])

    # 连接服务器
    def connection(self, host, port):
        conn = dubbo_telnet.dubbo(str(host), int(port))  # 初始化dubbo对象
        conn.set_connect_timeout(10)    # 设置telnet连接超时时间
        conn.set_encoding('gbk')        # 设置dubbo服务返回响应的编码
        state, info = conn.connection_telnet()
        if state =='1':
            self.connection_instance = conn
            return state, info
        else:
            return state, info

    # 检查是否连接、接口、方法、请求参数是否填写
    def check_state(self, check_object=''):
        host = self.input_box_object["host"].GetValue().strip()
        port = self.input_box_object["port"].GetValue().strip()
        interface_data = self.choice_object['interface'].GetStringSelection().encode('utf-8')
        method_data = self.choice_object['method'].GetStringSelection().encode('utf-8')
        request_body = self.input_box_object["body"].GetValue().encode('utf-8')
        # data_type = self.radio_object[u'普通类型数据'].GetValue()
        if check_object == 'connection':
            if host == '':
                error_info = error_code["box-00001"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            elif port == '':
                error_info = error_code["box-00002"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            else:
                return '1'
        else:
            if host == '':
                error_info = error_code["box-00001"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            elif port == '':
                error_info = error_code["box-00002"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            elif self.connection_instance == None:
                error_info = error_code["box-00006"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            elif interface_data == '':
                error_info = error_code["box-00003"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            elif method_data == '':
                error_info = error_code["box-00004"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            elif request_body == '':
                error_info = error_code["box-00005"]
                self.tips(error_info["title"], error_info["message"])
                return '0'
            else:
                return '1'

    # 提示框
    def tips(self, title, message):
        dlg=wx.MessageDialog(None, message, title, wx.YES_DEFAULT)  #|wx.ICON_QUESTION
        dlg.ShowModal()
        # if(retCode==wx.ID_YES):
        #     print 'yes'
        # else:
        #     print 'no'
        #     dlg.Destroy()

    # 方法
    def send(self, event):
        print '*'*40,'send','*'*40
        if self.connection_instance is not None:
            telnet_state, telnet_info = self.connection_instance.check_connect_state()
            if telnet_state =='0':
                error_info = error_code[telnet_info]
                self.tips(error_info["title"], error_info["message"])
                return
        state = self.check_state()
        if state =='0':
            return
        interface_data = self.choice_object['interface'].GetStringSelection().encode('utf-8')
        method_data = self.choice_object['method'].GetStringSelection().encode('utf-8')
        request_body = self.input_box_object["body"].GetValue().encode('utf-8')
        # body_type = self.radio_object[u'普通类型数据'].GetValue()
        # print '参数类型是否默认类型:',self.radio_object[u'普通类型数据'].GetValue()
        print 'host:', self.input_box_object["host"].GetValue().strip()
        print 'port:', self.input_box_object["port"].GetValue().strip()
        #print 'response:',self.input_box_object['response'].GetValue()
        #print 'remark:',self.input_box_object['remark'].GetValue()
        print u'请求数据:', request_body
        print u'接口:',interface_data
        print u'方法:',method_data
        response,times = self.connection_instance.invoke(interface_data,method_data,request_body)
        self.refresh_results_display(response, times)

    # 用于刷新方法内容
    def refresh_method_display(self, event):
        print u'调用 refresh_method_display 刷新界面的显示内容'
        if self.connection_instance is not None:
            telnet_state, telnet_info = self.connection_instance.check_connect_state()
            if telnet_state =='0':
                error_info = error_code[telnet_info]
                self.tips(error_info["title"], error_info["message"])
                return
        interface_name = self.choice_object['interface'].GetStringSelection()
        cmd = 'ls %s' %interface_name.encode('utf-8')
        all_service_list, info = self.connection_instance.do(cmd)
        self.choice_object['method'].Clear()
        for service in all_service_list[:-1]:
                    self.choice_object['method'].Append(service)

    #显示响应结果及响应时间
    def refresh_results_display(self, response_data, response_times):
        print u'调用显示响应结果及响应时间'
        print 'response_data:', response_data
        print 'response_times:', response_times
        self.input_box_object["response"].SetValue(json.dumps(response_data, ensure_ascii=False))
        self.static_text_object['response_time'].SetLabel(str(response_times))

    def reload(self, event):
        print '*'*40,'reload','*'*40
        self.input_box_object["host"].SetValue('172.30.0.114')
        self.input_box_object["port"].SetValue('20490')
        self.input_box_object["body"].SetValue('{"messageType":"bindWechat","userPhone":"15820492532","smsCode":"769097"}')
        # self.connection_instance.disconnect()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = interface()
    frame.Show()
    app.MainLoop()