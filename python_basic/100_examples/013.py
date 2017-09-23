#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
# 例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
# 程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
l=[]
for j in range(100,1000):
    i=str(j)
    print i,i[0],i[1],i[2]
    if (int(i[0]))**3+(int(i[1]))**3+(int(i[2]))**3 == int(i):
        l.append(i)
print l

#参考答案
for n in range(100,1000):
    i = n / 100  #取商
    j = n / 10 % 10  #取商再取余数
    k = n % 10      #取余数
    if n == i ** 3 + j ** 3 + k ** 3:
        print n