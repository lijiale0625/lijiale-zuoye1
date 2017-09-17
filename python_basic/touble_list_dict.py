# -*- coding: utf-8 -*-
#1、字典
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}

# #字典转为字符串，返回：<type 'str'> {'age': 7, 'name': 'Zara', 'class': 'First'}
# print type(str(dict)), str(dict)
# #字典可以转为元组，返回：('age', 'name', 'class')
# print tuple(dict)
# #字典可以转为元组，返回：(7, 'Zara', 'First')
# print tuple(dict.values())
#
# #字典转为列表，返回：['age', 'name', 'class']
# print list(dict)
#字典转为列表
# print list(dict.values())
#
# #2、元组
tup=(1, 2, 3, 4, )
print  type(tup)
#元组转为字符串，返回：(1, 2, 3, 4, 5)
print type(tup.__str__()) ,tup.__str__()

#元组转为列表，返回：[1, 2, 3, 4, 5]
print list(tup)

#元组不可以转为字典