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