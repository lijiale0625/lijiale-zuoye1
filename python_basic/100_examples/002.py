#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
#60万到100万之间时，高于60万元的部分，可提成1.5%，
#高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

i = int(raw_input('请输入利润金额：'))
a=[0,100000,200000,400000,600000,1000000]
#倒序排列
a1=a[::-1]
b=[0.1,0.075,0.05,0.03,0.015,0.01]
#reversed(a)  返回一个倒序可遍历对象，需序遍历出
b_reversed = reversed(b)
b1 = []
for i1 in b_reversed:
    b1.append(i1)

print a1,b1
result = 0
for j in range(0,len(b1)):
    if i > a1[j]:
        result += (i-a1[j])*b1[j]
        print (i-a1[j])*b1[j]
        i = a1[j]
print result

# 答案
# for idx in range(0,6):
#     if i > arr[idx]:
#         r += (i-arr[idx])*rat[idx]
#         print (i-arr[idx])*rat[idx]
#         i=arr[idx]
# print r