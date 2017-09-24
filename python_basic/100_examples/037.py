# -*- coding:UTF-8 -*-
# 题目：对10个数进行排序。
# 程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

# l = [1,1,2,3,4,5,6,54,2,3,2]
# l.sort(reverse=False)
# print l
# l.sort(reverse=True)
# print l
#参考
list = []
for i in range(5):
    list.append( int(input('enter num{} number:'.format(i))))  #format定位符
list.sort()
print(list)