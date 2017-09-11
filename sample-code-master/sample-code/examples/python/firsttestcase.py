# -*- coding: utf-8 -*-
#!/usr/bin/env python
# author: lijiale
import os
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep


# Returns abs path relative to this file and not cwd
#构造Desired Capabilities
class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '992616f7'
        desired_caps['appPackage'] = 'com.miui.notes'
        #desired_caps['appActivity'] = '.activity.SplashActivity'
        #driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        #1.获取元素
        #videoBtn = driver.find_element_by_name("视频")

        #2.操作元素
        #videoBtn.click()

        #3.结果验证
    def tearDown(self):
        self.driver.quit()

    # def test_find_elements(self):
    #     # pause a moment, so xml generation can occur
    #     sleep(2)
    #
    #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    #     self.assertEqual('API Demos', els[0].text)
    #
    #     el = self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "Animat")]')
    #     self.assertEqual('Animation', el.text)
    #
    #     el = self.driver.find_element_by_accessibility_id("App")
    #     el.click()
    #
    #     els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
    #     # there are more, but at least 10 visible
    #     self.assertLess(10, len(els))
    #     # the list includes 2 before the main visible elements
    #     self.assertEqual('Action Bar', els[2].text)
    #
    #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    #     self.assertLess(10, len(els))
    #     self.assertEqual('Action Bar', els[1].text)

    # def test_scroll(self):
    #     sleep(2)
    #     els = self.driver.find_elements_by_xpath('//android.widget.TextView')
    #     self.driver.scroll(els[7], els[3])
    #
    #     el = self.driver.find_element_by_accessibility_id('Views')