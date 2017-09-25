#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
# 程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

# l=[1,1,1,23,4,5,6,12]
# l.sort()
# print l
# s = int(raw_input('请输入一个数字：'))
# if s < l[0]:
#     l.insert(0,s)
# elif s > l[-1]:
#     l.insert(len(l),s)
# else:
#     for i in range(len(l)):
#         if  l[i] > s:
#             l.insert(i,s)
#             break
# print l

#参考
# if __name__ == '__main__':
#     # 方法一 ： 0 作为加入数字的占位符
#     a = [1,4,6,9,13,16,19,28,40,100,0]
#     print '原始列表:'
#     for i in range(len(a)):
#         print a[i],
#     number = int(raw_input("\n插入一个数字:\n"))
#     end = a[9]
#     if number > end:
#         a[10] = number
#     else:
#         for i in range(10):
#             if a[i] > number:
#                 temp1 = a[i]
#                 a[i] = number
#                 for j in range(i + 1,11):
#                     temp2 = a[j]
#                     a[j] = temp1
#                     temp1 = temp2
#                 break
#     print '排序后列表:'
#     for i in range(11):
#         print a[i],

#2)
a = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]
b = 18
a.append(b)
c = a[:]
l = len(c)

# 从后面开始，如果比倒数第二个数大，那就将新加入的数填在倒数第一的位置，否则倒数第二的数位置后移
for i in range(l,0,-1):
   if (b>c[i-2]):
      c[i-1] =b
      break
   else:
      c[i-1] = c[i-2]
print c