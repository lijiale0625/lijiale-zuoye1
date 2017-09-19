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