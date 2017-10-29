# -*- coding: UTF-8 -*-
# 题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
# if __name__ == '__main__':
#     n = int(raw_input('整数 n 为:\n'))
#     m = int(raw_input('向后移 m 个位置为:\n'))
#
#
#     def move(array, n, m):
#         array_end = array[n - 1]
#         for i in range(n - 1, -1, - 1):
#             array[i] = array[i - 1]
#         array[0] = array_end
#         m -= 1
#         if m > 0: move(array, n, m)
#
#
#     number = []
#     for i in range(n):
#         number.append(int(raw_input('输入一个数字:\n')))
#     print '原始列表:', number
#
#     move(number, n, m)
#
#     print '移动之后:', number
#参考一
# from collections import deque
#
# m = 3
# a = [1,2,3,4,5,6,7]   # 7 个数
# f = deque(a)
# for i in f :
#     print i
# f.rotate(m)
# for i in f :
#     print i
# print list(f)
#参考二
a = [1, 2, 3, 4, 5]    # 测试列表
m = 3                  # 设置向后移动 3 位
for i in range(m):
    a.insert(0, a.pop())
print(a)
#参考三
from random import randint

data = [randint(1,110) for i in range(20)]
print(data)
n = 20
m = 5

# data[5:20]= data[0:15]
data[5:20], data[0:5] = data[0:15] ,data[15:20]
print(data)

#参考四
def rLoop(ls, m):
    n = len(ls)
    return ls[n-m:n]+ls[0:n-m]

ls = [i for i in range(1, 10)]
print(rLoop(ls, 3))
#参考五
n = int(input('整数 n 为:'))
m = int(input('向后移 m 个位置为:'))
L = []
for i in range(n):
    print('请输入第{}个数字:'.format(i+1), end='')
    L.append(int(input('')))
print('原始列表为：', L)
print('更新列表为：', L[n-m:] + L[:n-m])