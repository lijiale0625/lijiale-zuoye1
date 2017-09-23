#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 其中reduce函数是python中的一个二元内建函数，它可以通过传给reduce中的函数（必须是二元函数）依次对数据集中的数据进行操作。
# 例如上述代码传给reduce的函数是做加法，数据集是list，那么reduce函数的作用就是将数据集中的数据依次相加，最后打印出的结果就是15。
# 凡是要对一个集合进行操作的，并且要有一个统计结果的，能够用循环或者递归方式解决的问题，
# 一般情况下都可以用reduce方式实现。在python 3.0.0.0以后, reduce已经不在built-in function里了,
# 要用它就得from functools import reduce。

list = [1,2,3,4,5]
print reduce(lambda x,y:x+y,list)