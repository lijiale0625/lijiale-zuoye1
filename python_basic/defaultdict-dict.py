# -*- coding: cp936 -*-
#1��
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
    # Python�ֵ�(Dictionary)get()��������ָ������ֵ�����ֵ�����ֵ��з���Ĭ��ֵ��
    # dict.get(key, default=None)
    # key - - �ֵ���Ҫ���ҵļ���
    # default - - ���ָ������ֵ������ʱ�����ظ�Ĭ��ֵֵ��
print freqs

#3��
from collections import defaultdict
freqs = defaultdict(int)
for c in "abracadabra":
    freqs[c] += 1
print freqs

#4
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
#�����defaultdict(function_factory)��������һ������dictionary�Ķ�������keys��ֵ������ȷ����ֵ��
# ����values�����ͣ���function_factory����ʵ�������Ҿ���Ĭ��ֵ������default(int)�򴴽�һ������dictionary����
# �����κε�values����int��ʵ�������Ҿ�����һ�������ڵ�key, d[key] Ҳ��һ��Ĭ��ֵ�����Ĭ��ֵ��int()��Ĭ��ֵ0.
d = collections.defaultdict(list)
print d
for k, v in s:
    d[k].append(v)
    # d[k] += 1
print d
# list(d.items())
# print d

