#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'
# 1.  漂亮胜于丑陋
# 实现一个功能：读取一列数据，只返回偶数并除以2。下面的代码，哪个更好一些呢？
# ----------------------------------------
nums = [1, 4, 6, 7, 9, 12, 17]
halve_evens_only = lambda nums: map(lambda i: i / 2, filter(lambda i: not i % 2, nums))
#filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新list。
print halve_evens_only([1,2,3,4])

# ----------------------------------------

def halve_evens_only(nums):
    return [i / 2 for i in nums if not i % 2]