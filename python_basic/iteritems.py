#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

d = {1: "1", 2: "2", 3: "3"}
#字典items()方法和iteritems()方法，是python字典的内建函数，分别会返回Python列表和迭代器
print d.items()
for key, val in d.items() :
    print key,val

# 当调用时构建完整的列表

for key, val in d.iteritems():
    print key, val
# 当请求时只调用值
iter = d.iteritems() #看函数名是迭代输出字典的键值对。
print iter.next()
