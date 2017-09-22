#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，
# 特殊情况，闰年且输入月份大于2时需考虑多加一天：

d = raw_input('请输入当前日期：')
mermonth = [31,28,31,30,31,30,31,31,30,31,30,31]
sum=0
year1 = int(d[0:4])
month1 = int(d[4:6])
date1 = int(d[6:8])
print year1,month1,date1
for i in range(0,month1-1):
    sum += mermonth[i]
    print sum
if (year1 % 400 == 0 or year1 % 4 == 0) and year1 % 100 != 0 and month1 > 2 :
    sum = sum + 1
    print sum
print 'it is the %dth day.' % (sum+date1)
# print  sum+date1