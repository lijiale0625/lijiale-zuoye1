# -*- coding: utf-8 -*-

#在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。

#一般在类中定义的方法，在实例化的时候进行初始化，但是由于Python是动态语言
#在对象实例后也可以进行现场绑定，为实例绑定变量，为实例绑定方法，甚至临时的为类绑定方法


class Student():
    pass

StuA=Student()
StuA.name="Jeson"  #给实例绑定属性
print(StuA.name)


def set_age(self,age):    #定义一个函数
    self.age=age

from types import MethodType

StuA.set_age=MethodType(set_age,StuA)#给实例动态绑定方法
StuA.set_age(15)
print(StuA.age)
#但是这种方法只对当前实例有效，对其他实例无效，所以实例化的时候我们要给类做一个动态绑定
#其他实例调用set_age(15)方法时就会报错
# Stu1 =Student()
# Stu1.set_age(15)
# print (Stu1.age)


def set_score(self,score):
    self.score=score

Student.set_score=MethodType(set_score,Student) #给Student类动态绑定方法
StuB=Student()
StuB.set_score(75)
print(StuB.score)