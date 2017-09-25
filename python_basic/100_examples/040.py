#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：将一个数组逆序输出。
# 程序分析：用第一个与最后一个交换。

a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]

# print a[::-1]
print a
a.sort(reverse=True)
print a
a.reverse()
print a
for i in reversed(a):
    print i

#参考
if __name__ == '__main__':
    a = [9,6,5,4,1]
    N = len(a)
    print a
    for i in range(len(a) / 2):
        a[i],a[N - i - 1] = a[N - i - 1],a[i]
    print a