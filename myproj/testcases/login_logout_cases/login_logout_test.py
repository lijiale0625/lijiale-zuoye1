# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale

from selenium import webdriver

from selenium.webdriver.support.ui import Select

import unittest, time, re,os

from testcases.common_logic.bussiness_common_steps import *
from  config import *
from lib.utils import *
from testcases.product_management.product_add import  ProductAdd
class LoginLogoutTest(unittest.TestCase):
    u'''创建用例-查询用例-统计用例报表'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        driver.get(self.base_url + "/bugfree/index.php/site/login")
        #打开bugfree登录页面
        #driver.get(url)
        #将登录页面函数封装成open_url(driver,url)
        #open_url(driver, self.base_url)

        #封装后的登录函数
        #login_bugfree(self.driver,"admin","123456")
        #login_bugfree(self.driver, username1, password1)
        #os.getcwd()获取当前模块
        self.data_dict = read_excel(os.getcwd()+'\data\login_account.xlsx')
        #print  self.data_dict


    def test_bugfree_login_success(self):
        u'''登录bugfree成功'''
        driver = self.driver
        username, password, flag = self.data_dict[1]
        #print username, password, flag
        login_bugfree(driver, username, password)
        self.assertEqual(flag, driver.title)
        # login_bugfree(driver, "admin", "123456")
        # self.assertEquals("Bugfree",driver.tittle)

    def test_bugfree_login_fail_invalid_username(self):
        u'''无效姓名登录bugfree失败'''
        driver = self.driver
        #data_dict[1]蒋字典里key为1的value分别赋值给username, password, flag
        username, password, flag = self.data_dict[2]
        #print username, password, flag
        login_bugfree(driver, username, password)
        #login_bugfree(driver, "invalid", "123456")
        self.assertIn(flag, driver.page_source)

    def test_bugfree_login_fail_invalid_password(self):
        u'''无效密码登录bugfree失败'''
        driver = self.driver
        #data_dict[1]蒋字典里key为1的value分别赋值给username, password, flag
        username, password, flag = self.data_dict[3]
        #print username, password, flag
        login_bugfree(driver, username, password)
        #login_bugfree(driver, "invalid", "123456")
        self.assertIn(flag, driver.page_source)
    def tearDown(self):
        driver = self.driver
        driver.quit()

