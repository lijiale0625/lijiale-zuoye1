#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'
# 题目：暂停一秒输出。
# 程序分析：使用 time 模块的 sleep() 函数。
import time
# while(1):
#     time.sleep(1)
#     print "hello,world!"


myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1)