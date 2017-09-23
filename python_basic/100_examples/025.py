# -*- coding: UTF-8 -*-
# 题目：求1+2!+3!+...+20!的和。
# 程序分析：此程序只是把累加变成了累乘。
'''
l = []
for i in range(1,21):
    z = 1
    for j in range(1,i+1):
        z = z*j
    l.append(z)
    print l
for k in l:
    s = 0
    s = s+k
print s
'''
#参考答案
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
    print t,s
print '1! + 2! + 3! + ... + 20! = %d' % s