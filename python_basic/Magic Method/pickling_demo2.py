#!/usr/bin/python
# -*- coding: UTF-8 -*-
# -*- coding: utf-8 -*-
import pickle
import time

class Slate:
    '''Class to store a string and a changelog, and forget its value when pickled.'''
    def __init__(self, value):
        self.value = value
        self.last_change = time.time()
        self.history = []

    def change(self, new_value):
        # 修改value, 将上次的valeu记录在history
        self.history.append((self.last_change, self.value))
        self.value = new_value
        self.last_change = time.time()

    def print_changes(self):
        print 'Changelog for Slate object:'
        for k, v in self.history:
            print '%s    %s' % (k, v)

    def __getstate__(self):
        # 故意不返回self.value和self.last_change,
        # 以便每次unpickle时清空当前的状态，仅仅保留history
        return self.history

    def __setstate__(self, state):
        self.history = state
        self.value, self.last_change = None, None

slate = Slate(0)
time.sleep(0.5)
slate.change(100)
time.sleep(0.5)
slate.change(200)
slate.change(300)
slate.print_changes()  # 与下面的输出历史对比
with open('slate.pkl', 'wb') as jar:
    pickle.dump(slate, jar)
del slate  # delete it
with open('slate.pkl', 'rb') as jar:
    slate = pickle.load(jar)
print 'current value:', slate.value  # None
print slate.print_changes()  # 输出历史记录与上面一致

# 在切片运算中将对象转化为int, 因此该方法的返回值必须是int。用一个例子来解释这个用法。
class Thing(object):
    def __index__(self):
        return 0


thing = Thing()
list_ = ['a', 'b', 'c']
print list_[thing]  # 'b'
print list_[thing:thing]  # []