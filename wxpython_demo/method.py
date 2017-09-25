#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'lijiale'

from load_problem import load_problem
import random

global a
a = 0

problem, answer = load_problem()
problem_num = len(problem)
answer_num = len(answer)
# print problem_num
if problem_num != answer_num:
    print 'load data error!'

order = random.sample(range(problem_num), problem_num)
# print order

def get_problem():
    global a
    a = a + 1
    if a > problem_num:
         a = 0
    return problem[order[a-1]]

def get_answer():
    global a
    return answer[order[a-1]]