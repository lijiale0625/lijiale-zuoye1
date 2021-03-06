# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale

from testcases.common_logic.bussiness_common_steps import *
# from bussiness_common_steps import *
from  config import *
from selenium import webdriver
import unittest, time, re
from testcases.bugfree_import_file import BugfreeImportFile

class ProductAdd(unittest.TestCase):
    """Bugfree_产品添加测试"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        driver = self.driver
        self.base_url = "http://localhost/bugfree"
        # 将登录页面函数封装成open_url(driver,url)
        open_url(driver, self.base_url)
        # 封装后的登录函数
        #login_bugfree(self.driver,"admin","123456")
        login_bugfree(self.driver, username1, password1)
        # login_bugfree(self.driver, 'admin', '123456')

    def test_product001(self):
        """新增产品"""
        driver = self.driver
        # driver.get(self.base_url + "/bugfree/index.php/bug/list/1")
        driver.find_element_by_link_text(u"后台管理").click()
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_link_text(u"添加产品").click()
        driver.find_element_by_id("Product_name").clear()
        #方便tearDown()中删除新增的产品id,self.product_id在前面加self才能被tearDown()调用，不然就仅能在此方法内用
        self.product_id = "Product_%s" % generate_random_num(1,99)
        driver.find_element_by_id("Product_name").send_keys(self.product_id)
        driver.find_element_by_id("Product_display_order").clear()
        driver.find_element_by_id("Product_display_order").send_keys("2")
        driver.find_element_by_id("Product_bug_severity").clear()
        driver.find_element_by_id("Product_bug_severity").send_keys("1,2,3,4,5")
        driver.find_element_by_id("Product_bug_priority").clear()
        driver.find_element_by_id("Product_bug_priority").send_keys("1,2,3,4,5")
        driver.find_element_by_id("Product_case_priority").clear()
        driver.find_element_by_id("Product_case_priority").send_keys("1,2,3,4,5")
        driver.find_element_by_name("yt0").click()

    def tearDown(self):
        #要在这里删除刚刚新增的产品id，self.product_id
        #连接数据库后在此执行一个delete语句
        #pass
        driver = self.driver
        self.driver.quit()
