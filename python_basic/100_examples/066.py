#!/usr/bin/python
# -*- coding: UTF-8 -*-
#方法一
# a=[]
# for i in range(3):
#     a.append(input("请输入一个数字："))
# a.sort()
# print a
#方法二


# L = []
# for i in range(3):
#     L.append(int(raw_input('输入一个数字:')))
# for i in range(3):
#     for j in range(i + 1, 3):
#         if L[i] > L[j]:
#             L[i],L[j] = L[j],L[i]
# print L

#方法三

if __name__=='__main__':
    l=[]
    for i in range(3):
        x=raw_input('输入一个数字:')
        l.append(x)
    for i in range(3):
        print(max(l))
        l.remove(max(l))  #利用 remove（）函数依次输出最大值