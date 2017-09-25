#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

def load_problem():
    filepath = './problem.txt'
    with open(filepath, 'r') as f:
        problem =[]
        answer = []
        txt = f.readlines()
        i = 1
        for i in range(len(txt)):
            if i%2 == 0:
                problem.append(txt[i].strip())
            else:
                answer.append(txt[i].strip())
    return problem, answer

if '__name__' == '__main__':
    a,b=load_problem()
    for i in range(a):
        print i