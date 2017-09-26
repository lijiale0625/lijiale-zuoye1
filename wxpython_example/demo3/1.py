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

d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
    # d[k] += 1
print d
# list(d.items())
# print d