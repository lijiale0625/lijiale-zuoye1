#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: lijiale
#http://zhxsnn.blog.51cto.com/9877771/1609820/
from suds.client import Client #导入suds.client 模块下的Client类
Mobile_url="http://webservice.webxml.com.cn/WebServices/MobileCodeWS.asmx?wsdl"#手机号码归属地
QQ_url="http://webservice.webxml.com.cn/webservices/qqOnlineWebService.asmx?wsdl"#qq在线状态
Random_url='http://webservice.webxml.com.cn/WebServices/RandomFontsWebService.asmx?wsdl'#生成随机字符串
def WsTest(url,Wsname,data):
    '''
    :param url: wsdl地址
    :param Wsname: 方法名，做保存结果的文件名
    :param data: 方法的传入参数
    :return:
    '''
    client = Client(url)
    client.service.getMobileCodeInfo(data)#调用这个接口下的getMobileCodeInfo方法，并传入参数
    req = str(client.last_sent())#保存请求报文，因为返回的是一个实例，所以要转换成str
    response = str(client.last_received())#保存返回报文，返回的也是一个实例
    print response#打印返回报文
    WriteRes(Wsname,req,response,data)#调用写入结果函数，把方法名、请求报文、返回报文、和入参传进去
def WriteRes(WsName,req,response,data):
    '''
    :param WsName: 接口的方法名
    :param req: 请求报文
    :param response: 返回报文
    :param data: 传入的数据
    '''
    res = response.find(data)#从返回结果里面找data，如果找到的话返回data的下标，也就是索引，找不到的话返回-1
    fw_flag = open('/tmp/WsTestRes/WsTestRes.txt','a')#以追加模式打开写入结果文件
    if res>0:
        fw_flag.write('%s  pass'%WsName)#如果在返回报文中找到data的话，就写pass,否则就写fail
    else:
        fw_flag.write('%s  fail'%WsName)
    fw_flag.close()#关闭结果文件
    fw_result = open('/tmp/WsTestRes/%s_result.txt'%WsName,'w')#打开以接口方法命名的文件
    fw_result.write(req+'\n'*3+response)#保存请求报文和返回报文，\n*3的意思是换行三次
    fw_result.close()#关闭结果文件
if __name__ =='__main__':
    WsTest(Mobile_url,'getMobileCodeInfo','110')