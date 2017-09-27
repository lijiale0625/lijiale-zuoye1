# -*- coding: cp936 -*-
#1）
# freqs = {}
# for i in "abracadabra":
#     try:
#         freqs[i] += 1
#     except:
#         freqs[i] = 1
# print freqs

#2
freqs = {}
for c in "abracadabra":
    freqs[c] = freqs.get(c, 0) + 1
    # Python字典(Dictionary)get()函数返回指定键的值，如果值不在字典中返回默认值。
    # dict.get(key, default=None)
    # key - - 字典中要查找的键。
    # default - - 如果指定键的值不存在时，返回该默认值值。
print freqs

#3）
from collections import defaultdict
freqs = defaultdict(int)
for c in "abracadabra":
    freqs[c] += 1
print freqs

#4
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#这里的defaultdict(function_factory)构建的是一个类似dictionary的对象，其中keys的值，自行确定赋值，
# 但是values的类型，是function_factory的类实例，而且具有默认值。比如default(int)则创建一个类似dictionary对象，
# 里面任何的values都是int的实例，而且就算是一个不存在的key, d[key] 也有一个默认值，这个默认值是int()的默认值0.
d = collections.defaultdict(list)
print d
for k, v in s:
    d[k].append(v)
    # d[k] += 1
print d
# list(d.items())
# print d

