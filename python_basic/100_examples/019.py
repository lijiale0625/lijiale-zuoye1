#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
# 程序分析：请参照程序Python 练习实例14。

# i= int(raw_input('请输入一个正整数：'))
# l=[1]
# h=[]
# for i in range(1,1001):
#     while i != 1:
#         for j in range(2,i+1):
#             if (i%j) == 0:
#                 #print '%d最小的质因数为：%d'%(i,j)
#                 l.append(j)
#                 i=i/j
#                 break
#                 #continue
#         if reduce(lambda x,y:x+y,l)==i:
#             h.append(i)
#
# print h
#         # if reduce(lambda x,y:x+y,l)==i:
#         #     h.append(i)
#         #     print h

#参考答案
for i in range(1, 1001):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)