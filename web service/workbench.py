#!/usr/bin/env python
# -*- coding: utf-8 -*-
#1)引入suds库，代码如下：
from suds.client import Client
from config  import  *
import sys
import unittest
import json
#2)创建一个webservice对象，来调用webservice里面的各类接口

user_url="http://172.30.0.169:8099/mchtService?wsdl" #这里是你的webservice访问地址
#创建商户
# client=Client(user_url)      #Client里面直接放访问的URL，可以生成一个webservice对象
# print client
# result = client.service.createMcht(t)
# print(result)
# # print len(client)
# print type(result)
# print  dir(result)
# json_data = result.json()

#绑定二维码
#{"mchtNo":"015440395007352","snNo":"019950135999"}
user_url="http://172.30.0.169:8099/mchtService?wsdl" #这里是你的webservice访问地址

try:
    client=Client(user_url)      #Client里面直接放访问的URL，可以生成一个webservice对象
except Exception,e:
    print e
    sys.exit()
service = client.service
print client
result = service.bindSnNo(t2)
print(result)
        #return result

# assertEqual(result['status'], 0)
# json_data = result.json()
# assertEqual(json_data['status'], 0)

#http://zhxsnn.blog.51cto.com/9877771/1609820/
# Mobile_url="http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl"
# client = Client(Mobile_url)
# print(client)
# client.service.getMobileCodeInfo(data)#调用这个接口下的getMobileCodeInfo方法，并传入参数
# req = str(client.last_sent())#保存请求报文，因为返回的是一个实例，所以要转换成str
# response = str(client.last_received())#保存返回报文，返回的也是一个实例
# print response#打印返回报文