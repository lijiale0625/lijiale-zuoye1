#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 1、数组倒序：
# 原始元素的倒序排列
arr = [1,2,3,4,3,4]
# (1)
print arr[::-1]
# ---->[4, 3, 4, 3, 2, 1]
# (2)
arr.reverse()
print arr
# ---->[4, 3, 4, 3, 2, 1]
# (3)reversed(arr)     #返回一个倒序可遍历对象，需序遍历出
arr = [1,2,3,4,3,4]
reversed_arr = []
for i in reversed(arr):
    reversed_arr.append(i)
print reversed_arr
# ---->[4, 3, 4, 3, 2, 1]

# 2、字符串倒序：
# (1)利用字符串截取
param = 'hello'
print param[::-1]
# ---->'olleh'

# (2)利用reversed()返回倒可迭代对象（字符串实现）
param = 'hello'
rev_str = ''
for i in reversed(param):
    rev_str += i
    print rev_str
print rev_str
# ---->'olleh'
# (3)利用reversed()返回倒可迭代对象（数组实现）
rev_arr = []
for i in reversed(param):
    rev_arr.append(i)
print rev_arr
print ''.join(rev_arr)


# 另：
# 元素排序后的倒序排列：
# 1、sorted(...)生成新的已排列数组
# sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
# 2、arr.sort(...)直接操作arr，arr内元素进行正序排列
#
# 元素内的排序
# param = 'hello'     #返回元素内的排序
# rev_str =  ''.join(sorted(param))     #sorted(param)返回倒序排列的数组['e', 'h', 'l', 'l', 'o']
# print rev_str      ---->'ehllo'
