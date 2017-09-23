# -*- coding:UTF-8 -*-
# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

i = str(raw_input('请输入一个不多于5位的正整数：'))
l = len(i)
while (1):
    if l > 5:
        i = str(raw_input('输入有误，请重新输入：'))
        l = len(i)
    break
print l