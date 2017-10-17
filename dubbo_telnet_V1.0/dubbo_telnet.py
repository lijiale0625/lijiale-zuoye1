#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import socket
import telnetlib

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class dubbo:
    # 定义私有属性
    __init = False
    __encoding = "gbk"
    __finish = 'dubbo>'
    __connect_timeout = 10
    __read_timeout = 10

    # 定义构造方法
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.telnet_instance =None
        if host is not None and port is not None:
            self.__init = True

    def set_finish(self, finish):
        '''
        defualt is ``dubbo>``
        '''
        self.__finish = finish

    def set_encoding(self, encoding):
        '''
        If ``result retured by dubbo`` is a ``str`` instance and is encoded with an ASCII based encoding
        other than utf-8 (e.g. latin-1) then an appropriate ``encoding`` name
        must be specified. Encodings that are not ASCII based (such as UCS-2)
        are not allowed and should be decoded to ``unicode`` first.
        '''
        self.__encoding = encoding

    def set_connect_timeout(self, timeout):
        '''
        Defines a timeout for establishing a connection with a dubbo server.
        It should be noted that this timeout cannot usually exceed 75 seconds.

        defualt is ``10``
        '''
        self.__connect_timeout = timeout

    def set_read_timeout(self, timeout):
        '''
        Defines a timeout for reading a response expected from the dubbo server.

        defualt is ``10``
        '''
        self.__read_timeout = timeout

    def connection_telnet(self):
        try:
            print u'调用 connection_telnet 方法，开始连接'
            self.telnet_instance = telnetlib.Telnet(host=self.host, port=self.port, timeout=self.__connect_timeout)
            print ("[host:%s port:%s connection successful]" % (self.host, self.port))
            return '1',''
        except socket.error as err:
            print ("[host:%s port:%s connection fails] %s" % (self.host, self.port, err))
            return '0', '[host:%s port:%s connection fails] %s'% (self.host, self.port, err)

    def disconnect(self):
        print u'调用 disconnect断开连接'
        if not self.telnet_instance ==None:
            self.telnet_instance.close()
        print u'已断开连接'

    def check_connect_state(self):
        try:
            print u'检查当前Telnet连接状态'
            self.telnet_instance.write('\n')   # 执行命令
            self.telnet_instance.read_until(self.__finish, timeout=self.__read_timeout)
            self.telnet_instance.write('%s\n' % 'ls')
            data = ''                          # 获取结果
            while data.find(self.__finish) == -1:
                data=self.telnet_instance.read_very_eager()
            print u'Telnet状态：正常'
            return '1', ''
        except Exception, e:
            print u'Telnet状态：异常，', e
            return '0', 'box-00007'

    def do(self, command):
        # 连接Telnet服务器
        # 触发doubble提示符
        self.telnet_instance.write('\n')

        # 执行命令
        self.telnet_instance.read_until(self.__finish, timeout=self.__read_timeout)
        self.telnet_instance.write('%s\n' % command)

        # 获取结果
        data = ''
        while data.find(self.__finish) == -1:
            data = self.telnet_instance.read_very_eager()
        try:
            data = data.split("\n")
            return json.loads(data[0], encoding=self.__encoding), data[1]
        except:
            return data, ''

    def invoke(self, interface, method, param, param_type='0'):
        cmd = "%s %s.%s(%s)" % ('invoke', interface, method, param)
        # if  param_type == '0':
        # if not isinstance(param, str):
        #     param =json.dumps(param)
        # cmd = "%s %s.%s(%s)" % ('invoke', interface, method, param)
        # else:
        #     cmd = "%s %s.%s(%s)" % ('invoke', interface, method, param)
        print '*'*20, ' invoke ', '*'*20
        print u'cmd:%s' %cmd
        print '*'*20, ' invoke ', '*'*20
        return self.do(cmd)

# def connect(host, port):
#      return dubbo(host, port)


if __name__ == '__main__':
    Host = '172.30.0.169'  # Doubble服务器IP  172.30.0.115
    Port =20880  # Doubble服务端口 20890 20870
    conn = dubbo(Host, Port)     # 初始化dubbo对象
    conn.set_connect_timeout(10) # 设置telnet连接超时时间
    conn.set_encoding('gbk')     # 设置dubbo服务返回响应的编码
    conn.connection_telnet()
    print '*'*50,u'dubbo service list'
    print conn.do('ls')
    for name in conn.do('ls'):
        print (name)
    print '*'*50,u'interface way 接口方法'
    for way in (conn.do('ls com.alibaba.dubbo.demo.DemoService')):  #com.iboxpay.olio.user.api.MerchantUserApi
        print (way)
    print '*'*25,u'invoke dubbo interface'
    interface = 'com.alibaba.dubbo.demo.DemoService'
    method = 'test_int'
    param =1222
    data=conn.invoke(interface, method, param, '0')
    print '*'*25,u'response 响应数据'
    print(json.dumps(data,ensure_ascii=False, indent=4))
    print conn.do('ps')
    print conn.do('pwd')   #log
    print conn.do('status -l')
    #print conn.do('log 100')
    print conn.do('count com.iboxpay.olio.coupon.api.GetCouponCountApi')