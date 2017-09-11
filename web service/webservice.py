#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: lijiale
#! encoding=utf-8
# auth ： leikai
# 2016-03-30 v1.0
#http://blog.csdn.net/fqlike/article/details/51027905
# url="http://127.0.0.1:8080/ws/xxxxxService?wsdl"
url="http://172.30.0.169:8099/mchtService?wsdl"
from suds.client import Client
# from ParametrizedTestCase import ParametrizedTestCase
import HTMLTestRunner
import unittest
import sys
reload(sys)
from lib.utils import *
import time
sys.setdefaultencoding( "utf-8" )

class ParametrizedTestCase(unittest.TestCase):
    """ TestCase classes that want to be parametrized should
        inherit from this class.
    """
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        self.param = param

    @staticmethod
    def parametrize(testcase_klass, param=None):
        """ Create a suite containing all tests taken from the given
            subclass, passing them the parameter 'param'.
        """
        testloader = unittest.TestLoader()#加载
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()#创建测试集
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
class bindSnNo(ParametrizedTestCase):
    #调用服务是否正常；如果正常，则获取对应的服务类；否则抛异常
    def setUp(self):
        try:
            self.client = Client(url)
        except Exception,e:
            #print e
            sys.exit()
        self.service = self.client.service
    def test_bindSnNo(self):
        "接口测试"
        # temp_data = int(self.param['routeId'])
        # data = {'routeId':temp_data}
        data = self.param
        result = self.service.bindSnNo(data)
        print result
        self.assertEqual(result,self.flag,"routeId:"+data+",is not in line class info!")



if __name__ == "__main__":
    suite = unittest.TestSuite()
    excel = ReadExcel.ReadExcel(path,0)
    # data = excel.readexcel()
    data = read_excel("E:\woody\lijiale-zuoye1\web service\data\workbench.xlsx")
    #print data
    #print len(data)
    for i in range(1,len(data)+1):
        interface,temp_dict,flag = data[i]
        #print interface,temp_dict
        suite.addTest(ParametrizedTestCase.parametrize(bindSnNo, param=temp_dict))
    print suite
    #一个用例
    # interface, temp_dict = data[2]
    # print interface, temp_dict
    # suite.addTest(ParametrizedTestCase.parametrize(getGps, param=temp_dict))
    # print suite
    #filename = u'./report/TestGpsResult.html'
    # fp = file(filename, 'wb')
    fp = open('E:\woody\lijiale-zuoye1\myproj\\reports/test_result_%s.html' % time.strftime("%Y-%m-%d-%H-%M-%S"), 'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'接口测试',
        description=u'用例执行情况：')
    #运行测试用例
    runner.run(suite)
