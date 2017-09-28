#!/usr/bin/python
# -*- coding: UTF-8 -*-
from decimal import Decimal


########################################################################
class Fees(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self._fee = None

    # ----------------------------------------------------------------------
    def get_fee(self):
        """
        Return the current fee
        """
        return self._fee

    # ----------------------------------------------------------------------
    def set_fee(self, value):
        """
        Set the fee
        """
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value

f = Fees()
f.set_fee("1")
# print f.fee
#Decimal('1')
# f.fee = "2" #实际上是给实例f新加了一个属性，
# print f.fee
print f.get_fee()
#Decimal('2')

class Cls(object):
    def __init__(self):
        self.__x = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        # pass
        del self.__x


if __name__ == '__main__':
    c = Cls()
    c.x = 200
    y = c.x
    print("set & get y: %d" % y)

    del c.x
    # print c.x #删除了c.x，不存在了，
    print("del c.x & y: %d" % y)