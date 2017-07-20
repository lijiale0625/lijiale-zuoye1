# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale
import unittest
from bugfree_login_or_condition import  BugfreeAdminLoginLogout
import time
from bussiness_common_steps import *

class BugfreeImportFile(BugfreeAdminLoginLogout):

    def test_bugfree_bug2(self):
        # 取消弹出框
        driver = self.driver
        # driver.find_element_by_xpath(".//*[@id='searchresult-grid']/div[1]/a[3]").click()
        driver.find_element_by_link_text(u"导入").click()
        # driver.implicitly_wait(3)
        """导入文件时，如果存在input标签，可以直接定位到元素，然后通过send_keys()方法上传"""
        driver.find_element_by_id("casefilename").send_keys('./test.xml')
        #导入文件时，如果没有input标签，可用autoIT工具上传

        '''
        driver.find_element_by_id("uploadbutton").click()
        time.sleep(3)
        '''
        #封装根据idc查找元素并默认等待2秒
        click_element_by_id_with_sleep(driver,"uploadbutton",sleep=2)
        #dismiss取消弹出框，accept接收弹出框
        #driver.switch_to.alert.dismiss()
        driver.switch_to.alert.accept()
        time.sleep(3)

