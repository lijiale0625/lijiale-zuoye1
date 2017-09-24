# -*- coding:utf-8 -*-

# 题目：按逗号分隔列表。
# 程序分析：无。
l=[1,2,3,4,5]
l1='asdfsa'.split('s')
print l1

L = [1,2,3,4,5]
s1 = ','.join(str(n) for n in L)
print s1
#2）
l = [1,2,3,4,5,6,7];
k = 1;
for i in l:
    print(i,end = ('' if (k == len(l)) else ','));
    k += 1;