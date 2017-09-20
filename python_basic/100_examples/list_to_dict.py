#!/usr/bin/python
# -*- coding: UTF-8 -*-
#list_to_dict
i = ['a', 'b']
q=['c','d']
l = [1, 2]
print dict([i, l,q])
#两个长度相等的list转换成字典
l1=[1,2,3,6,87,3]
l2=['aa','bb','cc','dd','ee','ff']
d={}
print range(len(l1))
for index in range(len(l1)):
    d[l1[index]]=l2[index] # 注意，key 若重复，则新值覆盖旧值
    print d
print d
# 从列表创建字典
i = ['a','b','c']
l = [1,2,3]
b=dict(zip(i,l))
print(b)
#矩阵
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print [[row[col] for row in a] for col in range(len(a[0]))]
#[[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print len(a[0])
#
keys = ['a', 'b']
values = [1, 2]
print({keys[i]: values[i] for i in range(len(keys))})
#使用 Python 字典 setdefault() 方法：
l1 = ['a','b','c']
l2 = [1,2,3]
d = {}
for i in range(len(l1)):
    d.setdefault(l1[i],0)
print d