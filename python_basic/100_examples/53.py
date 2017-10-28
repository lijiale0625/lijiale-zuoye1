#!/usr/bin/python
# -*- coding: UTF-8 -*-
# ^	按位异或运算符：当两对应的二进位相异时，结果为1
# if __name__ == '__main__':
#     a = 077
#     b = a ^ 3
#     print 'The a ^ 3 = %d' % b
#     b ^= 7
#     print 'The a ^ b = %d' % b

if __name__ == '__main__':
    a = int(raw_input('input a number:\n'))
    b = a >> 3
    print b
    # c = ~(~0 << 4)
    # d = b & c
    # print '%o\t%o' %(a,d)