#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 题目：数字比较。
# i= int(raw_input('请输入一个数字：'))
# j = int(raw_input('请再输入一个数字：'))
# if i>j :
#     print '%d>%d'%(i,j)
# elif i == j:
#     print '%d=%d' % (i, j)
# else:
#     print '%d<%d' % (i, j)
# 参考
def compare(num1, num2):
    if num1 > num2:
        print("%s大于%s" % (num1, num2))
    elif num2 > num1:
        print("%s大于%s" % (num2, num1))
    else:
        print("%s等于%s" % (num1, num2))

if __name__ == "__main__":
    numOne = input("请输入第一个数字:")
    numTwo = input("请输入第二个数字:")
    compare(numOne, numTwo)