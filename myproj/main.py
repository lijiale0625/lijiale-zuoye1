# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale

import unittest,time
from HTMLTestRunner import HTMLTestRunner

#from testcases.bugfree_login_or_condition import *
# from testcases.bugfree_import_file import BugfreeImportFile
from testcases.product_management.product_add import ProductAdd
from testcases.login_logout_cases.login_logout_test import LoginLogoutTest


def main():
    suite = unittest.TestSuite()#生成测试集
    loader = unittest.TestLoader()#加载
    #把BugfreeAdminLoginLogout类中的测试用例存放到测试集里
    #suite.addTest(loader.loadTestsFromTestCase(BugfreeAdminLoginLogout))
    #添加导入类测试用例，继承了BugfreeAdminLoginLogout类
    #suite.addTest(loader.loadTestsFromTestCase(BugfreeImportFile))
    #添加产品类测试用例
    suite.addTest(loader.loadTestsFromTestCase(ProductAdd))
    #添加登录用例
    suite.addTest(loader.loadTestsFromTestCase(LoginLogoutTest))
    #不生成报表
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #生成报表
    #fp = open('./reports/test_result_%s.html' % time.strftime("%Y-%m-%d-%H-%M-%S"), 'wb')
    fp = open('E:\woody\lijiale-zuoye1\myproj\\reports/test_result_%s.html' % time.strftime("%Y-%m-%d-%H-%M-%S"), 'wb')

    runner = HTMLTestRunner(stream=fp,
                            title=u'登录-查询',
                            description=u'创建bug-查询用例结果-统计用例情况')
    runner.run(suite)
   #为什么不用倒入from HTMLTestRunner import HTMLTestRunner呢?

if __name__ == "__main__":
    main()