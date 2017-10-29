#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
def inp(numbers):
    for i in range(6):
        numbers.append(int(raw_input('输入一个数字:\n')))


p = 0


def arr_max(array):
    max = 0
    for i in range(1, len(array) - 1):
        p = i
        if array[p] > array[max]: max = p
    k = max
    array[0], array[k] = array[k], array[0]


def arr_min(array):
    min = 0
    for i in range(1, len(array) - 1):
        p = i
        if array[p] < array[min]: min = p
    l = min
    array[5], array[l] = array[l], array[5]


def outp(numbers):
    for i in range(len(numbers)):
        print numbers[i]


if __name__ == '__main__':
    array = []
    inp(array)  # 输入 6 个数字并放入数组
    arr_max(array)  # 获取最大元素并与第一个元素交换
    arr_min(array)  # 获取最小元素并与最后一个元素交换
    print '计算结果：'
    outp(array)

#
a=[1,2,3,7,9,8]
for i in range(len(a)):
    if a[i]==max(a):
        a[0],a[i]=a[i],a[0]

for i in range(len(a)):
    if a[i]==min(a):
        a[len(a)-1],a[i]=a[i],a[len(a)-1]

print a
#2
a=[1,2,3,7,9,8]
print a
# 最小的放到最后
min = min(a)
a.remove(min)
a.append(min)
# 最大的放到最前面
max = max(a)
a.remove(max)
a.insert(0,max)
print a

#3
a=[]
for i in range (6):
    a.append(int(raw_input('num:')))
b=sorted(a)
for j in range(6):
    if a[j]==b[0]:
        a[0],a[j]=a[j],a[0]
for k in range(6):
    if a[k]==b[5]:
        a[5],a[k]=a[k],a[5]
print a
#4
import numpy as np
a = []
for i in range(5):
    a.append(input("Please input a number: "))
print a
a = np.array(a)
#得到最大值的索引
max_index = np.argmax(a)
#得到最小值的索引
min_index = np.argmin(a)
a[0], a[max_index] = a[max_index], a[0]
a[-1], a[min_index] = a[min_index], a[-1]
print a