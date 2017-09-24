# -*- coding:UTF-8 -*-
# 题目：求100之内的素数。
# 程序分析：无。
l=[]
for i in range(1,101):
    if i > 1:
        for j in range(2,i):
            if (i%j) == 0:
                break
        else:
            l.append(i)
print l

# 输出指定范围内的素数

# 用户输入数据
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))
s=[]
for num in range(lower, upper + 1):
    # 素数大于 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
            s.append(num)
print s
