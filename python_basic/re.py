
# -*- coding:utf-8 -*-
import re


def testsearchandmatch():
    s1 = "helloworld, i am 30 !"

    w1 = "world"
    m1 = re.search(w1, s1)
    if m1:
        print("find : %s" % m1.group())

    if re.match(w1, s1) == None :   #None
        print("cannot match")

    w2 = "helloworld"
    m2 = re.match(w2, s1)
    if m2:
        print("match : %s" % m2.group())
if __name__=="__main__":
    testsearchandmatch()