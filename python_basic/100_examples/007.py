#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：将一个列表的数据复制到另一个列表中。
# 程序分析：使用列表[:]。
#1）使用列表属性
a = [1,2,3,8,6,4,2,1,3,5,4]
b = a[:]
b1 = a[::2]
b2 = a[1::2]

print b,b1,b2
#2)引用copy类
import copy
b3 = copy.copy(a)
print b3
#3)迭代添加
p = []
for i in range(len(a)):
    p.append(a[i])
print p