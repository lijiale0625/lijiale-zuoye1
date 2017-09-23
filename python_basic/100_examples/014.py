#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 程序分析：对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：
# (1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。
# (2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。
# (3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

i= int(raw_input('请输入一个正整数：'))
l=[]
while i != 1 :
    for j in range(2,i+1):
        if (i%j) == 0:
            #print '%d最小的质因数为：%d'%(i,j)
            l.append(j)
            i=i/j
            # break
            continue
print l
# #参考答案
# input = int(raw_input("请输入要分解的正整数："))
#
# temp = []
# while input!=1:
#     for i in range(2,input+1):
#         if input%i == 0:
#             temp.append(i)
#             input = input/i
#             break

# print temp
# break和continue都是用来控制循环结构的，主要是停止循环。
#
# 1.break
#
# 有时候我们想在某种条件出现的时候终止循环而不是等到循环条件为false才终止。
#
# 这是我们可以使用break来完成。break用于完全结束一个循环，跳出循环体执行循环后面的语句。
#
# 2.continue
#
# continue和break有点类似，区别在于continue只是终止本次循环，接着还执行后面的循环，break则完全终止循环。
#
# 可以理解为continue是跳过当次循环中剩下的语句，执行下一次循环。

