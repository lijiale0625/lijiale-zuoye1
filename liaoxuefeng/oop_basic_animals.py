#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    pass
    # def run(self):
    #     print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()
# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('Start...')
class Timer1(object):
    pass

a = Animal()
d = Dog()   #继承animal，有run方法
c = Cat()       #继承animal，没有run方法
t = Timer()     #没有继承animal，有run方法
# t1 = Timer1()  #没有继承animal，也没有run方法

print('a is Animal?', isinstance(a, Animal))
print('a is Dog?', isinstance(a, Dog))
print('a is Cat?', isinstance(a, Cat))

print('d is Animal?', isinstance(d, Animal))
print('d is Dog?', isinstance(d, Dog))
print('d is Cat?', isinstance(d, Cat))

run_twice(a)
run_twice(d)
run_twice(c)
run_twice(t)
# run_twice(t1)