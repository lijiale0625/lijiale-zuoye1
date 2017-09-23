#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# 程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。

i = int(raw_input('请输入你的分数:'))
print type(i)
if i >= 90:
    print 'A'
elif i >= 60 :
    print 'B'
else:
    print 'C'
