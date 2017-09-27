#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'
def is_not_empty(s):
    return s and len(s.strip()) > 0
#and运算表示只有当s为真，并且s去掉首位空格后长度大于零（帮助排除s是'   '的情况），才返回True，否则返回False
# 就可以起到filter的效果了
#1)??
# def is_not_empty(s):
#     if s == True:
#         if len(s.strip()) > 0:
#             return True
#     else:
#         return False
print is_not_empty('')
a = ['test', None, '', 'str', '  ', 'END']
#filter()函数是 Python 内置的另一个有用的高阶函数，filter()函数接收一个函数 f 和一个list，
# 这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，
# 返回由符合条件元素组成的新list。
l2=filter(is_not_empty, a)#要是list里面添加了整型数据会报错，
print l2
# strip()函数 介绍
# 声明：s为字符串，rm为要删除的字符序列
# s.strip(rm)        删除s字符串中开头、结尾处，位于 rm删除序列的字符
# s.lstrip(rm)       删除s字符串中开头处，位于 rm删除序列的字符
# s.rstrip(rm)      删除s字符串中结尾处，位于 rm删除序列的字符
# 注意：
# 1. 当rm为空时，默认删除空白符（包括'\n', '\r',  '\t',  ' ')

