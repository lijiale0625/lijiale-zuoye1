# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale
import unittest
from bugfree_login_or_condition import  BugfreeAdminLoginLogout
import time


class BugfreeImportFile(BugfreeAdminLoginLogout):

    def test_bugfree_bug2(self):
        # 取消弹出框
        driver = self.driver
        # driver.find_element_by_xpath(".//*[@id='searchresult-grid']/div[1]/a[3]").click()
        driver.find_element_by_link_text(u"导入").click()
        # driver.implicitly_wait(3)
        driver.find_element_by_id("uploadbutton").click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)


