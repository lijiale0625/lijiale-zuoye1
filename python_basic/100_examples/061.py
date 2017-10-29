#!/usr/bin/python
# -*- coding: UTF-8 -*-

# if __name__ == '__main__':
#     a = []
#     for i in range(10):
#         a.append([])
#         for j in range(10):
#             a[i].append(0)
#     print a
    # for i in range(10):
    #     a[i][0] = 1
    #     a[i][i] = 1
    # for i in range(2, 10):
    #     for j in range(1, i):
    #         a[i][j] = a[i - 1][j - 1] + a[i - 1][j]
    # from sys import stdout
    #
    # for i in range(10):
    #     for j in range(i + 1):
    #         stdout.write(str(a[i][j]))
    #         stdout.write(' ')
    #     print

#参考
n =10
def lst(i,j):
    if i==j or j==1:
        return 1
    else:
        return lst(i-1,j-1) + lst(i-1,j)
for i in range(1,n+1):
    for j in range(1,i+1):
        print lst(i,j),
    print