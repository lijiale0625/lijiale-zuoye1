#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
import random
n = int(raw_input("请输入一个大于3 的整数："))
l = range(1,n+1)
for i in range(1,len(l)) :
    if i%3 == 0 :
        l.__reduce__(l[i])