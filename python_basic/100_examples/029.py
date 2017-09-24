# -*- coding:UTF-8 -*-
# 题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
# 程序分析：学会分解出每一位数。

i = str(raw_input('请输入一个不多于5位的正整数：'))
while (1):
    if len(i) > 5 or int(i) <= 0 :
        i = str(raw_input('输入有误，请重新输入：'))
    else:
        print '%d的位数为%d'%(int(i),len(i))
        print('逆序为：\n')
        print(i[::-1])
        break

#参考
# print( '请输入大于10的数字:' )
# n=input()
# x=[]
# i=0;
# while(n!=0):
#     x.append(n%10)
#     i+=1
#     n/=10
# print( '该数有 %d 位\n' %i )
# print( '逆序为：\n')
# print( x[::] )
