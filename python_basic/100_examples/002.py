#!/usr/bin/python
# -*- coding: UTF-8 -*-
#题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
#利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
#20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
#60万到100万之间时，高于60万元的部分，可提成1.5%，
#高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
#程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。

#i = int(raw_input('请输入利润金额：'))
a=[0,100000,200000,400000,600000,1000000]
a_reversed=reversed(a)
b=[0.1,0.075,0.05,0.03,0.015,0.01]
b_reversed=reversed(b)
print b_reversed
result=0
for j in range(0,len(b_reversed)):
    if i>a_reversed[j] :
        result += (i-a_reversed[j])*b_reversed[j]
        print (i-a_reversed[j])*b_reversed[j]
print result