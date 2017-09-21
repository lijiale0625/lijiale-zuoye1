#!/usr/bin/python
# -*- coding: UTF-8 -*-
i=int(raw_input('净利润:'))
I=[1000000,600000,400000,200000,100000,0]
r=[0.01,0.015,0.03,0.05,0.075,0.1]
for j in range(len(I)):
    if i>I[j]:
        b=[0,0,0,0,0,0]
        b[j]=i-I[j]
        for k in range(j,len(I)):
            b[k]=I[k]
        bonus=sum(map(lambda (i1,i2): i1*i2, zip(b,r))) #map函数，很简单，第一个参数接收一个函数名，第二个参数接收一个可迭代对象
        break
print '奖金:',bonus