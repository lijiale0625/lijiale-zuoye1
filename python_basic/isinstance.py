#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

# 不要这样做

# if type(s) == type(""): ...
# if type(seq) == list or \
#                 type(seq) == tuple: ...
#
# # 应该这样
#
# if isinstance(s, basestring): ...
# if isinstance(seq, (list, tuple)): ...
a=u'aaaa'
print isinstance(a, basestring)
print isinstance(a, str)