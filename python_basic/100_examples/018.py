#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
# 程序分析：关键是计算出每一项的值。

# a = str(raw_input('要累加数字：'))
# b = int(raw_input('累计的次数：'))
# l = []
# s = 0
# for i in range(1,b+1):
#     l.append(a*i)
# print l
# for j in range(len(l)):
#     s += int(l[j])
# print s
#参考答案
Tn = 0
Sn = []
n = int(raw_input('n = '))
a = int(raw_input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn

Sn = reduce(lambda x, y: x + y, Sn)
print "计算和为：", Sn
