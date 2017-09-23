#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'
# 题目：打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 程序分析：先把图形分成两部分来看待，前四行一个规律，后三行一个规律，利用双重for循环，第一层控制行，第二层控制列。
# for i in range(1,5):
#     for j in range(1,8,2):
#         print '*'*j,
#         print ''
# for i in range(1,4):
#     for j in range(5,1,-2):
#         print '*'*j,
#         print ''
#参考
def pic(lines):
    middle, lines = int(lines / 2), int(lines / 2) * 2 + 1
    for i in range(1, lines + 1):
        empty = abs(i - middle - 1)
        print(' ' * empty, '*' * (2 * (middle - empty) + 1))
line = 7 # 设置输出行数
pic(7)
#2）最简单的方法
for i in range(4):
    print((3-i)*' '+(2*i+1)*'*')
for i in range(3):
    print((i+1)*' '+(5-2*i)*'*')