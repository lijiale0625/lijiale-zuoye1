#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：暂停一秒输出，并格式化当前时间。
# 程序分析：无。
import time
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print key, value
    time.sleep(1)

# while(1):
#     print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#
# # 暂停一秒
#     time.sleep(1)
#
#     print time.strftime('%Y-%m-%d %H:%M:%S %w ', time.localtime(time.time()))
#     time.sleep(1)