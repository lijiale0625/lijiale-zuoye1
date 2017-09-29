#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr=='score':
            return 99
        if attr == 'name':
            return 'jingjing'
        #raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s = Student()
print s.name,s.score,s.age
#注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。
# 要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误