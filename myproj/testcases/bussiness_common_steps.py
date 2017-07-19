# -*- coding: utf-8 -*-
#!/usr/bin/env python   
# author: lijiale
import time
from selenium import webdriver
from  config import *
def open_url(driver,url):
    driver.get(url)
def login_bugfree(driver,username,password):
    driver.find_element_by_id("LoginForm_username").clear()
    driver.find_element_by_id("LoginForm_username").send_keys(username)
    driver.find_element_by_id("LoginForm_password").clear()
    driver.find_element_by_id("LoginForm_password").send_keys(password)
    driver.find_element_by_id("LoginForm_rememberMe").click()
    driver.find_element_by_id("SubmitLoginBTN").click()
def get_screenshots_immediately(driver,path=None):
    if path is  None :
        #当前目录下截图
        driver.get_screenshot_as_file(r"./screenshots/shots_%s.jpg"%time.strftime("%Y-%m-%d %H-%M-%S"))
    else:
        driver.get_screenshot_as_file(path)
def generate_random_num(start,stop):
    """
    @desc:生成一个随机整数
    @usage:generate_random_num(1,99)
    """
    import random
    return random.randint(start,stop)

def click_element_by_id_with_sleep(driver,id,sleep=2):
    #判断元素是否存在
    try:
        driver.find_element_by_id(id).click()
    except:
        pass
    finally:
        time.sleep(2)



