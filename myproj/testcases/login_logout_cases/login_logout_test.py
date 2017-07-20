# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale

from selenium import webdriver

from selenium.webdriver.support.ui import Select

import unittest, time, re

from testcases.common_logic.bussiness_common_steps import *
from  config import *
from lib.utils import read_excel

class LoginLogoutTest(unittest.TestCase):
    u'''创建用例-查询用例-统计用例报表'''

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost/bugfree"
        #url = self.base_url + "/bugfree/index.php/site/login"
        driver = self.driver
        #打开bugfree登录页面
        #driver.get(self.base_url)
        #将登录页面函数封装成open_url(driver,url)
        open_url(driver, self.base_url)

        #封装后的登录函数
        #login_bugfree(self.driver,"admin","123456")
        #login_bugfree(self.driver, username1, password1)
        #os.getcwd()获取当前模块
        self.data_dict = read_excel(os.getcwd()+'\data\login_account.xlsx')
        print  self.data_dict


    def test_bugfree_login_success(self):
        u'''登录bugfree成功'''
        driver = self.driver
        login_bugfree(driver, "admin", "123456")
        self.assertEquals("Bugfree",driver.tittle)

    # def test_bugfree_login_fail_invalid_username(self):
    #     u'''登录bugfree失败'''
    #     driver = self.driver
    #     login_bugfree(driver, "invalid", "123456")
    #     self.assertEquals("XX", driver.page_source)
    #
    # def test_bugfree_login_fail_invalid_password(self):
    #     u'''登录bugfree失败'''
    #     driver = self.driver
    #     login_bugfree(driver, "admin", "invalid")
    #     self.assertEquals("XX", driver.page_source)

