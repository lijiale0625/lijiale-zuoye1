# -*- coding:utf-8 -*-
# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
# 程序分析：无。
i = raw_input('请输入一个5位数：')
j = str(i)
if j[0] == j[len(j)-1] and j[1] == j[3]:
    print '%s是回文数！'% j
else:
    print '%s不是回文数！' % j

#参考
a = input("输入一串数字: ")
b = a[::-1]
if a == b:
    print("%s 是回文"% a)
else:
    print("%s 不是回文"% a)