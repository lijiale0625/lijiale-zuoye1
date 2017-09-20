#!/usr/bin/python
# -*- coding: UTF-8 -*-
######################################
i=[8,8,8,4,7,7,11,11,8]
dic = {}
for item in i :
    if  item in dic.keys():
        dic[item] += 1
    else:
        dic[item] = 1
print dic,list(dic),tuple(dic)
#第一种方法
# def fun(s):  #iteritems() 得到的[(键，值)]的列表，
#              # 通过sorted方法，指定排序的键值key是原来字典中的value属性，
#              # 其中用到了匿名函数lambda， 参数为t列表，返回第二个元素t[1]，也就是每个键值对中的value，
#              # 从小到大排序时 reverse=False，从大到小排序是True！
#     d = sorted(s.iteritems(), key=lambda t: t[1], reverse=True)
#     return d
# dic1 = fun(dic)
# print dic1
#第二种方法
#dict转成元组列表如：[(键，值)]
b = list(map(lambda x,y: (x,y), dic.keys(),dic.values()))
print b
# 方法1.用List的成员函数sort进行排序，在本地进行排序，不返回副本
# 方法2.用built-in函数sorted进行排序（从2.4开始），返回副本，原始输入不变
b1=b.sort(cmp=lambda x,y : cmp(x[1], y[1]),reverse=True)
b2=sorted(b,key=lambda t: t[1], reverse=True)
print b,b2
####################################
a = sorted(dic,cmp=lambda x,y:cmp(dic[x],dic[y]))
print a
a1 = sorted(dic,key=lambda k: dic[k])

# sorted(dic, cmp=None, key=dic[x], reverse=False)
#比较dict字典里value大小来排序，实际比较value值来排序key
from operator import itemgetter, attrgetter
sorted(dic.iteritems(), key=itemgetter(1), reverse=True)
print dic
#比较value值来排序key
d = {'a': 7, 'c': 4, 'b': 3, 'd': 4, 'f': 6, 'e': 1}
result = []
keys = sorted(d, key= lambda k: d[k])
print(keys)

s = {"a": "bb", "b": "cc", "c": "aa"}
def fun(s):
    d = sorted(s.iteritems(), key=lambda t: t[1], reverse=True)
    return d
d = fun(s)
d1 = fun(dic)
print d,d1